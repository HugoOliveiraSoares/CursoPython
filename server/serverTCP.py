import socket
HOST = ''              # Endereco IP do Servidor
PORT = 30800            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print 'Concetado por', cliente[0]
    while True:
        msg = con.recv(1024)
        if not msg:
            break
        print (msg)
        con.send(b'Eco =>' + msg)
    print 'Finalizando conexao do cliente', cliente
    con.close()
