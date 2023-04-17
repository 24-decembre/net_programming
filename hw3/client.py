from socket import *

sock = socket(AF_INET, SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

msg = sock.recv(1024)
print(msg.decode())

while True:
    studentname = input("GH or JH을 입력하세요: ")
    sock.send(studentname.encode())
    studentNum = sock.recv(1024)
    # 수신한 bytes 객체(네트워크 바이트 순서)를 호스트 바이트 순서 정수로 변경
    print(int.from_bytes(studentNum, 'big'))
    