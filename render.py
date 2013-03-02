import pygame, os
from pygame.locals import *

tileSet = pygame.image.load(os.path.join("img","tiles.png"))

class Renderer:
  def __init__(self,window,event,map):
    self.window = window
    self.event  = event
    self.map    = map
    self.map_w  = map.getWidth()
    self.map_h  = map.getHeight()
    event.register("update", self.update)
    
  def update(self):
    self.window.fill(pygame.Color(0,0,0))
    
    for x in map_w:
      for y in map_h:
        tile = map.getTile(x,y)
        if tile < 10:
          rect = pygame.Rect(64*tile, 0, 64, 64)
          self.window.blit(tileSet, x*64, y*64, rect)