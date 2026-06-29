import socket

def resolve_target(target):
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        return None