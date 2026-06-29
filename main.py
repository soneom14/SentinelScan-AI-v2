import socket
import time

from colorama import Fore, init

from modules.threaded_scanner import threaded_scan
from modules.banner_grabber import grab_banner
from modules.risk_analyzer import analyze_risk
from modules.report_generator import generate_report
from modules.pdf_report import generate_pdf_report
from modules.cve_lookup import lookup_cves
from modules.vulnerability_formatter import print_vulnerabilities
from modules.os_detector import detect_os

from modules.ui import (
    show_banner,
    success,
    error,
    info,
)

from modules.utils import title

# ==========================================
# Initialize Colorama
# ==========================================

init(autoreset=True)

# ==========================================
# Banner
# ==========================================

show_banner()
title("SentinelScan-AI v4.0")

# ==========================================
# Target Input
# ==========================================

target = input(
    "\nEnter target IP address or hostname: "
).strip()

try:

    ip_address = socket.gethostbyname(target)

    success(f"Resolved IP : {ip_address}")

except socket.gaierror as e:

    error(f"Unable to resolve hostname.")
    print(Fore.RED + f"Reason : {e}")
    exit()

# ==========================================
# Port Range
# ==========================================

while True:

    try:

        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))

        if start_port < 1 or end_port > 65535 or start_port > end_port:

            error("Invalid port range.")
            continue

        break

    except ValueError:

        error("Please enter valid numbers.")

# ==========================================
# Start Scan
# ==========================================

info("Starting threaded scan...\n")

start_time = time.time()

results = threaded_scan(
    ip_address,
    start_port,
    end_port
)

end_time = time.time()

success("Scan Completed!\n")

# ==========================================
# Process Results
# ==========================================

open_ports = []

for result in results:

    if result["is_open"]:

        banner = grab_banner(
            ip_address,
            result["port"]
        )

        open_ports.append({

            "port": result["port"],
            "service": result["service"],
            "banner": banner

        })

# ==========================================
# Risk Analysis
# ==========================================

risk_data, overall_risk = analyze_risk(
    open_ports
)
os_name, confidence = detect_os(open_ports)

# ==========================================
# Statistics
# ==========================================

total_ports = end_port - start_port + 1

closed_ports = total_ports - len(open_ports)

scan_time = round(
    end_time - start_time,
    2
)

# ==========================================
# Scan Summary
# ==========================================

print()

print(Fore.CYAN + "=" * 60)
print(Fore.YELLOW + "SCAN SUMMARY".center(60))
print(Fore.CYAN + "=" * 60)


print(Fore.WHITE + f"Target         : {target}")
print(Fore.WHITE + f"Resolved IP    : {ip_address}")
print(Fore.WHITE + f"Ports Scanned  : {total_ports}")

print(Fore.GREEN + f"Open Ports     : {len(open_ports)}")
print(Fore.RED + f"Closed Ports   : {closed_ports}")

print(
    Fore.WHITE +
    f"Open Port List : {[p['port'] for p in open_ports]}"
)

print(Fore.YELLOW + f"Overall Risk   : {overall_risk}")

print(Fore.CYAN + f"Scan Time      : {scan_time} sec")

print(Fore.CYAN + "=" * 60)

print()
print(Fore.CYAN + "=" * 60)
print(Fore.YELLOW + "OPERATING SYSTEM DETECTION".center(60))
print(Fore.CYAN + "=" * 60)

print(Fore.WHITE + f"Likely OS     : {os_name}")
print(Fore.WHITE + f"Confidence    : {confidence}%")

print(Fore.CYAN + "=" * 60)

# ==========================================
# Open Port Details
# ==========================================

if open_ports:

    print("\n" + Fore.GREEN + "OPEN PORT DETAILS")
    print(Fore.GREEN + "-" * 90)

    print(
        f"{'PORT':<8}"
        f"{'SERVICE':<18}"
        f"{'BANNER'}"
    )

    print("-" * 90)

    for port in open_ports:

        banner = port["banner"]

        if not banner:
            banner = "Banner not available"

        elif len(banner) > 60:
            banner = banner[:60] + "..."

        print(
            f"{port['port']:<8}"
            f"{port['service']:<18}"
            f"{banner}"
        )

        cves = lookup_cves(
            port["service"]
        )

        print_vulnerabilities(
            cves
        )

        print("-" * 90)

else:

    error("No open ports found.")
# ==========================================
# Generate Reports
# ==========================================

generate_report(
    target,
    open_ports,
    risk_data,
    overall_risk
)

try:

    generate_pdf_report(
        target=target,
        risk_data=risk_data,
        overall_risk=overall_risk,
        total_ports=total_ports,
        open_ports=len(open_ports),
        closed_ports=closed_ports,
        scan_time=scan_time,
        ip_address=ip_address,
    )

except PermissionError:

    error(
        "PDF is currently open. Close it and scan again."
    )

except Exception as e:

    error(
        f"PDF Generation Failed : {e}"
    )

# ==========================================
# Finish
# ==========================================

success("All reports generated successfully.")
print(Fore.GREEN + "Scan finished successfully.")