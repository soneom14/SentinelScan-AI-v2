from concurrent.futures import ThreadPoolExecutor
from modules.port_scanner import scan_port

def threaded_scan(target, start_port, end_port):
    open_ports = []

    def worker(port):
        result = scan_port(target, port)
        if result:
            open_ports.append(result)

    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(worker, range(start_port, end_port + 1))

    return sorted(open_ports)