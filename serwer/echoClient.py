import socket
import sys
import logging
from os import path, remove


class MyEchoClient:
    def __init__(self, address, port, data_size):
        self.data_size = data_size
        self._createTcpIpSocket()
        self._connectToServer(address, port)
        if path.isfile("client.log"):
            remove("client.log")
        logging.basicConfig(filename="client.log", level=logging.INFO)
        logging.info("MyEchoClient initialization")

    def sendMsg(self, msg):
        self.sock.send(msg)
        response = self.sock.recv(self.data_size)
        self.sock.close()
        print('recieve %s ' % response)
        logging.info("Recieve %s " % response)

    def _createTcpIpSocket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logging.info("Create socket")

    def _connectToServer(self, address, port):
        server_address = (address, port)
        print('connecting to %s port %s' % server_address)
        self.sock.connect(server_address)
        logging.info("Connect to %s port %s" % server_address)


if __name__=='__main__':

    host = 'localhost'
    port = 50001
    data_size = 1024
    client = MyEchoClient(host, port, data_size)
