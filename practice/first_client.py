import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
s.connect(addr)

msg = s.recv(1024)
print(msg.decode())
s.close()