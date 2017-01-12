__author__ = 'Rasheed'

from socket import *
import time

server_name = '127.0.0.1'
server_port = 12000

client_socket = socket(AF_INET, SOCK_DGRAM)

message = "Ping"
min = 1.0
max = 0.0
rtt = 0.0
count = 0
total = 0

for i in xrange(1, 11):
    #print('ping number: ', i)

    start = time.clock()
    print "Ping " +  server_name + " #" + str(i) +" at " + str(start)
    client_socket.sendto(message, (server_name, server_port))
    client_socket.settimeout(1)

    try:

        server_message, server_address = client_socket.recvfrom(2048)
        end = time.clock()
        rtt = end - start
        if min > rtt:
            min = rtt
        if max < rtt:
            max = rtt
        count += 1
        total += rtt
        print server_message + " " + str(i) + " rtt=" + str(rtt)

    except timeout:
        print "Request time out"

print "\nmin-rtt=" + str(min) + " max-rtt=" + str(max) + " average-rtt=" + str(total / count)