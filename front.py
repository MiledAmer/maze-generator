import pygame
from maze import Maze
from cell import Cell
from pile import piled
from file import filed


#init py games
pygame.init()
FPS = 5
SCREEN_WIDTH = 800
SCREEN_HIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
clock = pygame.time.Clock()
running = True
font = pygame.font.Font(None, 36)  # Choose the font and font size
text_surface = font.render('WINNER', True, (255, 255, 255))
running = True
show_text = False 



# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SELECTED = (219, 15, 204)

# Font
font = pygame.font.Font(None, 36)

# Menu items
menu_items = ["Start DFS", "Start BFS", "Change Maze","Quit"]
selected_item = 0  # Index of the currently selected item

# Function to display menu items
def display_menu():
    screen.fill("black")
    for i, item in enumerate(menu_items):
        color = WHITE if i != selected_item else SELECTED
        text_surface = font.render(item, True, color)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HIGHT/2 + i*50))
        screen.blit(text_surface, text_rect)
# create the maze
maze = Maze(10, 10)
# maze.displayAsDict()

# consts for the front
COLOR = "black"                                                 # screen color
RECT_COLOR = "pink"                                             # cell color
END_POINT_COLOR = "gold"                                        # color of the end point
PLAYER_COLOR = "grey"                                           # player color
START_POINT = 20                                                # starting coordonates for the first cell
RECT_WIDTH = (SCREEN_WIDTH - (START_POINT*2))/maze.width        # width of a cell
END_POINT_COORDENATES = START_POINT+((maze.width-1)*RECT_WIDTH) # coordenates of the end point
rect_x  = START_POINT
rect_y  = START_POINT
i = 0
j = 0

def drawGrid():
    
    x= START_POINT
    y = START_POINT
    RECT_WIDTH = (SCREEN_WIDTH - (START_POINT*2))/maze.width
    for i in range(maze.width):
        for j in range(maze.hight):
            #top line
            if maze.grid[i][j].walls[0]:
                pygame.draw.line(screen, COLOR, (x,y), (x+RECT_WIDTH, y))
            #right line
            if maze.grid[i][j].walls[1]:
                pygame.draw.line(screen, COLOR, (x+RECT_WIDTH, y), (x+RECT_WIDTH, y+RECT_WIDTH))
            #bottom line
            if maze.grid[i][j].walls[2]:
                pygame.draw.line(screen, COLOR, (x, y+RECT_WIDTH), (x+RECT_WIDTH, y+RECT_WIDTH))
            #left line
            if maze.grid[i][j].walls[3]:
                pygame.draw.line(screen, COLOR, (x, y), (x, y+RECT_WIDTH))
            x = x+RECT_WIDTH
        y = y+ RECT_WIDTH
        x = START_POINT


def dfs(startPoint: Cell, endpoint: Cell):
    p = piled()
    p.empiler(startPoint)
    while not p.pile_vide():
        curr = p.depiler()
        curr.state = True
        if curr.i == endpoint.i and curr.j == endpoint.j:
            return True
        else:
            for i in maze.getSucessors(curr):
                mazeSetup()
                playerTrack()

                print("cell : ", i.i, ", ", i.j)
                x = START_POINT + (RECT_WIDTH * i.j)
                y = START_POINT + (RECT_WIDTH * i.i)
                pygame.draw.rect(screen, PLAYER_COLOR, (x+5, y+5, RECT_WIDTH-10, RECT_WIDTH-10))
                pygame.display.flip()  # Update the display
                pygame.time.Clock().tick(FPS)  # Adjust the delay
                p.empiler(i)
    return False

def bfs (startPoint: Cell, endpoint: Cell):
    p = filed()
    p.enfiler(startPoint)
    curr = startPoint
    curr.state = True
    while not p.file_vide():
        curr = p.defiler()
        if curr.i == endpoint.i and curr.j == endpoint.j:
            return True
        else:
            for i in maze.getSucessors(curr):
                mazeSetup()
                playerTrack()
                p.enfiler(i)
                i.state = True
                print("cell : ", i.i, ", ", i.j)
                x = START_POINT + (RECT_WIDTH * i.j)
                y = START_POINT + (RECT_WIDTH * i.i)
                pygame.draw.rect(screen, PLAYER_COLOR, (x+5, y+5, RECT_WIDTH-10, RECT_WIDTH-10))
                pygame.display.flip()  # Update the display
                pygame.time.Clock().tick(FPS)  # Adjust the delay
                
    return False



def mazeSetup():
    screen.fill("purple")
    drawGrid()
    # start point
    pygame.draw.rect(screen, RECT_COLOR, (rect_x+5, rect_y+5, RECT_WIDTH-10, RECT_WIDTH-10))
    # end point
    pygame.draw.rect(screen, END_POINT_COLOR, (END_POINT_COORDENATES+5, END_POINT_COORDENATES+5, RECT_WIDTH-10, RECT_WIDTH-10)) 

def playerTrack():
    for i in range(maze.width):
        for j in range(maze.hight):
            if maze.grid[i][j].state == True:
                x = START_POINT + (RECT_WIDTH * j)
                y = START_POINT + (RECT_WIDTH * i)
                pygame.draw.rect(screen, PLAYER_COLOR, (x+5, y+5, RECT_WIDTH-10, RECT_WIDTH-10))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_item = (selected_item - 1) % len(menu_items)
            elif event.key == pygame.K_DOWN:
                selected_item = (selected_item + 1) % len(menu_items)
            elif event.key == pygame.K_RETURN:
                if selected_item == 0:
                    # DFS
                    maze.setStateZero()
                    mazeSetup()
                    
                    # Run the DFS algorithm once and set the show_text flag if it succeeds
                    resultat = dfs(maze.grid[0][0], maze.grid[9][9])
                    if resultat:
                            show_text = True


                elif selected_item == 1:
                    ## BFS
                    maze.setStateZero()
                    mazeSetup()
                    
                    # Run the DFS algorithm once and set the show_text flag if it succeeds
                    resultat = bfs(maze.grid[0][0], maze.grid[9][9])
                    

                elif selected_item == 2:
                    print("Quit")
                    pygame.quit()
                    running = False
        if event.type == pygame.QUIT:
            running = False

    display_menu()

    pygame.display.flip()
    pygame.time.Clock().tick(FPS)


pygame.quit()