
class Tower:
  def __init__(self, x, y):
    self.pos = x, y
    self.type = 0

  def getPos(self):
    return pos

  def getType(self):
    return self.type

class LaserTower(Tower):
  def __init__(self, x, y):
    super(LaserTower, self).__init__(x, y)
    self.type = 1