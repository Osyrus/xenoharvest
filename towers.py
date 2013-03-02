
class Tower:
  def __init__(self, x, y):
    self.pos = x, y
    self.type = 0
    self.radius = 0

  def getPos(self):
    return self.pos

  def getType(self):
    return self.type

class LaserTower(Tower):
  def __init__(self, x, y):
    super(LaserTower, self).__init__(x, y)
    self.type = 1

class FlameTower(Tower):
  def __init__(self, x, y):
    super(FlameTower, self).__init__(x, y)
    self.type = 2

class CannonTower(Tower):
  def __init__(self, x, y):
    super(CannonTower, self).__init__(x, y)
    self.type = 3

class RocketTower(Tower):
  def __init__(self, x, y):
    super(RocketTower, self).__init__(x, y)
    self.type = 4

class SlowTower(Tower):
  def __init__(self, x, y):
    super(SlowTower, self).__init__(x, y)
    self.type = 5

class LureTower(Tower):
  def __init__(self, x, y):
    super(LureTower, self).__init__(x, y)
    self.type = 6