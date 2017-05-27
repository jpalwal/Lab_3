import socket
import messages


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 50001)
print("Connecting to %s port %s" % server_address)
sock.connect(server_address)
md = messages.MsgDict()

while True:
    data = sock.recv(1024)
    received_message = messages.Message.decoding(data)
    to_send = md.handle(received_message)
    if to_send == messages.MsgDict.Exit:
        break
    to_send = to_send.decoding()
    sock.send(to_send)

print(to_send.message)
sock.close()
print("Connection closed")
