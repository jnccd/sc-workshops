import pygame, sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 0, 255), (10, 10, 300, 500))
    pygame.display.update()