import pygame, os
from pygame.locals import *

tileSet = pygame.image.load(os.path.join("img","tiles.png"))

class Renderer:
  def __init__(self,window,event,map):
    self.window = window
    self.event  = event
    self.map    = map
    event.register("update", self.update)
    
  def update(self):
    self.window.fill(pygame.Color(0,0,0))
    
    for x in map.width:
      for y in map.height:
        tile = map.getTile(x,y)
        if tile < 10:
          rect = pygame.Rect(64*tile, 0, 64, 64)
          self.window.blit(tileSet, x*64, y*64, rect)