"""
utils.py
Helper functions used throughout the project.
"""

import socket


def print_banner():
    """
    Display application banner.
    """

    print("=" * 60)
    print("        Python Multi-threaded Port Scanner")
    print("=" * 60)


def resolve_target(target):
    """
    Resolve hostname to IP address.

    Returns:
        str : IP Address
        None : If resolution fails
    """

    try:
        return socket.gethostbyname(target)

    except socket.gaierror:
        return None


def validate_port_range(start_port, end_port):
    """
    Validate port numbers.

    Returns:
        bool
    """

    if start_port < 1:
        return False

    if end_port > 65535:
        return False

    if start_port > end_port:
        return False

    return True


def print_summary(target, start_port, end_port, open_ports, duration):
    """
    Display scan summary.
    """

    print()
    print("=" * 60)
    print("                Scan Summary")
    print("=" * 60)

    print(f"Target            : {target}")
    print(f"Port Range        : {start_port} - {end_port}")
    print(f"Open Ports Found  : {open_ports}")
    print(f"Scan Duration     : {duration}")

    print("=" * 60)


def is_valid_ip(ip):
    """
    Check whether a string is a valid IPv4 address.
    """

    try:
        socket.inet_aton(ip)
        return True

    except socket.error:
        return False


def service_name(port):
    """
    Return the standard service name for a port.
    """

    try:
        return socket.getservbyport(port)

    except OSError:
        return "Unknown"


def separator():
    """
    Print a separator line.
    """

    print("-" * 60)