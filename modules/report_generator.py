from datetime import datetime

def generate_report(target, open_ports):

    txt_file = f"reports/report_{target}.txt"
    html_file = f"reports/report_{target}.html"

    # TXT REPORT
    with open(txt_file, "w") as report:

        report.write("SentinelScan-AI v3 Report\n")
        report.write("=" * 40 + "\n")
        report.write(f"Target: {target}\n")
        report.write(f"Scan Time: {datetime.now()}\n\n")

        report.write(f"Open Ports Found: {len(open_ports)}\n\n")

        for port in open_ports:
            report.write(f"- Port {port}\n")

    # HTML REPORT
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>SentinelScan-AI Report</title>

        <style>
            body {{
                font-family: Arial;
                background-color: #0d1117;
                color: white;
                padding: 40px;
            }}

            h1 {{
                color: #58a6ff;
            }}

            .card {{
                background: #161b22;
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 20px;
            }}

            ul {{
                line-height: 1.8;
            }}
        </style>
    </head>

    <body>

        <h1>SentinelScan-AI v3 Report</h1>

        <div class="card">
            <h3>Target Information</h3>
            <p><b>Target:</b> {target}</p>
            <p><b>Generated:</b> {datetime.now()}</p>
        </div>

        <div class="card">
            <h3>Open Ports Found ({len(open_ports)})</h3>

            <ul>
                {''.join([f'<li>Port {port}</li>' for port in open_ports])}
            </ul>
        </div>

    </body>
    </html>
    """

    with open(html_file, "w") as html_report:
        html_report.write(html_content)

    print(f"\n[+] TXT Report Saved: {txt_file}")
    print(f"[+] HTML Report Saved: {html_file}")