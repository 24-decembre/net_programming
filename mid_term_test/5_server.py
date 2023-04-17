from socket import *
import sys

BUFSIZE = 1024
port = 9001

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)
conn, (remotehost, remoteport) = sock.accept()
print('connected by', remotehost, remoteport)

mbox = {}

while True:
    data = conn.recv(BUFSIZE)
    first_data = data.decode()
    print(first_data)
    conn.send('recv first data'.encode())
    if first_data == 'quit':
        conn.close()
    elif first_data == 'send':
        data = conn.recv(BUFSIZE)
        conn.send('recv send'.encode())
        mboxID = data.decode()
        data = conn.recv(BUFSIZE)
        message = data.decode()
        if mboxID in mbox.keys():
            mbox[mboxID].append(message)
        else:
            mbox[mboxID] = []
            mbox[mboxID].append(message)
        print(mbox)
    else:
        data = conn.recv(BUFSIZE)
        mboxID = data.decode()

        if mboxID in mbox.keys() and len(mbox[mboxID]):
            conn.send(mbox[mboxID].pop(0).encode())
        else:
            conn.send('No messages'.encode())
        
        
        print(mbox)

conn.close()


