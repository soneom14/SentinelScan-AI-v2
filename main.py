from modules.port_scanner import scan_port
from modules.report_generator import generate_report
from modules.banner_grabber import grab_banner
import time

print("=" * 40)
print("      SentinelScan-AI v2.5")
print("=" * 40)

target = input("Enter target IP address: ")

start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

start_time = time.time()

open_ports = []

for port in range(start_port, end_port + 1):

    result = scan_port(target, port)

    if result:
        banner = grab_banner(target, port)

        print(f"    Banner: {banner}")

        open_ports.append(result)

end_time = time.time()

print("\n" + "=" * 40)
print("SCAN SUMMARY")
print("=" * 40)
print(f"Target: {target}")
print(f"Ports Scanned: {end_port - start_port + 1}")
print(f"Open Ports: {len(open_ports)}")
print(f"Closed Ports: {(end_port - start_port + 1) - len(open_ports)}")
print(f"Scan Time: {round(end_time - start_time, 2)} seconds")
print("=" * 40)

generate_report(target, open_ports)