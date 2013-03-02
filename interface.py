class Interface:
  def __init__(self,socket,event):
    self.socket = socket
    self.event  = event
    event.register("moveOrder",self.moveOrder)
    
  def moveOrder(self,x,y):
    self.socket.send("m"+str(x)+","+str(y))