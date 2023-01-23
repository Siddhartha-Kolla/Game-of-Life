import pygame as pygame

# Initializing pygame
pygame.init()

# Number of rows and columns

rows , cols = 50 , 50

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
        if event.type == pygame.QUIT:
            running = False
    
    # Setting background color
    screen.fill()

    # Drawing grid
    for x in range(50):
        for y in range(50):
            pygame.draw.rect(screen, (134, 134, 134) ,[x*(750/50),y*(750/50),750/50,750/50],1)

    # Updating(Flipping) the whole screen
    pygame.display.flip()

# Exit the program
pygame.quit()