__author__ = 'Rasheed'

from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

#mailserver to send mail through



mail_server = 'mail.nku.edu'
server_port = 25
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((mail_server, server_port))

recv = client_socket.recv(1024)

print(recv)
if recv[:3] != '220':
    print('220 reply not recived from server.')


helo_command = 'HELO Alice\r\n'
client_socket.send(helo_command)

recv1 = client_socket.recv(1024)

print(recv1)

if recv1[:3] != '250':
    print('250 reply not received from server.')

sender = raw_input("Enter sender email: ")
mailfrom_command = 'MAIL FROM: <' + sender + '>\r\n'
client_socket.send(mailfrom_command)
recv2 = client_socket.recv(1024)
print(recv2)

if recv2[:3] != '250':
    print('250 reply not received from server.')

recipient = raw_input("Enter recipient: ")
rcpt_command = 'RCPT TO: <' + recipient + '>\r\n'
client_socket.send(rcpt_command)
recv3 = client_socket.recv(1024)
print(recv3)

if recv2[:3] != '250':
    print('250 reply not received from server.')

#todo:accept multiline data
data_command = 'DATA\r\n'
client_socket.send(data_command)
recv4 = client_socket.recv(1024)
print(recv4)

if recv4[:3] != '354':
    print('354 reply not received from server.')

data = raw_input("Enter email body: ")
client_socket.send('\r\n' + data + '\r\n.\r\n')
#client_socket.send('\r\n.\r\n')
recv5 = client_socket.recv(1024)
print(recv5)

if recv5[:3] != '250':
    print('250 reply not received from server.')

client_socket.send('QUIT\r\n')
recv6 = client_socket.recv(1024)
print(recv6)

if recv6[:3] != '221':
    print('221 reply not received from server.')


client_socket.close()

