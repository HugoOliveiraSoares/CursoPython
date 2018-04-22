from socket import *

serverHOST = '192.168.0.15'
serverPORT = 30800
msg = [b'Ola,bem vindo!']

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHOST, serverPORT))

for linha in msg:
    sockobj.send(linha) #resposta do server
    data = sockobj.recv(1024)
    if not data:
        break
    print("cliente recebeu:", data)

sockobj.close()
