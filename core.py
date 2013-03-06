import pygame
from pygame.locals import *
import server,client,map,event,render,unit,towers,inputs,path,common

class Core:
  def __init__(self):
      self.event     = event.Event()
      self.map       = None
      self.input     = inputs.Inputs(self.event)
      self.units     = pygame.sprite.Group()
      self.buildings = pygame.sprite.Group()
      self.running   = False
      self.pather    = None
      self.ready     = False

  def start(self):
    self.window = pygame.display.set_mode((64*common.mapSize[0],64*common.mapSize[1]),pygame.RESIZABLE)
    pygame.display.set_caption("XenoHarvest")
    self.renderer = render.Renderer(self.window, self.event, self.map, self.units, self.buildings)
    self.event.register("update", self.units.update)
    self.running = True

  def loadMap(self,data):
    if not self.map:
      self.map = map.Map(data)
      self.pather = path.Path(self.map, self.units, self.buildings)
      self.start()

  def sendMap(self):
    if self.ready:
      self.event.notify("transmit","w",*self.map.toString())
      self.start()

  def checkPygameEvents(self):
    for e in pygame.event.get():
      if e.type == QUIT:
        disconnect(socket)
        pygame.quit()
        sys.exit()
      elif e.type == VIDEORESIZE:
        pygame.display.set_mode((e.size),pygame.RESIZABLE)
      elif e.type == MOUSEBUTTONDOWN:
        self.input.registerClick(e.pos, e.button, True)
      elif e.type == MOUSEBUTTONUP:
        self.input.registerClick(e.pos, e.button, False)
      elif e.type == KEYDOWN:
        self.input.registerKey(e.key, True)
      elif e.type == KEYUP:
        self.input.registerKey(e.key, False)

  def execute(self,cmd,*params):
    if cmd == 't':
      print "[Player "+str(params[0]+1)+"] "+params[1]
    elif cmd == 'm':
      self.event.notify("playerMove",*params)
    elif cmd == 'a':
      self.units.add(unit.Player(params[0],params[1],params[2],self.event,self.pather))
    elif cmd == 'b':
      self.buildings.add(towers.towerType(*params[1:]))
    elif cmd == 'w':
      self.loadMap(params)

  def generateMap(self):
    print("MAP GENERATED")
    self.map    = map.Map(*common.mapSize)
    self.pather = path.Path(self.map, self.units, self.buildings)
    self.ready  = True