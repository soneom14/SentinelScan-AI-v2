from datetime import datetime
import json


def generate_report(
    target,
    open_ports,
    risk_data,
    overall_risk
):

    txt_file = f"reports/report_{target}.txt"
    html_file = f"reports/report_{target}.html"
    json_file = f"reports/report_{target}.json"
    xml_file = f"reports/report_{target}.xml"

    # ======================
    # TXT REPORT
    # ======================

    with open(txt_file, "w", encoding="utf-8") as report:

        report.write("SentinelScan-AI v4 Report\n")
        report.write("=" * 60 + "\n")

        report.write(f"Target: {target}\n")
        report.write(f"Generated: {datetime.now()}\n")
        report.write(f"Overall Risk: {overall_risk}\n\n")

        for item in risk_data:

            report.write(
                f"Port {item['port']} | "
                f"{item['service']} | "
                f"{item['risk']} | "
                f"{item['banner']}\n"
            )

    # ======================
    # JSON REPORT
    # ======================

    json_data = {
        "target": target,
        "generated": str(datetime.now()),
        "overall_risk": overall_risk,
        "ports": risk_data
    }

    with open(json_file, "w", encoding="utf-8") as report:

        json.dump(
            json_data,
            report,
            indent=4
        )

    # ======================
    # HTML REPORT
    # ======================

    rows = ""

    for item in risk_data:

        rows += f"""
        <tr>
            <td>{item['port']}</td>
            <td>{item['service']}</td>
            <td>{item['banner']}</td>
            <td class="{item['risk'].lower()}">
                {item['risk']}
            </td>
        </tr>
        """

    html_content = f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<title>SentinelScan-AI Report</title>

<style>

body {{
    background:#0d1117;
    color:white;
    font-family:Arial;
    padding:30px;
}}

h1 {{
    color:#58a6ff;
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
    font-weight:bold;
}}

.medium {{
    color:orange;
    font-weight:bold;
}}

.low {{
    color:lime;
    font-weight:bold;
}}

</style>

</head>

<body>

<h1>SentinelScan-AI v4 Report</h1>

<div class="card">

<h2>Target Information</h2>

<p><b>Target:</b> {target}</p>

<p><b>Generated:</b> {datetime.now()}</p>

<p><b>Overall Risk:</b> {overall_risk}</p>

</div>

<div class="card">

<h2>Open Ports ({len(open_ports)})</h2>

<table>

<tr>
<th>Port</th>
<th>Service</th>
<th>Banner</th>
<th>Risk</th>
</tr>

{rows}

</table>

</div>

</body>

</html>
"""

    with open(html_file, "w", encoding="utf-8") as report:

        report.write(html_content)

    # ======================
    # XML REPORT
    # ======================

    xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>

<SentinelScanAI>

    <Target>{target}</Target>

    <Generated>{datetime.now()}</Generated>

    <OverallRisk>{overall_risk}</OverallRisk>

    <Ports>
"""

    for item in risk_data:

        xml_content += f"""

        <Port>

            <Number>{item['port']}</Number>

            <Service>{item['service']}</Service>

            <Banner><![CDATA[{item['banner']}]]></Banner>

            <Risk>{item['risk']}</Risk>

        </Port>
"""

    xml_content += """

    </Ports>

</SentinelScanAI>
"""

    with open(xml_file, "w", encoding="utf-8") as report:

        report.write(xml_content)

    print(f"\n[+] TXT Report Saved: {txt_file}")
    print(f"[+] HTML Report Saved: {html_file}")
    print(f"[+] JSON Report Saved: {json_file}")
    print(f"[+] XML Report Saved: {xml_file}")