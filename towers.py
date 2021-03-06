import pygame, os
from common import toPixels

towerSet = pygame.image.load(os.path.join("img","tower_sheet.png"))

def towerType(x, y, type):
  if type == 1:
    return LaserTower(x, y)
  elif type == 2:
    return FlameTower(x, y)
  elif type == 3:
    return CannonTower(x, y)
  elif type == 4:
    return RocketTower(x, y)
  elif type == 5:
    return SlowTower(x, y)
  elif type == 6:
    return LureTower(x, y)
  else:
    return None

class Tower(pygame.sprite.Sprite):
  def __init__(self, x, y, type):
    pygame.sprite.Sprite.__init__(self)
    self.pos = x, y
    self.type = type
    self.level = 1
    self.radius = 0
    self.image = pygame.Surface((64, 64))
    self.rect = self.image.get_rect()
    self.solid = False

    self.updateImage()

  def getPos(self):
    return self.pos

  def getX(self):
    return self.pos[0]

  def getY(self):
    return self.pos[1]

  def getType(self):
    return self.type

  def update(self):
    pass

  def isPassable(self):
    return self.solid

  def updateImage(self):
    if self.type > 0 and self.level > 0:
      self.image.blit(towerSet, self.image.get_rect(), pygame.Rect((self.type-1)*64, (self.level-1)*64, 64, 64))
      self.rect = self.image.get_rect()
      self.rect.center = toPixels(self.pos)

class LaserTower(Tower):
  def __init__(self, x, y):
    Tower.__init__(self, x, y, 1)

class FlameTower(Tower):
  def __init__(self, x, y):
    Tower.__init__(self, x, y, 2)

class CannonTower(Tower):
  def __init__(self, x, y):
    Tower.__init__(self, x, y, 3)

class RocketTower(Tower):
  def __init__(self, x, y):
    Tower.__init__(self, x, y, 4)

class SlowTower(Tower):
  def __init__(self, x, y):
    Tower.__init__(self, x, y, 5)

class LureTower(Tower):
  def __init__(self, x, y):
    Tower.__init__(self, x, y, 6)