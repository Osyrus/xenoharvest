from unit import *
import towers

class Interface:
  def __init__(self,socket,event,map,units, buildings):
    self.socket = socket
    self.event  = event
    self.map    = map
    self.units  = units
    self.buildings = buildings
    event.register("moveOrder",self.moveOrder)
    event.register("cmdRecv",self.parse)
    event.register("playerAdd",self.addPlayer)
    event.register("towerAdd", self.addTower)
    event.register("buildOrder", self.buildOrder)
    
  def moveOrder(self,x,y):
    self.socket.send("m"+str(x)+","+str(y))

  def buildOrder(self, type, x, y):
    self.socket.send("b"+str(type)+","+str(x)+","+str(y))
    
  def addPlayer(self,id,x,y):
    self.units.add(Player(x,y,id,self.event,self.map))

  def addTower(self,type,x,y):
    self.buildings.add(towerType(x, y, type))
    
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
    elif cmd == 'b':
      params = msg.split(',')
      self.event.notify("towerAdd",int(params[0]),int(params[1]),int(params[2]))

def towerType(x, y, type):
  if type == 1:
    return towers.LaserTower(x, y)
  elif type == 2:
    return towers.FlameTower(x, y)
  elif type == 3:
    return towers.CannonTower(x, y)
  elif type == 4:
    return towers.RocketTower(x, y)
  elif type == 5:
    return towers.SlowTower(x, y)
  elif type == 6:
    return towers.LureTower(x, y)
  else:
    return None