from pico2d import *
import game_framework
import title_state

import object
import stage

# initialization code

open_canvas(1000, 750)
game_framework.run(title_state)
close_canvas()