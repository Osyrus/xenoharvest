from math import floor
mapSize    = (20, 10)
packetSize = 1024


def toPixels((x,y)):
  return((64*x+32,64*y+32))
  
def toGrid((x,y)):
  return (int(floor(x/64)),int(floor(y/64)))

def parse(input):
  ret = []
  data = input.split(";")
  for message in data:
    cmd = message[0]
    params = message[1:].split(',')
    ret.append((cmd,tuple(params)))
  return ret

def package(cmd,params):
  ret = cmd
  for i in params:
    ret += ret(params)+','
  ret = ret[:-1]+';'
  return ret
