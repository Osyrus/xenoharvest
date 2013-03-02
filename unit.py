#from map import *

class Unit:
  def __init__(self,x,y,event,map):
    self.x        = 64*x
    self.y        = 64*y
    self.path     = [(x,y)]
    self.event    = event
    self.map      = map
    event.register("update",self.update)

  def move(self,x,y):
    self.path = self.map.getPath(self.path[0], (x,y))
    
  def update(self):
    reached = True
    
    if self.x > 64*self.path[0][0]:
      self.x -= 2
      reached = False
    elif self.x < 64*self.path[0][0]:
      self.x += 2
      reached = False
    
    if self.y > 64*self.path[0][1]:
      self.y -= 2
      reached = False
    elif self.y < 64*self.path[0][1]:
      self.y += 2
      reached = False
      
    if reached:
      if len(self.path)>1:
        self.path.pop(0)
        
class Player(Unit):
  def __init__(self,x,y,id,event,map):
    Unit.__init__(self,x,y,event,map)
    self.id       = id