import pygame
import os
from common import toPixels

class Unit(pygame.sprite.Sprite):
  def __init__(self,x,y,event,map,image):
    pygame.sprite.Sprite.__init__(self)
    self.path     = []
    self.target   = (x,y)
    self.event    = event
    self.map      = map
    self.image    = image
    self.baseImage= self.image
    self.rect     = self.baseImage.get_rect()
    self.speed    = 4
    self.bearing  = 0
    self.turnSpeed= 10
    self.x,self.y = toPixels((x, y))

    self.rect.center = (x+32, y+32)

  def move(self,x,y):
    self.path = self.map.getPath(self.target, (x,y))
    
  def update(self):
    reached = True

    targetPixel = toPixels(self.target)

    if self.rect.centerx > targetPixel[0]:
      if self.bearing == 90:
        self.x -= self.speed
      else:
        self.turnTo(90)
      reached = False
    elif self.rect.centerx < targetPixel[0]:
      if self.bearing == 270:
        self.x += self.speed
      else:
        self.turnTo(270)
      reached = False
    
    if self.rect.centery > targetPixel[1]:
      if self.bearing == 0:
        self.y -= self.speed
      else:
        self.turnTo(0)
      reached = False
    elif self.rect.centery < targetPixel[1]:
      if self.bearing == 180:
        self.y += self.speed
      else:
        self.turnTo(180)
      reached = False
      
    if reached:
      if len(self.path) > 0:
        self.target = self.path.pop(0)
    
    self.image = pygame.transform.rotate(self.baseImage, self.bearing)
    self.rect = self.image.get_rect()
    self.rect.center = (self.x, self.y)

  def turnTo(self, targetBearing):
    if self.bearing < targetBearing:
      if abs(targetBearing - self.bearing) > 180:
        self.bearing -= self.turnSpeed
      else:
        self.bearing += self.turnSpeed
    elif self.bearing > targetBearing:
      if abs(targetBearing - self.bearing) > 180:
        self.bearing += self.turnSpeed
      else:
        self.bearing -= self.turnSpeed

    if self.bearing > 360:
      self.bearing -= 360
    elif self.bearing < 0:
      self.bearing += 360
        
class Player(Unit):
  def __init__(self,x,y,id,event,map):
    self.id = id

    if id == 0:
      image = pygame.image.load(os.path.join("img","player_b.png"))
    elif id == 1:
      image = pygame.image.load(os.path.join("img","player_r.png"))

    Unit.__init__(self,x,y,event,map,image)

    event.register("playerMove",self.moveID)

  def moveID(self,id,x,y):
    if id == self.id:
      self.move(x,y)