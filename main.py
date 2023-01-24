import numpy as np
import pygame as pygame
import random

# Initializing pygame
pygame.init()

# Number of rows and columns
rows , cols = 50,75

# Creating a numpy array to check whether cell is alive or not(currently randomly generated)
global cell_status_list
cell_status_list = []
for i in range(rows):
    cell_status_list.append([random.getrandbits(1) for i in range(cols)])
cell_status_list = np.array(cell_status_list)


# Creating a numpy array for the cell status after checking the neighbors
global future_status_list
future_status_list = np.zeros((rows,cols),np.int8)

# Speed of the cycle
speed = 20

# Size of each cell
cell_size = 14

#Border width
b_wid = 1

# Border color
border_color = (134,134,134)

# Dead cell color
cell_d_color = (106, 106, 106)

# Alive cell color
cell_a_color = (255, 255, 0)

# Text display screen color
t_s_bg = (74, 182, 212)

# Text color
t_color = (29, 133, 34)

# Boolean that indicates whether to continue life cycle or not
cycle_runnig = False

extra_space = 200

# Configuring screen(setting its size by finding out the space rows and cols need)
screen = pygame.display.set_mode([cols*(cell_size+b_wid)+extra_space,rows*(cell_size+b_wid)])

# Adding a title
pygame.display.set_caption("Conways Game of Life")

# Adding an icon to the screen
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)

# Adding clock
clock = pygame.time.Clock()

# Game Loop
running = True


# Function to check the neighbors of each cell and update game list
def check_neighbours():
    # Iterating over each cell and counting the number of neighbors
    for row , col in np.ndindex(cell_status_list.shape):
        neib_temp = 0
        neib_temp = np.sum(cell_status_list[row-1:row+2 , col-1:col+2]) - cell_status_list[row,col]
    
        # Checking if the cell is alive or not and updating its status by using the rules
        # Rules for alive cells 
        if cell_status_list[row][col] == 1:
            if neib_temp == 3 or neib_temp == 2:
                future_status_list[row][col] = 1
            else:
                future_status_list[row][col] = 0

        # Rules for dead cells
        elif cell_status_list[row][col] == 0:
            if neib_temp == 3:
                future_status_list[row][col] = 1
            else:
                future_status_list[row][col] = 0
    
    # Returning the updated list
    return future_status_list

def display_text():
    pygame.draw.rect(screen,t_s_bg,[cols*(cell_size+b_wid),0,extra_space,rows*(cell_size+b_wid)])

# Main game loop
while running:

    # Checking events
    for event in pygame.event.get():

        # Quit event
        if event.type == pygame.QUIT:
            running = False
        # Event for checking different key press events
        if event.type == pygame.KEYDOWN:
            # Space key event(activates the life cycle)
            if event.key == pygame.K_SPACE:
                if cycle_runnig == False:
                    cycle_runnig = True
                elif cycle_runnig == True:
                    cycle_runnig = False
            if event.key == pygame.K_UP:
                speed = min(25,speed+1)
            if event.key == pygame.K_DOWN:
                speed = max(5,speed-1)
        # Mouse button events
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Mouse pointer position
            MouseX,MouseY = event.pos
            # Pulling out the status of the clicked cell
            status_temp = cell_status_list[MouseY//(cell_size+b_wid) , MouseX//(cell_size+b_wid)]
            # Setting new status of the clicked cell
            if status_temp == 0:
                cell_status_list[MouseY//(cell_size+b_wid), MouseX//(cell_size+b_wid)] = 1
            else:
                cell_status_list[MouseY//(cell_size+b_wid), MouseX//(cell_size+b_wid)] = 0

    # Setting background color
    screen.fill(border_color)

    # Life cycle
    if cycle_runnig:
        cell_status_list = np.array(check_neighbours())
    
    display_text()


    # Drawing the rectangles
    for y in range(rows):
        for x in range(cols):
            pygame.draw.rect(screen,cell_d_color if cell_status_list[y][x] == 0 else cell_a_color,[x*(b_wid+cell_size),y*(b_wid+cell_size),cell_size,cell_size])
    
    # Updating(Flipping) the whole screen
    pygame.display.flip()

    # Clock tick argument(Useful for making life cycle slower or faster)
    clock.tick(speed)


# Exit the program
pygame.quit()