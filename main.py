import time
import socket

from modules.threaded_scanner import threaded_scan
from modules.report_generator import generate_report

print("=" * 40)
print("      SentinelScan-AI v3.0")
print("=" * 40)

target = input("Enter target IP address or hostname: ")

# Resolve hostname to IP
try:
    target_ip = socket.gethostbyname(target)
    print(f"Resolved IP: {target_ip}")
except socket.gaierror:
    print("Unable to resolve hostname.")
    exit()

start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

start_time = time.time()

# Multi-threaded scan
open_ports = threaded_scan(
    target_ip,
    start_port,
    end_port
)

end_time = time.time()

print("\n" + "=" * 40)
print("SCAN SUMMARY")
print("=" * 40)
print(f"Target: {target}")
print(f"Resolved IP: {target_ip}")
print(f"Ports Scanned: {end_port - start_port + 1}")
print(f"Open Ports: {len(open_ports)}")
print(f"Closed Ports: {(end_port - start_port + 1) - len(open_ports)}")
print(f"Open Port List: {open_ports}")
print(f"Scan Time: {round(end_time - start_time, 2)} seconds")
print("=" * 40)

generate_report(target, open_ports)