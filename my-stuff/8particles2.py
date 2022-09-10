import pygame, sys
from pygame import Vector2

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pgclock = pygame.time.Clock()

class Particle:
    def __init__(self, x, y):
        self.pos = Vector2(x, y)
        self.vel = Vector2(0, 0)
    
    def update(self):
        self.pos += self.vel
        
        if self.pos.x < 0:
            self.vel.x *= -1
        if self.pos.y < 0:
            self.vel.y *= -1
        if self.pos.x > screen.get_width():
            self.vel.x *= -1
        if self.pos.y > screen.get_height():
            self.vel.y *= -1
            
        self.vel *= 0.96
        
    def get_pulled_to(self, target_vec):
        diff = self.pos - target_vec
        if (diff.length_squared() > 0):
            self.vel -= diff * (200 / (diff*diff))

particles = []
for x in range(0, screen.get_width(), 12):
    for y in range(0, screen.get_height(), 12):
        particles.append(Particle(x, y))

while True:
    screen.fill((0, 0, 0))
    
    # Control 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if pygame.mouse.get_pressed(3)[0]:
        for p in particles:
            p.get_pulled_to(pygame.mouse.get_pos())
    
    # Logic
    for p in particles:
        p.update()
        
    # Drawing
    for p in particles:
        pygame.draw.rect(screen, (10,125,255), (p.pos.x, p.pos.y, 1, 1))
    
    pygame.display.update()
    pgclock.tick(60)