import socket,sys
import common
from thread import *

class PlayerInterface:
  def __init__(self,id,server):
    self.id        = id
    self.ready     = False
    self.connected = True
    self.server    = server

  def send(self,cmd,*params):
    pass

  def execute(self,commands):
    for cmd,params in commands:
      if cmd in "mb":
        self.server.broadcast(cmd,self.id,*params)
      elif cmd in "w":
        self.server.broadcast(cmd,*params)
      elif cmd == "r":
        self.ready = True
        print("READY - "+str(self.id))
        self.server.playerReady()

class PlayerLocal(PlayerInterface):
  def __init__(self,id,server,event):
    PlayerInterface.__init__(self,id,server)
    self.event = event

  def send(self,cmd,*params):
    self.event.notify("cmdRecv",cmd,*params)

class PlayerRemote(PlayerInterface):
  def __init__(self,id,server,conn):
    PlayerInterface.__init__(self,id,server)
    self.conn   = conn
    self.server = server

    self.send("c",self.id)
    start_new_thread(self.listen,())

  def listen(self):
    while self.connected:
      data = self.conn.recv(common.packetSize)
      if data != "":
        print("RECV: "+data)
        commands = common.parse(data)
        self.execute(commands)

  def send(self,cmd,*params):
    data = common.package(cmd,params)
    self.conn.sendall(data)

class Server:
  def __init__(self, port, event):
    self.player_count = 0
    self.connections  = []
    self.event        = event
    self.socket       = self._initSocket();

    self.addPlayer() #Add the local player    
    start_new_thread(self.listen, ())
  
  def addPlayer(self,conn=None):
    if conn:
      self.connections.append(PlayerRemote(self.player_count,self,conn))
    else:
      self.connections.append(PlayerLocal(self.player_count,self,self.event))
    self.player_count += 1 
    
  def listen(self):
    while self.player_count <2:
      #wait to accept a connection - blocking call
      conn, addr = self.socket.accept()
      print 'New player connected with ' + addr[0] + ':' + str(addr[1])
      self.addPlayer(conn)
    print("Connected! Game Loading")

    self.event.notify("sendMap")

  def update(self):
    pass

  def getSocket(self):
    return self.socket
    
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
    for player in self.connections:
      if player.id >= 0:
        player.send(cmd,*params)

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
    #commands = []
    #commands.append(cmd,*params)
    self.connections[0].execute([(cmd,params)])

  def playerReady(self):
    ready = True
    for player in self.connections:
      if not player.ready:
        ready = False
    if ready:
      for player in self.connections:
        self.broadcast("a",player.id,0,player.id)
      self.broadcast("s")
