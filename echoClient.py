import socket
import sys


class MyEchoClient:
    def __init__(self, address, port, data_size):
        self.data_size = data_size
        self.createTcpIpSocket()
        self.connectToServer(address, port)

    def sendMsg(self, msg):
        self.sock.send(msg)
        response = self.sock.recv(self.data_size)
        self.sock.close()
        print('recieve %s ' % response)

    def createTcpIpSocket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connectToServer(self, address, port):
        server_address = (address, port)
        print('connecting to %s port %s' % server_address)
        self.sock.connect(server_address)


if __name__=='__main__':

    host = 'localhost'
    port = 50001
    data_size = 1024
    client = MyEchoClient(host, port, data_size)
    client.sendMsg("Hello")