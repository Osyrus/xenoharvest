import pygame,sys
import server,client,map,event,render,unit,inputs,path,core,common
from pygame.locals import *

#Initialise game objects
eventManager  = event.Event()
inputManager  = inputs.Inputs(event)
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
  interface  = server.Server(port,event, mapManager)

eventManager.register("transmit", interface.transmit)
eventManager.register("cmdRecv",  core.execute)

##DEBUG
def test(s):
  print s
 
eventManager.register("cmdRecv", test)
##END


running = True

while running:
  core.checkPygameEvents()
  eventManager.notify("update")
  eventManager.update()
  if window:
    pygame.display.update()
  clock.tick(30)