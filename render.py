import pygame, os
from pygame.locals import *
from math import floor

tileSet = pygame.image.load(os.path.join("img","tiles.png"))

class Renderer:
  def __init__(self,window,event,map,units):
    self.window = window
    self.event  = event
    self.map    = map
    self.map_w  = map.getWidth()
    self.map_h  = map.getHeight()
    self.units  = units
    event.register("update", self.update)
    
  def update(self):
    self.window.fill(pygame.Color(0,0,0))
    
    for x in range(self.map_w):
      for y in range(self.map_h):
        tile = self.map.getTile(x,y)
        if tile < 10:
          rect = pygame.Rect(64*tile, 0, 64, 64)
          self.window.blit(tileSet, (x*64, y*64), rect)
        
    self.units.draw(self.window)
    # for i in self.units:
    #   pygame.draw.circle(self.window,pygame.Color(0,255,0),(i.x+32,i.y+32),16)
      
      
  def registerClick(self, pos, button, down):
    x = floor(pos[0]/64)
    y = floor(pos[1]/64)
    
    if down and button == 3:
      self.event.notify("moveOrder", x,y)