import socket


def scan_port(target, port):
    # Create a TCP socket
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Don't wait forever if a port doesn't respond
    scanner.settimeout(1)

    # Try connecting to the target and port
    result = scanner.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] Port {port}")
    else:
        print(f"[CLOSED] Port {port}")

    scanner.close()


def main():
    print("=" * 50)
    print("        Python Port Scanner")
    print("=" * 50)

    target = input("Enter Target IP: ")

    start_port = int(input("Enter Start Port: "))
    end_port = int(input("Enter End Port: "))

    print(f"\nScanning {target} from Port {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        scan_port(target, port)


if __name__ == "__main__":
    main()