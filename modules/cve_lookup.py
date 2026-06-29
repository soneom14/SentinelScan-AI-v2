# ==========================================
# SentinelScan-AI v5
# Local CVE Database
# ==========================================

CVE_DATABASE = {

    "ssh": [

        {
            "id": "CVE-2018-15473",
            "severity": "HIGH",
            "cvss": 7.5,
            "description": "OpenSSH Username Enumeration",
            "impact": "Allows attackers to enumerate valid usernames.",
            "recommendation": "Upgrade OpenSSH to the latest version.",
            "reference": "https://nvd.nist.gov/vuln/detail/CVE-2018-15473"
        },

        {
            "id": "CVE-2016-0777",
            "severity": "HIGH",
            "cvss": 7.8,
            "description": "OpenSSH Information Leak",
            "impact": "May leak private memory contents.",
            "recommendation": "Disable roaming or upgrade OpenSSH.",
            "reference": "https://nvd.nist.gov/vuln/detail/CVE-2016-0777"
        }

    ],

    "http": [

        {
            "id": "CVE-2021-41773",
            "severity": "HIGH",
            "cvss": 7.5,
            "description": "Apache Path Traversal",
            "impact": "Allows attackers to read arbitrary files.",
            "recommendation": "Upgrade Apache to version 2.4.51 or later.",
            "reference": "https://nvd.nist.gov/vuln/detail/CVE-2021-41773"
        },

        {
            "id": "CVE-2021-42013",
            "severity": "CRITICAL",
            "cvss": 9.8,
            "description": "Apache Remote Code Execution",
            "impact": "Allows attackers to execute arbitrary code.",
            "recommendation": "Upgrade Apache immediately.",
            "reference": "https://nvd.nist.gov/vuln/detail/CVE-2021-42013"
        }

    ],

    "ftp": [

        {
            "id": "CVE-2011-2523",
            "severity": "CRITICAL",
            "cvss": 10.0,
            "description": "vsFTPd Backdoor",
            "impact": "Remote attackers may gain shell access.",
            "recommendation": "Upgrade vsFTPd.",
            "reference": "https://nvd.nist.gov/vuln/detail/CVE-2011-2523"
        }

    ],

    "smtp": [

        {
            "id": "CVE-2020-28017",
            "severity": "MEDIUM",
            "cvss": 5.3,
            "description": "SMTP Information Disclosure",
            "impact": "Server information may be exposed.",
            "recommendation": "Apply vendor patches.",
            "reference": "https://nvd.nist.gov"
        }

    ],

    "mysql": [

        {
            "id": "CVE-2016-6662",
            "severity": "CRITICAL",
            "cvss": 9.8,
            "description": "MySQL Privilege Escalation",
            "impact": "Allows privilege escalation.",
            "recommendation": "Upgrade MySQL.",
            "reference": "https://nvd.nist.gov"
        }

    ]
}


def lookup_cves(service):

    service = service.lower()

    return CVE_DATABASE.get(service, [])