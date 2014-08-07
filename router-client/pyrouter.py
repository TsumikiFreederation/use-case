import socket
import time
import thread


def deserialize(message):      
  """
  Returns the sequence of the packet, and movement hint.
  """
  if "|" in message:
    seq, move = message.split("|")
  else:
    seq = message
    move = None
  return (seq, move)


def recvack(sock):
  while 1:
    message, addr = sock.recvfrom(1024)
    seq, move = deserialize(message)
    #print "received " + seq + "th ack"
  

############ define protocol parameters ############ 
LENGTH = 1000    # packet length (change for different tx rates)
RTTWIN = 10      # check packet loss every RTTWIN ack
WIN = 1000        # window size to check for packet loss
sequenceno = 1   # sequence number of packets, starting from 1 to WIN

DEBUG = 0     # output some debug messages if DEBUG == 1 
              # TODO: make this a command line arg
CYCLE = 1  # time duration to calculate throughput

(destip, destport) = ('206.87.192.231', 63101)

port = 63100
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", port))

try:
   thread.start_new_thread(recvack, (s, ))
except:
   print "Error: unable to start thread"
   
lastchecktime = time.time()
totalbits = 0   # record total bytes received
totaltime = 0
sendtotal = 0   # time to send WIN packets
   
while 1:
  starttime = time.time()
  
  while sequenceno <= WIN:
    packet = str(sequenceno) + "|" + '0'*LENGTH 
    sendstarts = time.time()
    s.sendto(packet, (destip, destport))
    sendends = time.time()
    
    sendtotal = sendtotal + sendends - sendstarts
    totalbits = totalbits + len(packet)*8
    
    currenttime = time.time()
    totaltime = currenttime - lastchecktime
    
    if totaltime > CYCLE:
      # check throughput and movement every CYCLE sec
      lastchecktime = currenttime # reset clock
      throughput = float(totalbits)/(totaltime)/1000000 
      print "send rate: " + str(throughput) + " Mbps\n"
      totalbits = 0  # reset bits
      
    sequenceno = sequenceno + 1

  endtime = time.time()  # record time after sending WIN packets
  print "it took " + str(endtime-starttime) + "sec to send " + str(WIN) + " pkts of " + str(LENGTH) + "bytes. time spent sendto: " + str(sendtotal) + 'sec\n'             
  sendtotal = 0
  sequenceno = 1
