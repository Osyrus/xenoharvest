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
    if message != "":
      cmd = message[0]
      params = message[1:].split(',')
      for i in range(len(params)):
        try:
          params[i] = int(params[i])
        except:
          pass
      ret.append((cmd,tuple(params)))
  return ret

def package(cmd,params):
  ret = cmd
  for i in params:
    ret += str(i)+','
  ret = ret[:-1]+';'
  return ret
