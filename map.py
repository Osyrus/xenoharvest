from tile import *
import random

class Map:
  def __init__(self, w, h):
    self.tiles = [[0]*w]*h
    self.width = w
    self.height = h

    self.numTiles = 10
    self.tileWeighting = [50, 50, 50, 50, 50, 1, 1, 5, 4, 1]
    self._normWeight(self.tileWeighting)

    self.fill()

  def fill(self):
    for y in range(self.height):
      for x in range(self.width):
        self.tiles[y][x] = self._chooseTile()

  def getTile(self, x, y):
    return self.tiles[y][x]

  def getWidth(self):
    return self.width

  def getHeight(self):
    return self.height

  def _chooseTile(self):
    rand = random.random()

    for i in range(len(self.tileWeighting)):
      if rand < self.tileWeighting[i]:
        return i
      else:
        rand -= self.tileWeighting[i]

    return 0

  def _normWeight(self,array):
    total = sum(array)*1.0

    for x in range(0, self.numTiles):
      array[x] = array[x]/total