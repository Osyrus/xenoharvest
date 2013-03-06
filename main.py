import pygame,sys
import server,client,map,event,render,unit,towers,inputs,path,common
from pygame.locals import *

def init():
  window = pygame.display.set_mode((64*common.mapSize[0],64*common.mapSize[1]),pygame.RESIZABLE)
  pygame.display.set_caption("XenoHarvest")
  renderer = render.Renderer(window, eventManager, mapManager, unitGroup, buildingGroup)
  eventManager.register("update", unitGroup.update)

def loadMap(data):
  mapManager = map.Map(mapString)
  pather = path.Path(mapManager, unitGroup, buildingGroup)
  init()

def checkPygameEvents():
  for e in pygame.event.get():
    if e.type == QUIT:
      disconnect(socket)
      pygame.quit()
      sys.exit()
    elif e.type == VIDEORESIZE:
      pygame.display.set_mode((e.size),pygame.RESIZABLE)
    elif e.type == MOUSEBUTTONDOWN:
      inputManager.registerClick(e.pos, e.button, True)
    elif e.type == MOUSEBUTTONUP:
      inputManager.registerClick(e.pos, e.button, False)
    elif e.type == KEYDOWN:
      inputManager.registerKey(e.key, True)
    elif e.type == KEYUP:
      inputManager.registerKey(e.key, False)

def execute(cmd,*params):
  if cmd == 't':
    print "[Player "+str(params[0]+1)+"] "+params[1]
  elif cmd == 'm':
    if params >= 2:
      eventManager.notify("playerMove",int(params[0]),int(params[1]),int(params[2]))
  elif cmd == 'a':
    unitGroup.add(unit.Player(x,y,id,eventManager,pather))
  elif cmd == 'b':
    buildingGroup.add(towers.towerType(*params[1:]))

#Initialise game objects
eventManager  = event.Event()
inputManager  = inputs.Inputs(eventManager)
unitGroup     = pygame.sprite.Group()
buildingGroup = pygame.sprite.Group()
mapManager    = None                   # Map to be loaded from server
window        = None                   # Initialised once players connected
pather        = None

#Initialise pygame
pygame.init()
clock  = pygame.time.Clock()

#Connect to server
ip     = raw_input("Server ip (leave blank to host): ")
port   = input("Server port: ")
if( ip != "" ):
  interface  = client.Client(ip,port,event)
else:
  mapManager = map.Map(*common.mapSize)
  interface  = server.Server(port,eventManager, mapManager)
  pather = path.Path(mapManager, unitGroup, buildingGroup)
  unitGroup.add(unit.Player(0,0,0,eventManager, pather))
  init()

eventManager.register("transmit", interface.transmit)
eventManager.register("cmdRecv",  execute)

##DEBUG
def test(cmd,*params):
  print(cmd+" "+str(params))
 
eventManager.register("cmdRecv", test)
##END


running = True

while running:
  checkPygameEvents()
  eventManager.notify("update")
  eventManager.update()
  pygame.display.update()
  clock.tick(30)