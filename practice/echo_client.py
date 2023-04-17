import socket

BUFSIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 2500)
s.connect(addr)

while True:
    msg = input("Message to send: ")
    s.send(msg.encode())
    data = s.recv(BUFSIZE)
    print("Received message: %s" % data.decode())

s.close()