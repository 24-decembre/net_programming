from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('',3333))
s.listen(2)
def calculator(str):
    
    operator = str.split(' ')
    if(operator[1] == '+'):
        return int(operator[0]) + int(operator[2])
    elif(operator[1] == '-'):
        return int(operator[0]) - int(operator[2])
    elif(operator[1] == '*'):
        return int(operator[0]) * int(operator[2])
    elif(operator[1] == '/'):
        return round(int(operator[0]) / int(operator[2]), 1)
    else:
        return "use +,-,*,/ operator"
    


while True:
    Client, addr = s.accept()
    while True:
        try:
            formula = Client.recv(1024).decode()
            Client.send(str(calculator(formula)).encode())
        except:
            break

    Client.close()
