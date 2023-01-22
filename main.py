import pygame as pygame

pygame.init()


screen = pygame.display.set_mode([750,750])
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)
clock = pygame.time.Clock()
fps= 60


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((106, 106, 106))

    for x in range(50):
        for y in range(50):
            pygame.draw.rect(screen, (134, 134, 134) ,[x*(750/50),y*(750/50),750/50,750/50],1)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()