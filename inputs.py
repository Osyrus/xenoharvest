from common import toGrid

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
    pass