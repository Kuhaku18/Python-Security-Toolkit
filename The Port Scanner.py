# Port Scanner - A network security tool utilizing the socket library to identify open ports on a target server.
import socket
target = "scanme.nmap.org"
ports = [21, 22, 80, 443]
for port in ports:
    s = socket.socket()
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is OPEN!")
    else:
        print(f"Port {port} is CLOSED!")