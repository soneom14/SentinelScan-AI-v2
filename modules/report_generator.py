from datetime import datetime

def generate_report(
    target,
    open_ports,
    risk_data,
    overall_risk
):

    txt_file = f"reports/report_{target}.txt"
    html_file = f"reports/report_{target}.html"

    with open(txt_file, "w") as report:

        report.write("SentinelScan-AI v4 Report\n")
        report.write("=" * 50 + "\n")
        report.write(f"Target: {target}\n")
        report.write(f"Generated: {datetime.now()}\n")
        report.write(f"Overall Risk: {overall_risk}\n\n")

        for item in risk_data:

            report.write(
                f"Port {item['port']} | "
                f"{item['service']} | "
                f"{item['risk']}\n"
            )

    html_content = f"""
<!DOCTYPE html>
<html>

<head>

<title>SentinelScan-AI Report</title>

<style>

body {{
    background:#0d1117;
    color:white;
    font-family:Arial;
    padding:30px;
}}

.card {{
    background:#161b22;
    padding:20px;
    border-radius:10px;
    margin-bottom:20px;
}}

table {{
    width:100%;
    border-collapse:collapse;
}}

th, td {{
    padding:12px;
    border:1px solid #30363d;
}}

th {{
    background:#21262d;
}}

.high {{
    color:red;
}}

.medium {{
    color:orange;
}}

.low {{
    color:lime;
}}

</style>

</head>

<body>

<h1>SentinelScan-AI v4 Report</h1>

<div class="card">
<h3>Target Information</h3>

<p><b>Target:</b> {target}</p>
<p><b>Generated:</b> {datetime.now()}</p>
<p><b>Overall Risk:</b> {overall_risk}</p>

</div>

<div class="card">

<h3>Open Ports ({len(open_ports)})</h3>

<table>

<tr>
<th>Port</th>
<th>Service</th>
<th>Risk</th>
</tr>

{''.join([
f'''
<tr>
<td>{item["port"]}</td>
<td>{item["service"]}</td>
<td class="{item["risk"].lower()}">{item["risk"]}</td>
</tr>
'''
for item in risk_data
])}

</table>

</div>

</body>

</html>
"""

    with open(html_file, "w") as report:
        report.write(html_content)

    print(f"\n[+] TXT Report Saved: {txt_file}")
    print(f"[+] HTML Report Saved: {html_file}")