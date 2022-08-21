import pygame, sys

pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 0, 255), (10, 10, 300, 500))
    pygame.display.update()