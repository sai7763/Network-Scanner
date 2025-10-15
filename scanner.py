import socket
import threading

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        sock.close()
    except KeyboardInterrupt:
        exit()
    except socket.gaierror:
        print("Hostname could not be resolved.")
        exit()
    except socket.error:
        print("Could not connect to server.")
        exit()

def main():
    target = input("Enter target IP: ")
    print(f"Scanning target: {target}")
    for port in range(1, 1025):
        thread = threading.Thread(target=scan_port, args=(target, port))
        thread.start()

if __name__ == "__main__":
    main()
