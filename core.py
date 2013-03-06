import pygame

def init(mapString):
  mapManager = map.Map(mapString)
  window = pygame.display.set_mode((64*mapSize[0],64*mapSize[1]),pygame.RESIZABLE)
  pygame.display.set_caption("XenoHarvest")
  renderer = render.Renderer(window, eventManager, mapManager, unitGroup, buildingGroup)
  event.register("update", unitGroup.update)
  pather = path.Path(map, unitGroup, buildingGroup)

def checkPygameEvents():
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
      inputs.registerKey(e.key, True)
    elif e.type == KEYUP:
      inputs.registerKey(e.key, False)

def execute(data):
  commands = common.parse(data)
  for cmd,params in commands:
    if cmd == 't':
      print "[Player "+str(params[0]+1)+"] "+params[1]
    elif cmd == 'm':
      if params >= 2:
        event.notify("playerMove",int(params[0]),int(params[1]),int(params[2]))
    elif cmd == 'a':
      units.add(Player(x,y,id,event,pather))
    elif cmd == 'b':
      buildings.add(towerType(x, y, type))