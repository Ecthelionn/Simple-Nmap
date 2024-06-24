import socket
import threading


def get_own_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


def scan_port(ip, port, open_ports):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    if s.connect_ex((ip, port)) == 0:
        try:
            service_name = socket.getservbyport(port)
        except OSError:
            service_name = "Unknown"
        open_ports.append((port, service_name))
    s.close()
def scan_ports(ip, ports):
    open_ports = []
    threads = []
    for port in ports:
        thread = threading.Thread(target=scan_port, args=(ip, port, open_ports))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return open_ports

def main():
    popular_ports = [
        1, 3, 7, 9, 13, 17, 19, 20, 21, 22, 23, 25, 26, 30, 32, 33, 37, 42, 43, 49,
        53, 70, 79, 80, 81, 82, 83, 84, 85, 88, 89, 90, 99, 100, 106, 109, 110, 111,
        113, 119, 125, 135, 139, 143, 144, 146, 161, 163, 179, 199, 211, 212, 222,
        254, 255, 256, 259, 264, 280, 301, 306, 311, 340, 366, 389, 406, 407, 416,
        417, 425, 427, 443, 444, 458, 464, 465, 481, 497, 500, 512, 515, 524, 541,
        543, 544, 545, 548, 554, 555, 563, 587, 593, 616, 617, 625, 631, 636, 646,
        648, 666, 667, 683, 687, 691, 700, 705, 711, 714, 720, 722, 726, 749, 765,
        777, 783, 787, 800, 801, 808, 843, 873, 880, 888, 898, 900, 901, 902, 903,
        911, 912, 981, 987, 990, 992, 993, 995, 999, 1000
    ]

    ip = get_own_ip()
    print(f"Your IP Address is: {ip}")

    print("Select an option for port scanning:")
    print("1. Scan the first 100 popular ports")
    print("2. Scan a specific port")
    print("3. Scan all ports (1-65535)")

    option = input("Enter your choice (1/2/3): ")

    if option == '1':
        ports = popular_ports[:100]
    elif option == '2':
        port = int(input("Enter the port number to scan: "))
        ports = [port]
    elif option == '3':
        ports = range(1, 65536)
    else:
        print("Invalid option")
        return

    print(f"Scanning open ports on {ip}...")
    open_ports = scan_ports(ip, ports)
    print("Open ports:")
    for port, service_name in open_ports:
        print(f"Port {port}: {service_name}")

if __name__ == "__main__":
    main()
