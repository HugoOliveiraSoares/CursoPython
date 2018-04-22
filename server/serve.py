import socket
from os import system

ip = '0.0.0.0'
port = 30800

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind((ip, port))
    server.listen(5)

    print("Escutando %s %s" %(ip,port))

    (obj,cliente) = server.accept()
    print("Conexao recebida de %s" %cliente[0])

    while True:
        msg = obj.recv(1024)
        if not msg:
            break
        #print(msg)
        if msg == 'ls':
            print("Voce tentou obter os arquivos do sitema ")
            system('ls')
        elif msg == 'ip':
            system('ifconfig')
        else:
            print("Comando invalido")
    server.close()
except Exception as erro:
    print(erro)
    server.close()
