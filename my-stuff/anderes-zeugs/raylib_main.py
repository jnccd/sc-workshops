import os
import pyray as pr

try: 
    os.chdir('Spacegame')
except:
    print("Already in correct dir")
    
class Player:
    pos_x = 0
    pos_y = 0
    pos = (pos_x, pos_y)
    
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

# Init
pixel_size = 6
b_size = (b_width, b_height) = (240, 160) # Background
t_size = (t_width, t_height) = (16, 16) # Tile
w_size = (w_width, w_height) = (b_width * pixel_size, b_height * pixel_size) # Window
pr.init_window(w_width, w_height, "Hello")
pr.set_target_fps(60)
ground_height = w_height - 16 * pixel_size

# Load Assets
tex_back = pr.load_texture("images/background.png")
tex_protag_idle = pr.load_texture("images/herochar_idle_anim_strip_4.png")
tex_tileset = pr.load_texture("images/tileset.png")

# Game Loop
while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.WHITE)
    
    pr.draw_texture_pro(tex_back, (0,0,b_width,b_height), (0,0,w_width,w_height), (0,0), 0, pr.WHITE)
    pr.draw_texture_pro(tex_protag_idle, (0,0,16,16), (0,0,16*pixel_size,16*pixel_size), (0,0), 0, pr.WHITE)
    pr.draw_texture_tiled(tex_tileset, (112, 48, 16, 16), (0, ground_height, w_width, 16*pixel_size), (0,0), 0, pixel_size, pr.WHITE)
    
    pr.end_drawing()
pr.close_window()