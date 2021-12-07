import random
import json
import os

import pico2d
from pico2d import *
import game_framework
import game_world

from character import *
from stage import *
from object import *
from enemy import Enemy
import server
import game_over_state

name = "MainState"

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def enter():
    server.character = Character()
    game_world.add_object(server.character, 1)
    server.stage = Background()
    game_world.add_object(server.stage, 0)
    server.enemies = [Enemy() for i in range(6)]
    game_world.add_objects(server.enemies, 1)

def exit():
    game_world.clear()

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
            server.character.handle_event(event)

def update():
    if server.character.y < 0:
        game_framework.change_state(game_over_state)
    for game_object in game_world.all_objects():
        game_object.update()
    for enemy in server.enemies:
        if collide(server.character, enemy):
            if server.character.y - enemy.y > 25 and enemy.dir != 0:
                enemy.dir = 0
                server.enemies.remove(enemy)
                game_world.remove_object(enemy)
            else:
                enemy.dir = 0
                server.character.add_event(DAMAGE)



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()







