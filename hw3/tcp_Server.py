from socket import *

s = socket(AF_INET,SOCK_STREAM)
s.bind(('',9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())
    studentName = client.recv(1024)
    # bytes 객체로 받은 studentName을 문자열로 변환
    print(studentName.decode())
    studentNum = 20181517
    # 정수를 네트워크 바이트 순서의 bytes 객체로 변경 후 전송
    client.send(studentNum.to_bytes(4,'big'))
    client.close()