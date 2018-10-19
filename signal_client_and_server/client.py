# coding: utf-8
# client

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('localhost', 8888))
for i in range(1000000):
    sock.sendall(b'hello')
# print(sock.recv(1024))
# sock.close()

print('send over')