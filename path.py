
class Path:
  def __init__(self, map):
    self.graph = []
    self.height = map.getHeight()
    self.width = map.getWidth()

    for y in range(self.height):
      temp = []
      for x in range(self.width):
        temp.append(True);
      self.graph.append(temp)

    self.calcGraph()

  def calcGraph(self):
    for y in range(self.height):
      for x in range(self.width):
        self.graph = map.isPassable(x, y)
  
  def calcPath(self, start, end):
    #Create empty list of possible squares to check out
    possibles = []
    #The closed list is for already checked squares
    closed = []

    #Add the starting point to the possibles list
    possibles.append(Node(start, 0, 0))

    #Find the possible places to go
    #Define a list in which to iterate over to check the adjacent squares
    sList = ((-1, 0), (1, 0), (0, -1), (0, 1))
    #The main loop, iterate until done
    while parent = possibles.pop():
      #The parent is the square by which the checks are based around
      #The parent is chosen from the end as that should be the Node with the lowest F score
      if parent.getPos() == end:
        closed.append(parent)
        break

      parentX, parentY = parent.getPos()

      #Check all of the adjacent points using the previously defined list
      for i in range(4):
        #Create a candidate to possibly add to the list of possibles
        candidate = Node(parentX + sList[i][0], parentY + sList[i][1], parent, end)

        #Check to see if the graph shows that the location is passable
        if self.graph[candidate.getY()][candidate.getX()] and candidate not in closed:
          #Thanks to python, pretty much what it says
          if candidate not in possibles:
            #If it's not there, add it
            possibles.append(candidate)
          else:
            #If it is in there, is it more efficient to come from this new direction or not?
            for i in range(len(possibles)):
              if possibles[i] == candidate:
                if possibles[i].getG() > candidate.getG():
                  #If it is a lower cost to get there from the current parent Node, change the
                  #parent to be the current one instead. If not, do nothing
                  possibles[i].setParent(candidate.parent)

      #Put the now dealt with parent test Node into the closed list
      closed.append(parent)
      #Sort the possibles list from highest to lowest, so the next popped should have the lowest F
      possibles.sort(compareNodes)

    #Now to trace the completed path back to the start
    done = False
    path = []
    #Fetch the last added Node to the closed list (the end Node)
    traceNode = closed.pop()
    #Loop until the start square is found
    while not done:
      #Check is the start square has been found,
      #(don't append it as we don't need to move to where we already are)
      if traceNode.getPos() == start:
        done = True
      else:
        #Append the position of the Node to the path list
        path.append(traceNode.getPos())
        #Change our trace Node to the next Node in line
        traceNode = traceNode.getParent()

    #The path currently starts at the end and ends at the start, needs to be reversed
    path.reverse()
    #Finally we can return the completed path
    return path

class Node:
  def __init__(self, pos, parent, end):
    self.pos = pos
    self.parent = parent
    self.g = parent.getG() + 1
    self.h = abs(pos[0] - end[0]) + abs(pos[1] - end[1])

  def __eq__(self, other):
    return self.pos == other.pos

  def getPos(self):
    return self.pos

  def getX(self):
    return self.pos[0]

  def getY(self):
    return self.pos[1]

  def getF(self):
    return self.g + self.h

  def getG(self):
    return self.g

  def setParent(self, parent):
    self.parent = parent
    self.g = parent.getG() + 1

  def getParent(self):
    return self.parent

def compareNodes(x, y):
  if x.getF() > y.getF():
    return 1
  elif x.getF() == y.getF():
    return 0
  elif x.getF() < y.getF():
    return -1