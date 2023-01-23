import pygame as pygame

# Initializing pygame
pygame.init()

# Configuring screen
screen = pygame.display.set_mode([750,750])

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
    screen.fill((106, 106, 106))

    # Drawing grid
    for x in range(50):
        for y in range(50):
            pygame.draw.rect(screen, (134, 134, 134) ,[x*(750/50),y*(750/50),750/50,750/50],1)

    # Updating(Flipping) the whole screen
    pygame.display.flip()

# Exit the program
pygame.quit()