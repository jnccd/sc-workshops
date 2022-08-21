from pyray import *
init_window(800, 450, "Hello")
while not window_should_close():
    begin_drawing()
    clear_background(WHITE)
    draw_text("Yes, it wörks C:", 190, 200, 20, VIOLET)
    end_drawing()
close_window()