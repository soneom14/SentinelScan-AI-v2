from modules.port_scanner import scan_port

print("SentinelScan AI v2.0")

target = input("Enter the target IP address: ")

ports = [21,22,23,25,53,80,110,443] 

for port in ports:
    scan_port(target, port)   
    