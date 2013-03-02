from client import connect
import pygame,sys
from pygame.locals import *
from map import *
from tile import *
from event import *

socket = False

#Initialise events
event = Event();

while not socket:
  
  #Connect to server
  ip     = "127.0.0.1" 
  #raw_input("Server ip: ")
  port   = 8888
  #input("Server port: ")
  socket = connect(ip,port,event)
  if not socket:
    print "Error: server connection failed"

#Set up pygame window
pygame.init()
window = pygame.display.set_mode((1024,600),pygame.RESIZABLE)
pygame.display.set_caption("XenoHarvest")
clock  = pygame.time.Clock()

#Set up game
map   = Map(10,10)

#Start running
running = True

def test(s):
  print s
 
event.register("cmd_recv", test)

#Main loop
while running:
  for e in pygame.event.get():
		if e.type == QUIT:
			pygame.quit()
			disconnect(socket)
			sys.exit()
		elif e.type == VIDEORESIZE:
			pygame.display.set_mode((e.size),pygame.RESIZABLE) 
	
  window.fill(pygame.Color(0,0,0));
  for x in range(map.width):
    for y in range(map.height):
			pygame.draw.rect(window,pygame.Color(255,255,255),(32*x,32*y,32,32),1)
	
  pygame.display.update()
  event.update()
  clock.tick(30)