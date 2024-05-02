from random import choice

TOP = 0
RIGHT = 1
BOTTOM = 2
LEFT = 3

class Cell ():
    def __init__(self, i, j):

        # these are the cooordenates of the cell in the grid
        self.i = i
        self.j = j

        # if the cell is visited the state become true else it is False by default
        self.state = False 

        # the walls are by default true for every cell
        # the arrangement of the walls is TOP, RIGHT, BOTTOM, LEFT
        self.walls = [True, True, True, True]

    def createArc(self, nextCell):
        if (self.i == nextCell.i):
            if(self.j + 1 ==  nextCell.j):
                self.walls[RIGHT] = False
                nextCell.walls[LEFT] = False
            elif (self.j - 1 ==  nextCell.j) : 
                self.walls[LEFT] = False
                nextCell.walls[RIGHT] = False
            else:
                raise IndexError("cell ({},{}) and cell ({},{}) are not neighbors".format(self.i, self.j, nextCell.i, nextCell.j))
        elif (self.j == nextCell.j):
            if (self.i + 1 == nextCell.i):
                self.walls[BOTTOM] = False
                nextCell.walls[TOP] = False
            elif (self.i - 1 == nextCell.i):
                self.walls[TOP] = False
                nextCell.walls[BOTTOM] = False
            else:
                raise IndexError("cell ({},{}) and cell ({},{}) are not neighbors".format(self.i, self.j, nextCell.i, nextCell.j))
        else:
            raise IndexError("cell ({},{}) and cell ({},{}) are not neighbors".format(self.i, self.j, nextCell.i, nextCell.j))

    
    def isVisited (self):
        return self.state

    def getCoordonate(self):
        return (self.i, self.j)
    
    def isNeighbor(self, cell):
        if cell.i == self.i+1 and cell.j == self.j or cell.i == self.i-1 and cell.j == self.j :
            return True
        elif cell.j == self.j+1 and cell.i == self.i or cell.j == self.j-1 and cell.i == self.i :
            return True
        else:
            return False



    
