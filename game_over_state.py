import game_framework
from pico2d import *
import main_state

name = "GameOverState"
image = None
bgm = None

class Bgm:
    def __init__(self):
        self.bgm = load_music('16 - Game Over.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

def enter():
    global image, bgm
    image = load_image('gameover.png')
    bgm = Bgm()


def exit():
    global image, bgm
    del (image)
    del bgm


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)

def draw():
    clear_canvas()
    image.draw(500, 275)
    update_canvas()





def update():
    delay(0.02)


def pause():
    pass


def resume():
    pass



