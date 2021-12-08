import game_framework
from pico2d import *
import main_state

name = "ClearState"
image = None


def enter():
    global image
    image = load_image('clear.png')


def exit():
    global image
    del (image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if event.type == SDL_KEYDOWN:
                game_framework.quit()

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






