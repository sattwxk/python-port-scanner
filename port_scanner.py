"""
port_scanner.py
Core scanning engine for the Python Port Scanner.
"""

import argparse
import logging
import socket
import threading
import sys
from datetime import datetime

from report import save_results
from utils import (
    print_banner,
    print_summary,
    resolve_target,
    validate_port_range,
)

# Thread-safe printing
print_lock = threading.Lock()

# Store scan results
results = []


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

            results.append(port_info)

            logging.info(f"OPEN {port} ({service})")

            with print_lock:
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

    return target, start, end, 1


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

    # If no arguments supplied → Interactive Mode
    if len(sys.argv) == 1:

        target, start_port, end_port, timeout = get_user_input()

    else:

        args = parser.parse_args()

        if args.target is None or args.start is None or args.end is None:
            parser.error("Please provide -t -s -e or run without arguments.")

        target = args.target
        start_port = args.start
        end_port = args.end
        timeout = args.timeout

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
    print()

    results.clear()

    start_time = datetime.now()

    threads = []

    for port in range(start_port, end_port + 1):

        thread = threading.Thread(
            target=scan_port,
            args=(target, port, timeout),
        )

        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = datetime.now()

    save_results(results)

    print_summary(
        target,
        start_port,
        end_port,
        len(results),
        end_time - start_time,
    )