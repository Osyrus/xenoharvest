<<<<<<< HEAD
from client import connect
import pygame,sys
from pygame.locals import *
from map,tile import *

#Connect to server
ip     = "127.0.0.1" 
#raw_input("Server ip: ")
port   = 8888
#input("Server port: ")
socket = connect(ip,port)

#Set up pygame window
pygame.init()
window = pygame.display.set_mode((1024,600),pygame.RESIZABLE)
pygame.display.set_caption("XenoHarvest")
clock  = pygame.time.Clock()

#Create world
map = Map(10,10)

#Start running
running = True

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
			pygame.draw.rect(window,pygame.Color(255,255,255),(32*x,32*y,32,32),1);
	
	pygame.display.update()
	clock.tick(30)
=======
import socket   #for sockets
import sys  #for exit
#import pygame
from objects import *
from thread  import *

players = []
self_id = -1
byteRec = 1024

def parse(data):
  global self_id

  cmd = data[0]
  msg = data[1:]

  if cmd == 'c':
    self_id = int(msg)
  elif cmd == 't':
    params = msg.split(',',1)
    id = int(params[0])
    if id != self_id:
      print "[Player "+str(id+1)+"] "+params[1]

def serverlisten(socket):
  
  while True:
    data = socket.recv(byteRec)
    if not data:
      break
    cmds = data.split(';')
    for i in cmds:
      if i:
        parse(i)

ip   = raw_input("Server ip: ");
port = input("Server port: ");
try:
  #create an AF_INET, STREAM socket (TCP)
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
  print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
  sys.exit()

print 'Socket Created'
s.connect((ip,port))
start_new_thread(serverlisten ,(s,))
while 1:
  msg = raw_input()
  msg.replace(';','')
  s.send("t"+msg)

s.close()
>>>>>>> f281856df02f5c837516a9c32c8f65779df65959
