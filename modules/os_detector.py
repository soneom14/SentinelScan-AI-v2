def detect_os(open_ports):

    banners = ""

    for port in open_ports:

        if port["banner"]:
            banners += port["banner"].lower() + " "

    if "ubuntu" in banners:
        return "Ubuntu Linux", 95

    elif "debian" in banners:
        return "Debian Linux", 92

    elif "centos" in banners:
        return "CentOS Linux", 90

    elif "red hat" in banners:
        return "Red Hat Enterprise Linux", 90

    elif "linux" in banners:
        return "Linux", 85

    elif "iis" in banners:
        return "Windows Server", 92

    elif "microsoft" in banners:
        return "Windows", 88

    elif "freebsd" in banners:
        return "FreeBSD", 90

    elif "cisco" in banners:
        return "Cisco IOS", 94

    return "Unknown", 0