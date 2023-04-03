from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())
    studentName = client.recv(1024)
    print(studentName.decode())
    studentNum = 20181517
    client.send(studentNum.to_bytes(4,'big'))
    client.close()