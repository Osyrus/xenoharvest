import pygame,sys
import server,client,map,event,render,unit,towers,inputs,path,core,common
from pygame.locals import *


#Initialise game objects
game = core.Core()

#Initialise pygame
pygame.init()
clock   = pygame.time.Clock()
running = False

#Connect to server
ip     = raw_input("Server ip (leave blank to host): ")
#Get the port (don't accept a blank input)
port = ""
while port == "":
  port = raw_input("Server port: ")
#Start up client or server
if( ip != "" ):
  interface  = client.Client(ip,port,game.event)
else:
  interface  = server.Server(port,game.event)
  game.generateMap()
  game.event.register("sendMap", game.sendMap)
  print("Waiting for player 2...")

game.event.register("transmit", interface.transmit)
game.event.register("cmdRecv",  game.execute)

##DEBUG
def test(cmd,*params):
  print(cmd+" "+str(params))
 
game.event.register("cmdRecv", test)
##END

while True:
  game.checkPygameEvents()
  game.event.notify("update")
  game.event.update()
  if game.running:
    pygame.display.update()
  clock.tick(30)