import socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input('lowercase sentence:')
clientSocket.sendto(bytes(message, "utf-8"),(socket.gethostname(),1234))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode("utf-8"))
clientSocket.close()