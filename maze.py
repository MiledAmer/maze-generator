from random import choice
from cell import Cell
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

visitedCells =[]

class Maze():
    def __init__(self, width, hight):
        self.grid = []
        self.width = width
        self.hight = hight

        self.createGrid()
        self.generateMaze(self.grid[0][0])

    def createGrid(self):
        for i in range(self.width):
            col = []
            for j in range(self.hight):
                newCell = Cell(i, j)
                col.append(newCell)
                
            self.grid.append(col)
    
    def generateMaze(self, cell: Cell):
        cell.state = True
        visitedCells.append(cell)
        while (len (visitedCells) > 0):
            currentCell = visitedCells.pop()
            unvisitedNeighbors = self.getUnvisitedNeighbors(currentCell)
            if len(unvisitedNeighbors) > 0:
                visitedCells.append(currentCell)
                nextCell = choice(unvisitedNeighbors)
                currentCell.createArc(nextCell)
                nextCell.state = True
                visitedCells.append(nextCell)
            else:
                visitedCells.pop()
        self.setStateZero()
        
    
    def setStateZero(self):
        for i in range(self.width):
            for j in range(self.hight):
                self.grid[i][j].state = False

    
            
    def getNeighbors (self, cell: Cell):
        i = cell.i
        j = cell.j
        neighbors = []
        if i-1 >= 0 :
            neighbors.append(self.grid[i-1][j])

        if i+1 < self.hight:
            neighbors.append(self.grid[i+1][j])

        if j-1 >= 0 :
            neighbors.append(self.grid[i][j-1])

        if j+1 < self.width :
            neighbors.append(self.grid[i][j+1])

        return neighbors
    
    def getSucessors (self, cell: Cell):
        i = cell.i
        j = cell.j
        neighbors = []
        if i-1 >= 0 and cell.walls[0] == False and self.grid[i-1][j].state == False :
            neighbors.append(self.grid[i-1][j])
        
        if j+1 < self.width and cell.walls[1] == False and self.grid[i][j+1].state == False :
            neighbors.append(self.grid[i][j+1])

        if i+1 < self.hight and cell.walls[2] == False and self.grid[i+1][j].state == False:
            neighbors.append(self.grid[i+1][j])

        if j-1 >= 0 and cell.walls[3] == False and self.grid[i][j-1].state == False:
            neighbors.append(self.grid[i][j-1])

        return neighbors

    def getUnvisitedNeighbors (self, cell: Cell):
        i = cell.i
        j = cell.j
        neighbors = []
        if i-1 >= 0 and self.grid[i-1][j].isVisited() == False :
            neighbors.append(self.grid[i-1][j])

        if i+1 < self.hight and self.grid[i+1][j].isVisited() == False:
            neighbors.append(self.grid[i+1][j])

        if j-1 >= 0 and self.grid[i][j-1].isVisited() == False:
            neighbors.append(self.grid[i][j-1])

        if j+1 < self.width and self.grid[i][j+1].isVisited() == False:
            neighbors.append(self.grid[i][j+1])

        return neighbors

    def displayAsDict(self):
        grid= dict()
        for i in range(self.width):
            for j in range(self.hight):
                nieghbors = []
                if  i-1>=0 and self.grid[i][j].isNeighbor(self.grid[i-1][j]):
                    nieghbors.append(((i-1,j,self.grid[i][j].walls[0])))
                if i+1<self.hight and  self.grid[i][j].isNeighbor(self.grid[i+1][j]):
                    nieghbors.append(((i+1,j,self.grid[i][j].walls[2])))
                if j+1<self.hight and self.grid[i][j].isNeighbor(self.grid[i][j+1]):
                    nieghbors.append(((i,j+1,self.grid[i][j].walls[1])))
                if j-1>=0 and self.grid[i][j].isNeighbor(self.grid[i][j-1]):
                    nieghbors.append(((i,j-1,self.grid[i][j].walls[3])))
                grid.update({(i,j): nieghbors})
        
        print(grid)
    
        
    def display(self):
        for i in range(self.width):
            for j in range(self.hight):
                print(self.grid[i][j].getCoordonate())



def main():
    maze = Maze(4, 4)
    maze.displayAsDict()
    maze.display()


if __name__ == "__main__":
    main()



