import socket   #for sockets
import sys  #for exit
#import pygame
from thread  import *

players = []
self_id = -1

def serverlisten(socket,event):  
  while True:
    data = socket.recv(1024)
    if not data:
      break
    cmds = data.split(';')
    for i in cmds:
      if i:
        event.notify("cmdRecv", i)
        
def connect(ip, port, event):
  try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit()

  print 'Socket Created'
  s.connect((ip,port))
  start_new_thread(serverlisten ,(s,event,))
  return s
  
def disconnect(socket):
  socket.sendall("d")
  socket.close()