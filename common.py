def toPixels((x,y)):
  return((64*x+32,64*y+32))
  
def toGrid((x,y)):
  return (floor(x/64),floor(y/64))