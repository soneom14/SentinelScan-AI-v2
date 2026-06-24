import socket

def grab_banner(host, port):

    try:

        sock = socket.socket()
        sock.settimeout(2)

        sock.connect((host, port))

        if port == 80:
            sock.send(
                b"HEAD / HTTP/1.0\r\n\r\n"
            )

        banner = sock.recv(
            1024
        ).decode(
            errors="ignore"
        )

        sock.close()

        return banner.strip()

    except:

        return "Unknown"