import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9999))
s.listen(5)

while True:
    client, addr = s.accept()
    print('connection from ', addr)
    client.send(time.ctime(time.time()).encode())
    client.close()


# 클라이언트가 타임서버에 접속하여 시간을 읽어오는 프로그램