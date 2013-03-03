import socket
import sys
from thread import *

class Server:
  def __init__(self, port, event):
    self.player_count = 0
    self.connections = []
    self.event = event

    self.socket = initSocket();
    
    start_new_thread(self.listen, (self.socket, ))
    
    
    
    
    
  def listen(self,socket):
    while True:
      #wait to accept a connection - blocking call
      conn, addr = socket.accept()
      print 'New player connected with ' + addr[0] + ':' + str(addr[1])
     
      #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
      self.connections.append(conn)
      self.player_count += 1
      start_new_thread(self.clientThread ,(conn,))
   
    s.close()
      
 
  def parse(self,data,player):
    cmd = data[0]
    msg = data[1:]

    if cmd == 't':
      print "[Player "+str(player.id+1)+"] "+msg
      self.broadcast("t"+str(player.id)+","+msg)
    elif cmd == 'm':
      params = msg.split(',')
      if params >= 2:
        print "[Player "+str(player.id+1)+" > "+params[0]+","+params[1]+"]"
        self.event.notify("serverMove", player.id, params[0],params[1])
        self.broadcast("m"+str(player.id)+","+params[0]+","+params[1])
    elif cmd == 'b':
      params = msg.split(',')
      if params >= 2:
        self.event.notify("serverBuild",params[0],params[1],params[2])
        self.broadcast("b"+params[0]+","+params[1]+","+params[2])

  def broadcast(self,data):
    data = data+';'
    for i in self.connections:
      if i != 0:
        i.sendall(data)

  #Function for handling connections. This will be used to create threads
  def clientThread(self,conn):
    player = Player()
    player.id = self.player_count - 1
    conn.sendall("c"+str(player.id)+";")
    self.broadcast("a"+str(player.id)+","+str(player.x)+","+str(player.y))
    
    for i in self.connections:
      if i != 0:
        pass
       
    #infinite loop so that function do not terminate and thread do not end.
    while True:     
      #Receiving from client
      data = conn.recv(1024)
      if not data:
        break
      cmds = data.split(';')
      for i in cmds:
        self.parse(i,player)
          
    #came out of loop
    conn.close()

def initSocket():
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

