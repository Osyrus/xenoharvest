import random
import path

class Map:
  def __init__(self, a, b=None):
  
    self.tiles  = []
    self.tileMap = ['0','1','2','3','4','5','6','7','8','9']
    self.numTiles = 10
    self.tileWeighting = [50, 50, 50, 50, 50, 2, 1, 5, 4, 1]
    self.passable = [True, True, True, True, True, False, False, False, False, False]

    if b == None:
      # Single string to load from has been passed
      (self.width,self.height) = self.load(a)
    else:
      # Ints for w and h have been passed
      self.width = a
      self.height = b
      
      self._normWeight(self.tileWeighting)

      self.fill()

  def fill(self):
    for y in range(self.height):
      temp = []

      for x in range(self.width):
        temp.append(self._chooseTile())

      self.tiles.append(temp)
      
  def load(self, rows):
    for row in rows:
      if row != "":
        temp = []
        for char in row[1:]:
          temp.append(self.tileMap.index(char))
        self.tiles.append(temp)

    return (len(self.tiles[0]),len(self.tiles))

  def toString(self):
    ret = ()
    for y in range(self.height):
      temp = "r"
      for x in range(self.width):
        print(str(x)+","+str(y))
        temp += self.tileMap[self.getTile(x,y)]
      ret += (temp,)
    return ret

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
