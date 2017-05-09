import socket
import sys

class MyEchoServer:
    def __init__(self, address, port, data_size):
        self.data_size = data_size
        self.createTcpIpSocket()
        self.bindSocketToThePort(address, port)

    def handle_connection(self):
        self.sock.listen(1)
        while True:
            connection, client_address = self.sock.accept()
            data = connection.recv(self.data_size)
            if data:
                print(data)
                connection.send(data)
            connection.close()

    def createTcpIpSocket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bindSocketToThePort(self, address, port):
        server_address = (address, port)
        print('bind to %s port %s' % server_address)
        self.sock.bind(server_address)
