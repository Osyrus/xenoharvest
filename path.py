#A path-finding system based on the Manhattan A* algorithm.
#The map object that is passed into the constructor needs a method isPassable(x, y) that gives
#a boolean as to if the location (x, y) is passable (True) or impassable (False). There also
#needs to be two methods, getWidth() and getHeight(), that return the width and height of the
#map respectively. Once the object is made, to get the path simply call calcPath(start, end) on
#the Path object (where start and end are tuples representing the start and end locations) to
#receive a list containing tuples in the form (x, y) that represent locations along the path.

class Path:
  #At this point it needs to be passed the map object containing the indices of each tile,
  #but will likely later need to know building positions as well.
  def __init__(self, map):
    #Pull the width and height of the map object and associate the values to itself
    self.map = map
    self.height, self.width = self.map.getHeight(), self.map.getWidth()

    #Preallocate a 2D boolean matrix
    self.graph = []
    for y in range(self.height):
      temp = []
      for x in range(self.width):
        temp.append(True);
      self.graph.append(temp)

    #Fill it with the correct passable / impassable values
    self.calcGraph()

  #Turns the map into a 2D matrix of boolean values (True is passable, False is not)
  def calcGraph(self):
    for y in range(self.height):
      for x in range(self.width):
        self.graph[y][x] = self.map.isPassable(x, y)
  
  #The method where all the magic happens (or doesn't...)
  #Start and end are tuples in the form (x, y)
  def calcPath(self, start, end):
    #Make sure the desired location isn't just the start location
    if start == end:
      return []

    #Create empty list of possible squares to check out
    possibles = []
    #The closed list is for already checked squares
    closed = []

    #Add the starting point to the possibles list
    possibles.append(Node(start, None, end))

    #Find the possible places to go
    #Define a list in which to iterate over to check the adjacent squares
    sList = ((-1, 0), (1, 0), (0, -1), (0, 1))
    #The main loop, iterate until done
    while len(possibles) > 0:
      parent = possibles.pop()
      #The parent is the square by which the checks are based around
      #The parent is chosen from the end as that should be the Node with the lowest F score
      if parent.getPos() == end:
        closed.append(parent)
        break

      parentX, parentY = parent.getPos()

      #Check all of the adjacent points using the previously defined list
      for i in range(4):
        #Create a candidate to possibly add to the list of possibles
        candidate = Node((parentX + sList[i][0], parentY + sList[i][1]), parent, end)

        #Check to see if the graph shows that the location is passable
        if candidate.getY() < self.height and candidate.getY() >= 0 and candidate.getX() < self.width and candidate.getX() >= 0:
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

#The Node object, allows for each coordinate to contain more information that just it's position
class Node:
  #Initialise the object with some stuff
  def __init__(self, pos, parent, end):
    self.pos = pos #It's position in the grid
    self.parent = parent #What it's parent Node is

    if parent != None:
      self.g = parent.getG() + 1 #Update the cost to get here
    else:
      self.g = 0

    self.h = abs(pos[0] - end[0]) + abs(pos[1] - end[1]) #Update the cost to get to the end

  #Overriding the equivalence operator to allow for Nodes to be equated based on their locations
  def __eq__(self, other):
    return self.pos == other.pos

  #Getters
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

  def getParent(self):
    return self.parent

  #Setter for the parent, also updates the new cost to get to the Node from the parent
  def setParent(self, parent):
    self.parent = parent
    self.g = parent.getG() + 1

#Function used to define how the list of possible Node should be sorted
#In this case, we want to sort it in terms of the total cost F (G + H)
def compareNodes(x, y):
  if x.getF() > y.getF():
    return -1
  elif x.getF() == y.getF():
    return 0
  elif x.getF() < y.getF():
    return 1