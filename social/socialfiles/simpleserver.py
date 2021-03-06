#!/usr/bin/env python

import socket
import datetime
import time

TCP_IP = '198.162.52.146'
TCP_PORT = 63109
BUFFER_SIZE = 64  # Normally 1024, but we want fast response
LOGFILE = "server.log"

f = open(LOGFILE, 'w+')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(5)

while 1:
  conn, addr = s.accept()
  data = conn.recv(BUFFER_SIZE)
  ts = time.time()  # time stamp
  dt = datetime.datetime.now()  # date time format
  outstring = str(ts) + '\t' + str(dt) + " from " + data + '\n'
  f.write(outstring)
  f.flush()
  conn.close()

f.close()
