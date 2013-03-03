from common import toGrid
from pygame.locals import *

class Inputs:
  def __init__(self, event):
    self.event = event
    self.currentTower = 1

  def registerClick(self, pos, button, down):
    x,y = toGrid(pos)
    if down and button == 3:
      self.event.notify("moveOrder", x,y)
    elif down and button == 1:
      self.event.notify("buildOrder",self.currentTower,x,y)

  def registerKey(self, key, down):
    if down:
      if key == K_1:
        self.currentTower = 1
      elif key == K_2:
        self.currentTower = 2
      elif key == K_3:
        self.currentTower = 3
      elif key == K_4:
        self.currentTower = 4  
      elif key == K_5:
        self.currentTower = 5
      elif key == K_6:
        self.currentTower = 6