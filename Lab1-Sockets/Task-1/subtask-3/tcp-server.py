import socket
from datetime import datetime
import time


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 5555

server_socket.bind((host, port))
server_socket.listen(5)
print('The server is waiting for connection......')
client_socket, addr = server_socket.accept()
while True:
    client_message = client_socket.recv(1024)
    if client_message.decode('utf-8') == 'stop':
        server_socket.close()
        break
    print('Client message:' + client_message.decode('utf-8') +
          "\nTime to receive the message:" + str(datetime.now()))