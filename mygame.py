from pico2d import *
import game_framework
import title_state

# initialization code

open_canvas(1000, 500)
game_framework.run(title_state)
close_canvas()