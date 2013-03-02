from tile import *

class Map:
  def __init__(self, w, h):
    self.tiles = [[Tile()]*w]*h
    self.width = w
    self.height = h

