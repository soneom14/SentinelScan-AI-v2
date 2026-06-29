from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

from modules.port_scanner import scan_port


def threaded_scan(target, start_port, end_port):

    ports = list(range(start_port, end_port + 1))

    results = []

    with ThreadPoolExecutor(max_workers=100) as executor:

        futures = [
            executor.submit(scan_port, target, port)
            for port in ports
        ]

        for future in tqdm(
            futures,
            desc="Scanning Ports",
            colour="green"
        ):
            results.append(future.result())

    return sorted(results, key=lambda x: x["port"])