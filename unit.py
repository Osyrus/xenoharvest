import pygame
import os

class Unit(pygame.sprite.Sprite):
  def __init__(self,x,y,event,map):
    pygame.sprite.Sprite.__init__(self)
    self.path     = [(x,y)]
    self.event    = event
    self.map      = map
    self.image    = None
    self.rect     = pygame.Rect(0, 0, 64, 64)
    self.speed    = 4
    self.bearing  = 0
    self.turnSpeed= 4

    self.rect.topleft = (x, y)
    event.register("update",self.update)

  def move(self,x,y):
    self.path = self.map.getPath(self.path[0], (x,y))
    
  def update(self):
    reached = True

    if self.rect.left > 64*self.path[0][0]:
      self.rect.move_ip(-self.speed, 0)
      reached = False
    elif self.rect.left < 64*self.path[0][0]:
      self.rect.move_ip(self.speed, 0)
      reached = False
    
    if self.rect.top > 64*self.path[0][1]:
      self.rect.move_ip(0, -self.speed)
      reached = False
    elif self.rect.top < 64*self.path[0][1]:
      self.rect.move_ip(0, self.speed)
      reached = False
      
    if reached:
      if len(self.path) > 1:
        self.path.pop(0)
        
class Player(Unit):
  def __init__(self,x,y,id,event,map):
    Unit.__init__(self,x,y,event,map)

    self.id = id

    if id == 0:
      self.image = pygame.image.load(os.path.join("img","player_b.png"))
    elif id == 1:
      self.image = pygame.image.load(os.path.join("img","player_r.png"))

    event.register("playerMove",self.moveID)

  def moveID(self,id,x,y):
    if id == self.id:
      self.move(x,y)