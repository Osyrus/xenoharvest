import socket,sys
import common
from thread  import *

class Client:
  def __init__(self,ip,port,event):
    self.event  = event
    self.socket = self._initSocket(ip,port)

  def update():
    data = socket.recv(1024).split(";")
    for i in data:
      if i != "":
        cmd,params = common.parse(i)
        self.event.notify("cmdRecv", cmd, *params)
        
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
