from modules.port_scanner import scan_port
from modules.report_generator import generate_report

print("=" * 40)
print("      SentinelScan-AI v2.0")
print("=" * 40)

target = input("Enter target IP address: ")

ports = [21, 22, 23, 25, 53, 80, 110, 443]

open_ports = []

for port in ports:
    result = scan_port(target, port)

    if result:
        open_ports.append(result)

print("\nScan Complete")

if open_ports:
    print(f"Open Ports Found: {open_ports}")
else:
    print("No open ports found.")

generate_report(target, open_ports)