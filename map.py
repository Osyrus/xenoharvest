import random
import path

class Map:
  def __init__(self, a, b = None):
  
    self.tiles = []
    self.tileMap = ['0','1','2','3','4','5','6','7','8','9']
    if b == None:
      # Single string to load from has been passed
      (self.width,self.height) = self.load(a)
    else:
      # Ints for w and h have been passed
      self.width = a
      self.height = b
      
      self.numTiles = 10
      self.tileWeighting = [50, 50, 50, 50, 50, 2, 1, 5, 4, 1]
      self.passable = [True, True, True, True, True, False, False, False, False, False]
      self._normWeight(self.tileWeighting)

      self.fill()

    self.pather = path.Path(self)

  def fill(self):
    for y in range(self.height):
      temp = []

      for x in range(self.width):
        temp.append(self._chooseTile())

      self.tiles.append(temp)
      
  def load(self, str):
    rows = str.split(",")
    for row in rows:
      temp = []
      for char in row:
        temp.append(tileMap.index(char))
      self.tiles.append(temp)
        
    return(len(temp), len(self.tiles))

  def getTile(self, x, y):
    return self.tiles[y][x]

  def getWidth(self):
    return self.width

  def getHeight(self):
    return self.height

  def isPassable(self, x, y):
    return self.passable[self.tiles[y][x]]

  def _chooseTile(self):
    random.seed()
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
      
  def getPath(self, start, end):
    if self.isPassable(int(end[0]), int(end[1])):
      candidatePath = self.pather.calcPath(start, end)
      if len(candidatePath) > 0:
        if end == candidatePath[-1]:
          return candidatePath

    return [start]
    
  def toString(self):
    str = ""
    for y in range(self.height):
      for x in range(self.width):
        str += self.tileMap[self.getTile(x,y)]
      str += ","
    return str[:-1]
    