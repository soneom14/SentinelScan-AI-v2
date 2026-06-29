# 🛡️ SentinelScan-AI

> **An AI-Assisted Vulnerability Assessment & Network Reconnaissance Framework built with Python**

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge\&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-v4.0-orange?style=for-the-badge)

---

## Overview

SentinelScan-AI is a Python-based vulnerability assessment framework designed to automate network reconnaissance, service discovery, banner analysis, operating system detection, vulnerability lookup, and professional report generation.

The project combines fast multi-threaded scanning with intelligent risk analysis to produce actionable security reports in multiple formats.

---

## Features

### Network Scanning

* Multi-threaded TCP Port Scanner
* Custom Port Range Selection
* Fast Concurrent Scanning
* Banner Grabbing
* Service Detection

### Intelligence

* Risk Analysis Engine
* Local CVE Database Lookup
* CVSS Severity Classification
* Operating System Detection
* Service Enumeration

### Reporting

* TXT Report
* JSON Report
* HTML Report
* PDF Report
* Risk Summary

### User Experience

* Colored Terminal Interface
* Progress Bar
* Error Handling
* Professional Scan Summary

---

## Current Project Structure

```
SentinelScan-AI/

├── modules/
│   ├── banner_grabber.py
│   ├── cve_lookup.py
│   ├── os_detector.py
│   ├── pdf_report.py
│   ├── port_scanner.py
│   ├── report_generator.py
│   ├── risk_analyzer.py
│   ├── threaded_scanner.py
│   ├── ui.py
│   ├── utils.py
│   └── vulnerability_formatter.py
│
├── reports/
│
├── main.py
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Technologies Used

* Python 3
* Socket Programming
* ThreadPoolExecutor
* ReportLab
* Colorama
* tqdm
* JSON
* HTML/CSS

---

## Installation

Clone the repository:

```bash
git clone https://github.com/soneom14/SentinelScan-AI.git

cd SentinelScan-AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the scanner:

```bash
python main.py
```

Example:

```
Target: scanme.nmap.org

Port Range:
20-100

Detected Services:
SSH
HTTP

Detected Operating System:
Ubuntu Linux

Overall Risk:
MEDIUM
```

---

## Output Reports

After every scan the framework automatically generates:

* TXT Report
* JSON Report
* HTML Report
* PDF Report

Reports are saved inside the `reports/` directory.

---

## Example Scan Features

* Host Resolution
* Multi-threaded Port Scan
* Banner Grabbing
* Operating System Detection
* Local CVE Lookup
* Risk Classification
* Automated Report Generation

---

## Upcoming Features

* Interactive HTML Dashboard
* Advanced PDF Reports
* Live CVE Integration
* Service Version Detection
* CVSS Risk Scoring
* Security Recommendations
* CSV & XML Export
* GUI Application
* AI-generated Risk Summaries
* Network Mapping

---

## Disclaimer

This project is intended for educational purposes and authorized security testing only.

Do not scan systems without explicit permission.

---

## Author

**Om Sone**

Cybersecurity | Python | Ethical Hacking | Network Security

GitHub: https://github.com/soneom14

LinkedIn: https://www.linkedin.com/in/om-sone-ba591a352/
---

## License

This project is licensed under the MIT License.
