import socket
from colorama import Fore, init

init(autoreset=True)

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

            print(Fore.GREEN + f"[+] Port {port} OPEN ({service})")
            return port

        print(Fore.RED + f"[-] Port {port} CLOSED")
        return None

    except Exception as e:
        print(Fore.YELLOW + f"Error: {e}")
        return None