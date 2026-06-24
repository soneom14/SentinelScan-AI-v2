def analyze_risk(open_ports):

    risk_data = []

    high_risk_ports = [
        21,
        23,
        445,
        3389
    ]

    medium_risk_ports = [
        22,
        80,
        443
    ]

    for port_info in open_ports:

        port = port_info["port"]

        if port in high_risk_ports:
            risk = "HIGH"

        elif port in medium_risk_ports:
            risk = "MEDIUM"

        else:
            risk = "LOW"

        risk_data.append({

            "port": port,

            "service":
            port_info["service"],

            "banner":
            port_info["banner"],

            "risk": risk
        })

    if any(
        item["risk"] == "HIGH"
        for item in risk_data
    ):
        overall_risk = "HIGH"

    elif any(
        item["risk"] == "MEDIUM"
        for item in risk_data
    ):
        overall_risk = "MEDIUM"

    else:
        overall_risk = "LOW"

    return risk_data, overall_risk