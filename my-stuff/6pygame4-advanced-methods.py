from math import cos, sin
import pygame, sys

pygame.init()
s_width = 1280
s_height = 720
screen = pygame.display.set_mode((1280, 720))
pgclock = pygame.time.Clock()

r_width = 60
r_height = 30

def draw_rect(screen, clock, xbase):
    pygame.draw.rect(screen, (0, (sin(clock / 10) + 1) * 127, 255), 
                     (s_width / 2 + xbase + cos(clock / 10) * 80 - r_width / 2, 
                      s_height / 2 + sin(clock / 10) * 40 - r_height / 2, r_width, r_height))

clock = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill((0, 0, 0))
    draw_rect(screen, clock, 0)
    draw_rect(screen, clock + 50, 100)
    draw_rect(screen, clock - 50, -100)
    pygame.display.update()
    
    pgclock.tick(60)
    clock += 1