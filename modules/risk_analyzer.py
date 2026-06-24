def get_risk(port):

    high_risk = [21, 23, 25]
    medium_risk = [22, 53, 110]

    if port in high_risk:
        return "HIGH"

    elif port in medium_risk:
        return "MEDIUM"

    else:
        return "LOW"