from client import connect,disconnect
from server    import *
import pygame,sys
from pygame.locals import *
from map       import *
from event     import *
from render    import *
from unit      import *
from interface import *

socket = False

#Initialise events
event = Event();

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
pygame.init()
window = pygame.display.set_mode((1024,600),pygame.RESIZABLE)
pygame.display.set_caption("XenoHarvest")
clock  = pygame.time.Clock()

#Set up game
interface = Interface(socket,event)
map       = Map(10,10)
units     = []
render    = Renderer(window, event, map, units)
units.append(Player(0,0,0,event,map))
event.register("moveOrder", units[0].move)

#Start running
running = True

def test(s):
  print s
 
event.register("cmdRecv", test)

#Main loop
while running:
  for e in pygame.event.get():
    if e.type == QUIT:
			pygame.quit()
			disconnect(socket)
			sys.exit()
    elif e.type == VIDEORESIZE:
			pygame.display.set_mode((e.size),pygame.RESIZABLE)
    elif e.type == MOUSEBUTTONDOWN:
      render.registerClick(e.pos, e.button, True)
    elif e.type == MOUSEBUTTONUP:
      render.registerClick(e.pos, e.button, False)
	
  pygame.display.update()
  event.update()
  event.notify("update")
  clock.tick(30)