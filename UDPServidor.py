import socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((socket.gethostname(),1234))
print('The server is ready to receive')
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = (message.decode("utf-8")).upper()
    serverSocket.sendto(bytes(modifiedMessage, "utf-8"), clientAddress)