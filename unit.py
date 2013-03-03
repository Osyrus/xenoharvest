import pygame
import os

class Unit(pygame.sprite.Sprite):
  def __init__(self,x,y,event,map):
    pygame.sprite.Sprite.__init__(self)
    self.path     = []
    self.target   = (x,y)
    self.event    = event
    self.map      = map
    self.image    = None
    self.rect     = pygame.Rect(0, 0, 64, 64)
    self.speed    = 4
    self.bearing  = 0
    self.turnSpeed= 5

    self.rect.topleft = (x, y)

  def move(self,x,y):
    self.path = self.map.getPath(self.target, (x,y))
    
  def update(self):
    reached = True

    if self.rect.left > 64*self.target[0]:
      if self.bearing == 90:
        self.rect.move_ip(-self.speed, 0)
      else:
        self.turnTo(90)
      reached = False
    elif self.rect.left < 64*self.target[0]:
      if self.bearing == 270:
        self.rect.move_ip(self.speed, 0)
      else:
        self.turnTo(270)
      reached = False
    
    if self.rect.top > 64*self.target[1]:
      if self.bearing == 0:
        self.rect.move_ip(0, -self.speed)
      else:
        self.turnTo(0)
      reached = False
    elif self.rect.top < 64*self.target[1]:
      if self.bearing == 180:
        self.rect.move_ip(0, self.speed)
      else:
        self.turnTo(180)
      reached = False
      
    if reached:
      if len(self.path) > 0:
        target = self.path.pop(0)

    def turnTo(self, targetBearing):
      if self.bearing < targetBearing:
        self.bearing += self.turnSpeed
      elif self.bearing > targetBearing:
        self.bearing -= self.turnSpeed
        
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