import socket,sys
import common
from thread import *

class PlayerConn:
  def __init__(self,conn,server,id=-1):
    self.id     = id
    self.conn   = conn
    self.server = server
    self.ready  = False

    self.send("c",self.id)
    server.broadcast("a",0,0,self.id)

  def update(self):
    data = self.conn.recv(common.packetSize)
    if data != "":
      commands = common.parse(data)
      for cmd,params in commands:
        server.broadcast(cmd,self.id,*params)

  def send(self,cmd,*params):
    data = common.package(cmd,params)
    self.conn.sendall(data)

class Server:
  def __init__(self, port, event):
    self.player_count = 1
    self.connections  = []
    self.event        = event
    self.socket       = self._initSocket();
    
    start_new_thread(self.listen, (self.socket, ))
    
    
  def listen(self, socket):
    while self.player_count <2:
      #wait to accept a connection - blocking call
      conn, addr = socket.accept()
      print 'New player connected with ' + addr[0] + ':' + str(addr[1])
     
      self.connections.append(PlayerConn(conn,self,self.player_count))
      self.player_count += 1

    self.event.notify("sendMap")
    
#  def receive(self,player,cmd,params):
#
#    if cmd == 't':
#      self.broadcast("t",player.id,params[0])
#    elif cmd == 'm':
#      if params >= 2:
#        self.broadcast("m",player.id,*params)
#    elif cmd == 'b':
#      params = msg.split(',')
#      if params >= 2:
#        self.event.notify("serverBuild",params[0],params[1],params[2])
#        self.broadcast("b"+params[0]+","+params[1]+","+params[2])

  def broadcast(self,cmd,*params):
    self.event.notify("cmdRecv",cmd,*params)
    for player in self.connections:
      if player.id >= 0:
        player.send(cmd,*params)

  #Function for handling connections. This will be used to create threads
#  def clientThread(self,conn):
#    player = Player()
#    player.id = self.player_count - 1
#    conn.sendall("c"+str(player.id)+";")
#    self.broadcast("a"+str(player.id)+","+str(player.x)+","+str(player.y))
#    
#    for i in self.connections:
#      if i != 0:
#        pass
       
    #infinite loop so that function do not terminate and thread do not end.
          
    #came out of loop
#    conn.close()

  def _initSocket(self):
    HOST = ''   # Symbolic name meaning all available interfaces
    PORT = 8888 # Arbitrary non-privileged port
 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    #Bind socket to local host and port
    try:
      s.bind((HOST, PORT))
    except socket.error , msg:
      print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
      sys.exit()
   
    #Start listening on socket
    s.listen(8)
    print 'Socket initialised'
    return s

  def transmit(self,cmd,*params):
    self.broadcast(cmd,0,*params)