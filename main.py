import numpy as np
import pygame as pygame
import random

# Initializing pygame
pygame.init()

# Number of rows and columns
rows , cols = 10,10

# Creating a numpy array to check whether cell is alive or not
cell_status_list = np.zeros((rows,cols),np.int8)
# cell_status_list = [[random.getrandbits(1) for i in range(10)],[random.getrandbits(1) for i in range(10)],[random.getrandbits(1) for i in range(10)],[random.getrandbits(1) for i in range(10)],[random.getrandbits(1) for i in range(10)],[random.getrandbits(1) for i in range(10)],[random.getrandbits(1) for i in range(10)],[random.getrandbits(1) for i in range(10)],[random.getrandbits(1) for i in range(10)],[random.getrandbits(1) for i in range(10)]]

# Creating a numpy array for the cell status after checking the neighbors
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

# Adding a logo
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)

# Game Loop
running = True

def check_neighbours():
    for i in range(rows):
        for j in range(cols):
            neib_temp = 0
            for x in range(-1,2):
                for y in range(-1,2):
                    if x != 0 and y != 0:
                        if not (x+i < 0 or y+j < 0 or x+i >= rows or y+j >= cols):
                            if cell_status_list[j+y][x+i] == 1:
                                neib_temp = neib_temp + 1
            print(neib_temp)
            future_status_list[i][j] = neib_temp
while running:

    # Checking events
    for event in pygame.event.get():
        # Quit event
        if event.type == pygame.QUIT:
            running = False
        # Mouse click event
        if event.type == pygame.MOUSEBUTTONDOWN:
            MouseX , MouseY = event.pos
            status_temp = cell_status_list[MouseY//(cell_size+b_wid) , MouseX//(cell_size+b_wid)]
            cell_status_list[MouseY//(cell_size+b_wid) , MouseX//(cell_size+b_wid)] = 1 if status_temp == 0 else 0

        # Spacebar click event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cycle_runnig = True if cycle_runnig == False else False
    # Setting background color
    screen.fill(border_color)
    
    for y in range(rows):
        for x in range(cols):
            pygame.draw.rect(screen,cell_d_color if cell_status_list[y][x] == 0 else cell_a_color,[x*(b_wid+cell_size),y*(b_wid+cell_size),cell_size,cell_size])
    
    # Updating(Flipping) the whole screen
    pygame.display.flip()
# Exit the program

check_neighbours()
print(future_status_list[0])

pygame.quit()