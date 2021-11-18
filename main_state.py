import random
import json
import os

from pico2d import *
import game_framework
import game_world

from character import Character
from stage import Stage
from object import *


name = "MainState"

character = None
stage = None
enemy = None

def enter():
    global character, stage, enemy
    character = Character()
    stage = Stage()
    enemy = Enemy()

def exit():
    global character, stage
    del character
    del stage
    del enemy

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            character.handle_event(event)

def update():
    character.update()
    #enemy.update()
    delay(0.02)


def draw():
    clear_canvas()
    stage.draw()
    character.draw()
    enemy.draw()
    update_canvas()







