import socket
import time

from modules.threaded_scanner import threaded_scan
from modules.banner_grabber import grab_banner
from modules.risk_analyzer import analyze_risk
from modules.report_generator import generate_report

print("=" * 40)
print("      SentinelScan-AI v4.0")
print("=" * 40)

target = input(
    "\nEnter target IP address or hostname: "
)

try:

    ip_address = socket.gethostbyname(
        target
    )

    print(
        f"Resolved IP: {ip_address}"
    )

except:

    print(
        "Unable to resolve hostname."
    )

    exit()

start_port = int(
    input("Enter start port: ")
)

end_port = int(
    input("Enter end port: ")
)

start_time = time.time()

results = threaded_scan(
    ip_address,
    start_port,
    end_port
)

open_ports = []

for result in results:

    if result["is_open"]:

        banner = grab_banner(
            ip_address,
            result["port"]
        )

        open_ports.append({

            "port":
            result["port"],

            "service":
            result["service"],

            "banner":
            banner
        })

end_time = time.time()

risk_data, overall_risk = analyze_risk(
    open_ports
)

print("\n" + "=" * 40)
print("SCAN SUMMARY")
print("=" * 40)

print(f"Target: {target}")
print(f"Resolved IP: {ip_address}")

print(
    f"Ports Scanned: "
    f"{end_port - start_port + 1}"
)

print(
    f"Open Ports: "
    f"{len(open_ports)}"
)

print(
    f"Closed Ports: "
    f"{(end_port - start_port + 1) - len(open_ports)}"
)

print(
    f"Open Port List: "
    f"{[p['port'] for p in open_ports]}"
)

print(
    f"Overall Risk: "
    f"{overall_risk}"
)

print(
    f"Scan Time: "
    f"{round(end_time - start_time, 2)} seconds"
)

print("=" * 40)

generate_report(
    target,
    open_ports,
    risk_data,
    overall_risk
)