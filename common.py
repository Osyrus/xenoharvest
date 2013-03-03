from math import floor

def toPixels((x,y)):
  return((64*x+32,64*y+32))
  
def toGrid((x,y)):
  return (int(floor(x/64)),int(floor(y/64)))