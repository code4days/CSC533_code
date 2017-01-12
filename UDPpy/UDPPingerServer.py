__author__ = 'Rasheed'

import random
from socket import *


def build_server_socket():
    server_port = 12000
    server_name = 'localhost'

    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind(('localhost', 12000))
    print "Server started..."

    return server_socket

def start_server():
    server_socket = build_server_socket()
    while True:
        rand = random.randint(0, 10)
        message, address = server_socket.recvfrom(1024)
        #message = message.upper()
        message = "Pong"

        if rand < 4:
            continue

        #print message
        server_socket.sendto(message, address)

if __name__ == '__main__':
    start_server()
