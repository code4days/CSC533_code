
from socket import*
import time
import re

class WebServer:

    __author__ = 'Rasheed'

    #todo:think about identifying filetypes by header information not extention
    #todo:add better exception handling

    '''
        Server content supported:
        html, javascript, css, jpg, mp4
    '''

    def construct_header(self, http_code, filetype=None, data_size=0):
        """function to construct header lines based on file type and http response code"""

        header_lines = ""
        server_name = "Rasheed-Server/1.0.0"
        content_types = {
            'html' : "text/html",
            'jpg'  : "image/jpeg",
            'mp4'  : "video/mp4",
            'js'   : "text/javascript",
            'css'  : "text/css",
            'map'  : "application/octet-stream",
            "bmp"  : "image/bmp",
            "htm"  : "text/html",
            "ico"  : "image/x-icon",
            "jpeg" : "image/jpeg",
            "mp3"  : "audio/mpeg",
            "zip"  : "application/zip",
            "pdf"  : "application/pdf",
            "png"  : "image/png",
            "ogg"  : "application/ogg",
            "gif"  : "image/gif"
        }

        if http_code == 404 and filetype == None:
            header_lines = "HTTP/1.1 404 Not Found\n"
            header_lines += "Content-type: text/plain\n"
            header_lines += "Date: " + time.strftime("%c") + "\n"
            header_lines += "Server: " + server_name + "\n\n"

        if http_code == 200:
            header_lines = "HTTP/1.1 200 OK\n"
            header_lines += "Content-type: " + content_types[filetype] + "\n"
            header_lines += "Content-Length: " + str(data_size) + "\n"
            header_lines += "Date: " + time.strftime("%c") + "\n"
            header_lines += "Server: " + server_name + "\n\n"

        return header_lines

    def build_server_socket(self):
        server_port = 5555
        server_name = 'localhost'
        server_socket = socket(AF_INET, SOCK_STREAM)
        server_socket.bind((server_name, server_port))
        server_socket.listen(5)
        print 'Rasheed-Server v1.0.0 running on port:', server_port
        return server_socket


    def find_file_extension(self, filename):
        return re.match(".+\.(\w+)$", filename).group(1)

    def start_server(self):
        # in a class server_socket will be an instance variable initialized in constructor??
        server_socket = self.build_server_socket()
        while True:

            #wait for connection from client
            connection_socket, addr = server_socket.accept()
            try:
                #receive request from client
                message = connection_socket.recv(4096)

                #print request to console
                print(message)

                #extract file name from reqeust
                filename = message.split()[1]

                #open file and load it into output_data var
                f = open(filename[1:], 'rb')
                output_data = f.read()
                #output_data = f.readlines()

                #close file
                f.close()

                #filetype = filename.split('.')[1]

                #identify file type by extension
                if filename:
                    filetype = self.find_file_extension(filename)

                #Send HTTP header lines into socket for 200 OK
                connection_socket.send(self.construct_header(200, filetype, len(output_data)))

                #Send the content of the reqeusted file to the client
                connection_socket.sendall(output_data)

                #Close the connection with this particular client
                connection_socket.close()

            except IOError:
                #send 404 Not Found for IO exceptions
                connection_socket.send(self.construct_header(404))
                connection_socket.send(" 404 file not there!!!")
                connection_socket.close()

        server_socket.close()

#create instance of WebServer
rasheed_server = WebServer()

#call start_server() method to start web server
rasheed_server.start_server()