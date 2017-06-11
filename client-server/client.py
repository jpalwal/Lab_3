import socket
import messages

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 50001)
print("Connecting to %s port %s" % server_address)
sock.connect(server_address)
md = messages.MsgDict()

try:
    while True:
        rec = sock.recv(1024)
        print("rec: ", rec)
        recm = messages.Message.decoding(rec)
        msg1 = md.handle(recm)
        if isinstance(msg1, messages.Exit):
            break
        if msg1:
            msg1 = msg1.encoding()
            sock.send(msg1)
except ConnectionAbortedError:
    pass
finally:
    print(msg1.message)
    sock.close()
    print("Connection closed")
    exit()
