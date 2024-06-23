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


def scan_ports(ip):
    open_ports = []
    threads = []
    for port in range(1, 65535):
        thread = threading.Thread(target=scan_port, args=(ip, port, open_ports))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return open_ports


def main():
    ip = get_own_ip()
    print(f"Your IP Address is: {ip}")
    print(f"Scanning open ports on {ip}...")
    open_ports = scan_ports(ip)
    print("Open ports:")
    for port, service_name in open_ports:
        print(f"Port {port}: {service_name}")


if __name__ == "__main__":
    main()
