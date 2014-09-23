#!/usr/bin/env python

import socket
import datetime
import time

TCP_IP = '198.162.52.143' # lamport.cs.ubc.ca
TCP_PORT = 63109
BUFFER_SIZE = 64  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(5)

while 1:
  conn, addr = s.accept()
  data = conn.recv(BUFFER_SIZE)
  if data:
    print "received ", data 
    conn.send(data) 
  conn.close()

f.close()
