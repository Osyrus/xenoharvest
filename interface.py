from unit import *

class Interface:
  def __init__(self,socket,event,map,units):
    self.socket = socket
    self.event  = event
    self.map    = map
    self.units  = units
    event.register("moveOrder",self.moveOrder)
    event.register("cmdRecv",self.parse)
    event.register("playerAdd",self.addPlayer)
    
  def moveOrder(self,x,y):
    self.socket.send("m"+str(x)+","+str(y))
    
  def addPlayer(self,id,x,y):
    self.units.add(Player(x,y,id,self.event,self.map))
    
  def parse(self,data):
    cmd = data[0]
    msg = data[1:]

    if cmd == 't':
      print "[Player "+str(player.id+1)+"] "+msg
    elif cmd == 'm':
      params = msg.split(',')
      if params >= 2:
        self.event.notify("playerMove",int(params[0]),float(params[1]),float(params[2]))
    elif cmd == 'a':
      params = msg.split(',')
      self.event.notify("playerAdd",int(params[0]),int(params[1]),int(params[2]))
  