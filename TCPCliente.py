import socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((socket.gethostname(),1234))
sentence = input('lowercase sentence:')
clientSocket.send(bytes(sentence, "utf-8"))
modifiedSentence = clientSocket.recv(1024)
print('From Server:', modifiedSentence.decode("utf-8"))
clientSocket.close()