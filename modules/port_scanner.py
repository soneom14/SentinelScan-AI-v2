import socket

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((host, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"

            print(f"[+] Port {port} OPEN ({service})")
            return port

        return None

    except Exception as e:
        print(f"Error scanning port {port}: {e}")
        return None