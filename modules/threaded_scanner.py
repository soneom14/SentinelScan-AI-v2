from concurrent.futures import ThreadPoolExecutor
from modules.port_scanner import scan_port

def threaded_scan(target, start_port, end_port):

    results = []

    with ThreadPoolExecutor(max_workers=100) as executor:

        futures = [
            executor.submit(scan_port, target, port)
            for port in range(start_port, end_port + 1)
        ]

        for future in futures:
            results.append(future.result())

    return sorted(results, key=lambda x: x[0])