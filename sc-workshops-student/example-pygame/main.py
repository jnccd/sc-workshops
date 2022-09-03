# Textures from https://o-lobster.itch.io/platformmetroidvania-pixel-art-asset-pack
# Font from https://www.1001fonts.com/press-start-font.html
import pygame, os
from typing import List

# Starting from the directory above means we need to move into spacegame for the relative path's to work
try: 
    os.chdir('StudentStuff')
except:
    pass
try: 
    os.chdir('ExampleGame')
except:
    pass

#-----------------------------------------------------------------------------------------------------------------------------------
# Initiate
#-----------------------------------------------------------------------------------------------------------------------------------
# Can mostly be ignored, loads images and other data

pygame.init()
pygame.font.init()

# Create Window
pixel_size = 5
tex_back = pygame.image.load('assets/background.png') # Load background early for window size calculation
wsize = (wwidth, wheight) = (tex_back.get_width() * pixel_size, tex_back.get_height() * pixel_size) # Window Widht / Height
display = pygame.display.set_mode(wsize)
pygame.display.set_caption("Pygame Tutorial Platformer") 

# Load and Resize Textures
tex_back_scaled = pygame.transform.scale(tex_back, (wwidth, wheight))
tex_player = pygame.image.load('assets/herochar_idle_anim_strip_4.png')
tex_monster = pygame.image.load('assets/slime_idle_anim_strip_5.png')
font = pygame.font.Font('assets/prstartk.ttf', 30)
tex_s = pygame.Vector2(16, 16) # Single image size

# Complicated Method that cuts out part of an image
def clip(surface, x, y, x_size, y_size):
    handle_surface = surface.copy() #Sprite that will get process later
    clipRect = pygame.Rect(x,y,x_size,y_size) #Part of the image
    handle_surface.set_clip(clipRect) #Clip or you can call cropped
    image = surface.subsurface(handle_surface.get_clip())
    return image.copy()

# Physics
player_speed = 1.2
enemy_speed = 0.7
jump_force = 70
gravity = 1.5
friction = 0.9

#-----------------------------------------------------------------------------------------------------------------------------------
# Game Classes
#-----------------------------------------------------------------------------------------------------------------------------------
# Contains Logic specifically for enemies and the player in the update() method

class Entity:
    def __init__(self, position, size, texture):
        self.pos = position
        self.vel = pygame.Vector2(0, 0) # Velocity
        self.size = size
        self.touching_ground = False
        self.tex = texture
        self.marked_for_deletion = False
    
    def update(self):
        self.vel.y += gravity
        self.vel *= friction
        self.pos += self.vel
        
        # Up/Down Bounds Collision
        if self.pos.y < 0:
            self.pos.y = 0
        if self.pos.y > wheight - self.size.y:
            self.pos.y = wheight - self.size.y
            self.touching_ground = True
        else:
            self.touching_ground = False
        
    def draw(self):
        display.blit(self.tex, self.pos)
        
class Player(Entity):
    def __init__(self):
        super().__init__(pygame.Vector2(0, 0), tex_s * pixel_size, tex_player)
        
    def update(self):
        global score
        global entities
        super().update()
        
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.x > wwidth - self.size.x:
            self.pos.x = wwidth - self.size.x
            
        for e in entities[1:]:
            if self.pos.x < e.pos.x + e.size.x and self.pos.x + self.size.x > e.pos.x and self.pos.y < e.pos.y + e.size.y and self.pos.y + self.size.y > e.pos.y:
                if self.pos.y < e.pos.y - e.size.y / 2:
                    # Hopped on his head
                    e.marked_for_deletion = True
                    self.vel.y -= 50
                    score += 15
                else:
                    # Ran into him
                    score = 0
                    self.pos = pygame.Vector2(0, 0)
                    self.vel = pygame.Vector2(0, 0)
                    entities = [self]
    
    def draw(self):
        cur_sprite = clip(self.tex, 0, 0, tex_s.x, tex_s.y)
        scaled_tex = pygame.transform.scale(cur_sprite, self.size)
        display.blit(scaled_tex, self.pos)
        
class Enemy(Entity):
    def __init__(self):
        super().__init__(pygame.Vector2(wwidth, wheight), tex_s * pixel_size, tex_monster)
        
    def update(self):
        self.vel.x -= enemy_speed        
        super().update()
    
    def draw(self):
        cur_sprite = clip(self.tex, 0, 0, tex_s.x, tex_s.y)
        scaled_tex = pygame.transform.scale(cur_sprite, self.size)
        display.blit(scaled_tex, self.pos)
        
#-----------------------------------------------------------------------------------------------------------------------------------
# Create Loop Variables
#-----------------------------------------------------------------------------------------------------------------------------------
# Can mostly be ignored, creates variables for the game loop operation

global score
global entities
player = Player()
entities: List[Entity] = [player]
score = 0

# Timings
fps = 60
pgclock = pygame.time.Clock()
frame_timer = 0

#-----------------------------------------------------------------------------------------------------------------------------------
# Game Loop
#-----------------------------------------------------------------------------------------------------------------------------------
# Defines the game loop which is executed at 60 FPS, checks for key presses and creates new enemies, etc.

while True:
    frame_timer += 1
    
    # Key Events
    if (len([x for x in pygame.event.get() if x.type == pygame.QUIT])):
        break
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.vel.x -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.vel.x += player_speed
    if keys[pygame.K_SPACE] and player.touching_ground:
        player.vel.y -= jump_force
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.vel.y += player_speed
    
    # Logic
    if (frame_timer / fps) % 3 == 1:
        entities.append(Enemy()) # Create new enemy
    for e in entities:
        e.update()
    entities = [e for e in entities if not e.marked_for_deletion] # Remove marked entites
    
    # Draw
    display.blit(tex_back_scaled, [0,0]) # Background
    for e in entities:
        e.draw()
    texttex = font.render("Score " + str(score), True, (255, 255, 255))
    display.blit(texttex, (10,10))
    pygame.display.update()
    
    # Enforce FPS limit
    pgclock.tick(fps)
    
pygame.quit()