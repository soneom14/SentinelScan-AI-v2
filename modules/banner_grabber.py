import socket

def grab_banner(host, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)

        sock.connect((host, port))

        banner = sock.recv(1024).decode(errors="ignore").strip()

        sock.close()

        if banner:
            return banner

        return "Banner not available"

    except:
        return "Banner not available"