import socket
import threading

clients = [] # 클라이언트 목록

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 2500))
s.listen()

print('Server Started')

def handler(conn, addr):
    clients.append(conn)
    print('new client', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        msg = data.decode()
        print(msg)
        # 모든 클라이언트에게 전송
        for client in clients:
            if client != conn:
                client.send(msg.encode())
    print(addr, 'exited')
    clients.remove(conn)
    conn.close()

while True:
    conn, addr = s.accept()
    th = threading.Thread(target=handler, args=(conn, addr))
    th.daemon = True
    th.start()

