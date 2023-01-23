import numpy as np
import pygame as pygame

# Initializing pygame
pygame.init()

# Number of rows and columns
rows , cols = 50,50

# Creating a numpy array to check whether cell is alive or not
cell_status_list = np.zeros((rows,cols),np.int8)
print(cell_status_list)

# Creating a numpy array for the cell status after checking the neighbors
future_status_list = np.zeros((rows,cols),np.int8)
print(future_status_list)

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
while running:

    # Checking events
    for event in pygame.event.get():
        # Quit event
        if event.type == pygame.QUIT:
            running = False
        # Mouse click event
        if event.type == pygame.MOUSEBUTTONDOWN:
            MouseX , MouseY = event.pos
        # Spacebar click event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cycle_runnig = True if cycle_runnig == False else False
    # Setting background color
    screen.fill(border_color)
    
    for y in range(rows):
        for x in range(cols):
            pygame.draw.rect(screen,cell_d_color,[x*(b_wid+cell_size),y*(b_wid+cell_size),cell_size,cell_size])
    
    # Updating(Flipping) the whole screen
    pygame.display.flip()

# Exit the program
pygame.quit()