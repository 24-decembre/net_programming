from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    msg = input('input formula: ')
    if msg == 'q':
        break
    s.send(msg.encode())
    try:
        data = s.recv(1024)
    except:
        break
    else:
        if not data:
            break
    print('Received answer: ', data.decode())



s.close()