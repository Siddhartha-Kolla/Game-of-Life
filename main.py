import numpy as np
import pygame as pygame
import random

# Initializing pygame
pygame.init()

# Number of rows and columns
rows , cols = 100,100

# Creating a numpy array to check whether cell is alive or not
global cell_status_list
# cell_status_list = np.zeros((rows,cols),np.int8)
cell_status_list = []
for i in range(rows):
    cell_status_list.append([random.getrandbits(1) for i in range(cols)])
cell_status_list = np.array(cell_status_list)


# Creating a numpy array for the cell status after checking the neighbors
global future_status_list
future_status_list = np.zeros((rows,cols),np.int8)

# Size of each cell
cell_size = 15

#Border width
b_wid = 2

# Border color
border_color = (134,134,134)

# Dead cell color
cell_d_color = (106, 106, 106)

# Alive cell color
cell_a_color = (255, 255, 0)

cycle_runnig = False

# Configuring screen(setting its size by finding out the space rows and cols need)
screen = pygame.display.set_mode([cols*(cell_size+b_wid),rows*(cell_size+b_wid)])

# Adding a title
pygame.display.set_caption("Conways Game of Life")

# Adding an icon to the screen
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)

# Adding clock
clock = pygame.time.Clock()

# Game Loop
running = True

def check_neighbours():

    for i in range(rows):
        for j in range(cols):
            neib_temp = 0
            for x in range(-1,2):
                if not (x+i < 0 or x+i >= rows):
                    for y in range(-1,2):
                        if not (x == 0 and y == 0):
                            if not (y+j < 0 or y+j >= cols):
                                if cell_status_list[x+i][y+j] == 1:
                                    neib_temp = neib_temp + 1
            if cell_status_list[i][j] == 1:
                future_status_list[i][j] = 1 if neib_temp == 3 or neib_temp == 2 else 0

            elif cell_status_list[i][j] == 0:
                future_status_list[i][j] = 1 if neib_temp == 3 else 0
    
    return future_status_list



while running:

    # Checking events
    for event in pygame.event.get():
        # Quit event
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if cycle_runnig == False:
                    cycle_runnig = True
                elif cycle_runnig == True:
                    cycle_runnig = False



    # Setting background color
    screen.fill(border_color)

    if cycle_runnig:
        cell_status_list = check_neighbours()



    for y in range(rows):
        for x in range(cols):
            pygame.draw.rect(screen,cell_d_color if cell_status_list[y][x] == 0 else cell_a_color,[x*(b_wid+cell_size),y*(b_wid+cell_size),cell_size,cell_size])
    
    # Updating(Flipping) the whole screen
    pygame.display.flip()
    clock.tick(50)
# Exit the program


pygame.quit()