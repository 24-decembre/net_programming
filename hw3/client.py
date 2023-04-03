from socket import *

sock = socket(AF_INET, SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())
studentname = "Gahyeon Kim"
sock.send(studentname.encode())
studentNum = sock.recv(1024)
print(int.from_bytes(studentNum, 'big'))
sock.close()