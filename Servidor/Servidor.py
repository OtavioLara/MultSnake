import socket
import os
import sys

class Server(object):
    def __init__(self, host="localhost", port=5000):
        self.HOST = host
        self.PORT = port
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def startServer(self):
        orig = (self.HOST, self.PORT)
        self.tcp.bind(orig)
        self.tcp.listen(1)
        while True:
            con, cliente = self.tcp.accept()
            pid = os.fork()
            if pid == 0:
                self.tcp.close()
                print 'Conectado por', cliente
                while True:
                    msg = con.recv(1024)
                    if not msg: break
                    print cliente, msg
                print 'Finalizando conexao do cliente', cliente
                con.close()
                sys.exit(0)
            else:
                con.close()

if __name__ == '__main__':
    servidor_pincipal = Server()
    servidor_pincipal.startServer()
