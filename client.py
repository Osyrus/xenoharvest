import socket,sys
import common
from thread  import *

class Client:
  def __init__(self,ip,port,event):
    self.event     = event
    self.socket    = self._initSocket(ip,port)
    self.connected = True

    start_new_thread(self.listen,())

  def listen(self):
    while self.connected:
      data = self.socket.recv(common.packetSize)
      for cmd,params in common.parse(data):
        print(cmd)
        self.event.notify("cmdRecv", cmd, *params)

  def update(self):
    pass
        
  def _initSocket(self,ip,port):
    try:
      #create an AF_INET, STREAM socket (TCP)
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
      print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
      sys.exit()

    s.connect((ip,port))
    return s

  def transmit(self,cmd,*params):
    socket.sendall(common.package(cmd,params))
