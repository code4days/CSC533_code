from socket import *

import sys
import pprint

if len(sys.argv) <=1:
    print('Usage: "python proxy_server.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server]')
    sys.exit(2)

print(sys.argv[1])
tcp_server_socket = socket(AF_INET, SOCK_STREAM)
tcp_server_socket.bind((sys.argv[1], 8888))
tcp_server_socket.listen(5)

while 1:

    print('Ready to serve...')

    tcp_client_socket, addr = tcp_server_socket.accept()
    print('Received a connection from:', addr)

    message = tcp_client_socket.recv(1024)
    print('MESSAGE: ' + message)# prints entire request header

    print('MESSAGE.split: ' + message.split()[1]) #/norserage.com


    filename = message.split()[1].partition("/")[2]
    print('FILENAME: ' + filename) #filename = norserage.com


    file_exist = "false"
    file_to_use = "/" + filename
    print('FILE_TO_USE' + file_to_use) #/norserage

    try:
        f = open(file_to_use[1:], "r")
        output_data = f.readlines()
        file_exist = "true"

        tcp_client_socket.send("HTTP/1.0 200 OK\r\n")
        tcp_client_socket.send("Content-Type:text/html\r\n")
        tcp_client_socket.send("Content-Length:" + str(len(output_data)))

        for i in range(0, len(output_data)):
            tcp_client_socket.send(output_data[i])
        print('Read from cache')

    except IOError:
        if file_exist == "false":
            c = socket(AF_INET, SOCK_STREAM)
            hostn = filename.replace("www.","",1)
            print ('HOSTN: ' + hostn)

            try:
                c.connect((hostn, 80))
                file_obj = c.makefile('r', 0)
                file_obj.write(("GET "+"http://" + filename + "HTTP/1.0\n\n"))

                #response = c.recv(4096)
                buff = file_obj.readlines()


                #pprint.pprint(buff)

                final = []
                for line in buff:
                    l = line.replace('href="/', 'href="http://' + filename + '/')
                    l = l.replace('src="/', 'href="http://' + filename + '/')
                    final.append(l)

                tmp_file = open("./" + filename, "wb")

                for i in final:
                    tmp_file.write(i)
                    tcp_client_socket.send(i)
                '''
                tmp_file = open("./" + filename, "wb")
                for i in buff:
                    tmp_file.write(i)
                    tcp_client_socket.send(i)
                '''

            except Exception as e:
                print("Illegal request")
                #print(e)


        else:
            tcp_client_socket.send("HTTP/1.0 404 Not Found\r\n")
            tcp_client_socket.send("Content-Type:text/html\r\n")

        tcp_client_socket.close()

tcp_server_socket.close()