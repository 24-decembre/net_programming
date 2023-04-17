import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9999))
print("Time: ", sock.recv(1024).decode())
sock.close()


# 클라이언트가 타임서버에 접속하여 시간을 읽어오는 프로그램