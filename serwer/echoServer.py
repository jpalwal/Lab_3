import socket
import sys
import logging
from os import path, remove

class MyEchoServer:
    def __init__(self, address, port, data_size):
        self.data_size = data_size
        self.createTcpIpSocket()
        self.bindSocketToThePort(address, port)
        if path.isfile("server.log"):
            remove("server.log")
        logging.basicConfig(filename="server.log", level=logging.INFO)
        logging.info("MyEchoServer initialization")

    def handle_connection(self):
        logging.info("Handling connection")
        self.sock.listen(1)
        #while True:
        logging.info("Waiting for connection")
        connection, client_address = self.sock.accept()
        data = connection.recv(self.data_size)
        if data:
            logging.info("Data recevied")
            connection.send(data)
        connection.close()

    def createTcpIpSocket(self):
        logging.info("Socket created")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bindSocketToThePort(self, address, port):
        server_address = (address, port)
        print('bind to %s port %s' % server_address)
        self.sock.bind(server_address)
        logging.info("Bind to %s port %s" % server_address)

if __name__=='__main__':

    host = 'localhost'
    port = 50001
    data_size = 1024
    server = MyEchoServer(host, port, data_size)
    server.handle_connection()
