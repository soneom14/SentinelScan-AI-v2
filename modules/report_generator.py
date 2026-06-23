from datetime import datetime

def generate_report(target, open_ports):
    filename = f"reports/report_{target}.txt"

    with open(filename, "w") as report:
        report.write("SentinelScan-AI v2 Report\n")
        report.write("=" * 40 + "\n")
        report.write(f"Target: {target}\n")
        report.write(f"Scan Time: {datetime.now()}\n\n")

        report.write(f"Total Open Ports: {len(open_ports)}\n\n")

        if open_ports:
            report.write("Open Ports:\n")
            for port in open_ports:
                report.write(f"- Port {port}\n")
        else:
            report.write("No open ports found.\n")

    print(f"\n[+] Report saved as {filename}")