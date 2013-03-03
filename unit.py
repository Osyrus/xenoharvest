#from map import *
class Unit:
  def __init__(self,x,y,event,map):
    self.x        = 64*x
    self.y        = 64*y
    self.path     = [(x,y)]
    self.event    = event
    self.map      = map
    self.speed    = 4
    event.register("update",self.update)

  def move(self,x,y):
    self.path = self.map.getPath(self.path[0], (x,y))
    
  def update(self):
    reached = True
    
    if self.x > 64*self.path[0][0]:
      self.x -= self.speed
      reached = False
    elif self.x < 64*self.path[0][0]:
      self.x += self.speed
      reached = False
    
    if self.y > 64*self.path[0][1]:
      self.y -= self.speed
      reached = False
    elif self.y < 64*self.path[0][1]:
      self.y += self.speed
      reached = False
      
    if reached:
      if len(self.path)>1:
        self.path.pop(0)
        
class Player(Unit):
  def __init__(self,x,y,id,event,map):
    Unit.__init__(self,x,y,event,map)
    self.id       = id
    event.register("playerMove",self.moveID)
    
  def moveID(self,id,x,y):
    if id == self.id:
      self.move(x,y)