import socket

def scan_ports(target, ports):
    open_ports = []

    total_ports = len(ports)
    progress = 0

    print("+---------------------------------+")
    print("|      Port Scanning Progress     |")
    print("+---------------------------------+")

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

        progress += 1
        percent_complete = (progress / total_ports) * 100
        print("| {:<2}% [{}]".format(int(percent_complete), "=" * int(percent_complete / 2)).ljust(35) + "|")

    print("+---------------------------------+")
    return open_ports

def main():
    print("                          ")
    print("="*30)
    target = input("Enter the target IP address or hostname: ")
    print("="*30)
    port_range = input("Enter the range of ports to scan (e.g., 1-100): ")
    print("="*30)

    start_port, end_port = map(int, port_range.split('-'))
    ports_to_scan = range(start_port, end_port + 1)

    open_ports = scan_ports(target, ports_to_scan)

    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(port)
    else:
        print("No open ports found.")

if __name__ == "__main__":
    print("                               ")
    print("+"*30)
    print("Agent RXD's Port Scanner     ")
    print("+"*30)
    main()
