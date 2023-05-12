from socket import *

nPortID = 600

sock = socket(AF_INET, SOCK_STREAM, 0)
sock.bind(("", nPortID))
sock.listen(5)

(newsock, addr) = sock.accept()
sock.close()

while True:
    bMessage = newsock.recv(1024, 0)
    print("Recieved: ",
          bMessage.decode())

newsock.close();
# To test fire up a browser and enter 127.0.0.1:600/any_old_text

