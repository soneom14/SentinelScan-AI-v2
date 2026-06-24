import socket

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((host, port))
        sock.close()

        if result == 0:

            try:
                service = socket.getservbyport(port)

            except:
                service = "Unknown"

            return {
                "port": port,
                "is_open": True,
                "service": service
            }

        return {
            "port": port,
            "is_open": False,
            "service": None
        }

    except:

        return {
            "port": port,
            "is_open": False,
            "service": None
        }