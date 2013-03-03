from client import connect,disconnect
from server    import *
import pygame,sys,inputs
from pygame.locals import *
from map       import *
from event     import *
from render    import *
from unit      import *
from interface import *

socket = False

#Initialise events and inputs
event = Event();
inputs = inputs.Inputs(event)

#Connect to server
ip     = raw_input("Server ip (leave blank to host): ")
port   = input("Server port: ")
if( ip != "" ):
  socket = connect(ip,port,event)
  if not socket:
    print "Error: server connection failed"
    sys.exit()
else:
  server = Server(port,event)
  socket = connect("127.0.0.1",port,event)

#Set up pygame window
mapSize = (20, 10)
pygame.init()
window = pygame.display.set_mode((64*mapSize[0],64*mapSize[1]),pygame.RESIZABLE)
pygame.display.set_caption("XenoHarvest")
clock  = pygame.time.Clock()

#Set up game
map       = Map(mapSize[0], mapSize[1])
units     = pygame.sprite.Group()
buildings = pygame.sprite.Group() ##Testing
interface = Interface(socket,event,map,units, buildings)
render    = Renderer(window, event, map, units, buildings)
event.register("update", units.update)

#Start running
running = True

def test(s):
  print s
 
event.register("cmdRecv", test)

#Main loop
while running:
  for e in pygame.event.get():
    if e.type == QUIT:
      disconnect(socket)
      pygame.quit()
      sys.exit()
    elif e.type == VIDEORESIZE:
      pygame.display.set_mode((e.size),pygame.RESIZABLE)
    elif e.type == MOUSEBUTTONDOWN:
      inputs.registerClick(e.pos, e.button, True)
    elif e.type == MOUSEBUTTONUP:
      inputs.registerClick(e.pos, e.button, False)
    elif e.type == KEYDOWN:
      imputs.registerKey(e.key, True)
  
  pygame.display.update()
  event.update()
  event.notify("update")
  clock.tick(30)