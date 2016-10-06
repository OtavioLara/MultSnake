#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
class Cliente(object):

    def __init__(self, host="localhost", port=5000):
        self.destine = (host,port)
        self.tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcp.connect(self.destine)

    def conect(self):
        print "para sair digit 'fechar' \n"
        msg = raw_input()
        while msg <> "fechar":
            self.tcp.send(msg)
            msg = raw_input()
        print "conexão terminada"
        self.tcp.close()

if __name__ == '__main__':
    cli = Cliente()
    cli.conect()