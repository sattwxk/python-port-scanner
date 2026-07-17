"""
port_scanner.py
Core scanning engine for the Python Port Scanner.
"""

import argparse
import logging
import socket
import threading
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

from report import save_results
from utils import (
    print_banner,
    print_summary,
    resolve_target,
    validate_port_range,
)

# Thread-safe printing / shared state
print_lock = threading.Lock()

# Store scan results
results = []

DEFAULT_WORKERS = 200


def scan_port(target, port, timeout=1):
    """
    Scan a single TCP port.
    """

    try:
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(timeout)

        result = scanner.connect_ex((target, port))

        if result == 0:

            # Detect service
            try:
                service = socket.getservbyport(port)
            except OSError:
                service = "Unknown"

            # Banner grabbing
            try:
                scanner.send(b"\r\n")
                banner = scanner.recv(1024).decode(errors="ignore").strip()

                if not banner:
                    banner = "No Banner"

            except Exception:
                banner = "No Banner"

            port_info = {
                "Port": port,
                "Service": service,
                "Banner": banner,
            }

            logging.info(f"OPEN {port} ({service})")

            with print_lock:
                results.append(port_info)

                print("=" * 60)
                print(f"[OPEN] Port    : {port}")
                print(f"Service        : {service}")
                print(f"Banner         : {banner}")

        scanner.close()

    except Exception as e:
        logging.error(str(e))


def get_user_input():
    """
    Interactive mode if no command-line arguments are provided.
    """

    print("\nInteractive Mode\n")

    target = input("Enter Target IP / Hostname : ").strip()

    while True:
        try:
            start = int(input("Enter Start Port        : "))
            end = int(input("Enter End Port          : "))

            if validate_port_range(start, end):
                break

            print("\nInvalid port range.\n")

        except ValueError:
            print("\nPlease enter valid numbers.\n")

    return target, start, end, 1, DEFAULT_WORKERS


def run():

    parser = argparse.ArgumentParser(
        description="Python Multi-threaded Port Scanner"
    )

    parser.add_argument(
        "-t",
        "--target",
        help="Target hostname or IP address",
    )

    parser.add_argument(
        "-s",
        "--start",
        type=int,
        help="Starting Port",
    )

    parser.add_argument(
        "-e",
        "--end",
        type=int,
        help="Ending Port",
    )

    parser.add_argument(
        "--timeout",
        default=1,
        type=int,
        help="Socket timeout",
    )

    parser.add_argument(
        "-w",
        "--workers",
        default=DEFAULT_WORKERS,
        type=int,
        help=f"Max concurrent threads (default: {DEFAULT_WORKERS})",
    )

    # If no arguments supplied → Interactive Mode
    if len(sys.argv) == 1:

        target, start_port, end_port, timeout, workers = get_user_input()

    else:

        args = parser.parse_args()

        if args.target is None or args.start is None or args.end is None:
            parser.error("Please provide -t -s -e or run without arguments.")

        target = args.target
        start_port = args.start
        end_port = args.end
        timeout = args.timeout
        workers = args.workers

    if not validate_port_range(start_port, end_port):
        print("\nInvalid port range.\n")
        return

    target = resolve_target(target)

    if target is None:
        print("\nUnable to resolve hostname.\n")
        return

    logging.basicConfig(
        filename="scanner.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    print_banner()

    print(f"Target     : {target}")
    print(f"Port Range : {start_port} - {end_port}")
    print(f"Workers    : {workers}")
    print()

    results.clear()

    start_time = datetime.now()

    port_count = end_port - start_port + 1
    max_workers = min(workers, port_count)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(scan_port, target, port, timeout)
            for port in range(start_port, end_port + 1)
        ]

        for future in futures:
            future.result()

    end_time = datetime.now()

    save_results(results)

    print_summary(
        target,
        start_port,
        end_port,
        len(results),
        end_time - start_time,
    )