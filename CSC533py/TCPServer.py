__author__ = 'Rasheed'

from socket import *

srv_socket = socket(AF_INET, SOCK_STREAM)

srv_socket.bind(('0.0.0.0', 9090))
srv_socket.listen(1)
'''
from socket import *

serverPort = 9090

serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('localhost',serverPort))

serverSocket.listen(1)

print 'The server is ready to receive'

while 1:
    connectionSocket, addr = serverSocket.accept()

    sentence = connectionSocket.recv(1024)

    capitalizedSentence = sentence.upper()

    connectionSocket.send(capitalizedSentence)

    connectionSocket.close()

'''