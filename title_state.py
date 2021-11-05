import game_framework
from pico2d import *
import main_state

name = "TitleState"
image = None
logo_time = 0.0

def enter():
    global image
    image = load_image('title.jpg')

def exit():
    global image
    del(image)

def update():
    global logo_time
    if (logo_time > 1.0):
        logo_time = 0
        game_framework.quit()
    delay(0.01)
    logo_time += 0.01

def draw():
    clear_canvas()
    image.draw(500, 300)
    update_canvas()


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


def pause(): pass


def resume(): pass




