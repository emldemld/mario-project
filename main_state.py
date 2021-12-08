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
import clear_state

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
    server.stage = Background()
    game_world.add_object(server.stage, 0)
    server.enemies = [Enemy(i) for i in range(6)]
    game_world.add_objects(server.enemies, 1)
    server.holes = [Hole(i) for i in range(3)]
    game_world.add_objects(server.holes, 1)
    server.tiles = [Tile(i) for i in range(3)]
    game_world.add_objects(server.tiles, 1)
    server.blocks = [Block(i) for i in range(5)]
    game_world.add_objects(server.blocks, 1)
    server.goal = Goal()
    game_world.add_object(server.goal, 1)
    server.character = Character()
    game_world.add_object(server.character, 1)

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
    if collide(server.character, server.goal):
        game_framework.change_state(clear_state)
    for game_object in game_world.all_objects():
        game_object.update()

    for enemy in server.enemies:
        if collide(server.character, enemy):
            if server.character.y - enemy.y > 25 and enemy.dir != 0:
                enemy.dir = 0
                server.enemies.remove(enemy)
                game_world.remove_object(enemy)
            else:
                if enemy.x > server.character.x:
                    server.character.x -= RUN_SPEED_PPS * game_framework.frame_time * 20
                else:
                    server.character.x += RUN_SPEED_PPS * game_framework.frame_time * 20
                server.character.add_event(DAMAGE)
                server.character.y = clamp(120, server.character.y, 150)
        for hole in server.holes:
            if collide(hole, enemy):
                enemy.y -= 10
        for tile in server.tiles:
            if collide(tile, enemy):
                if tile.x > enemy.x:
                    enemy.x -= RUN_SPEED_PPS * game_framework.frame_time
                else:
                    enemy.x += RUN_SPEED_PPS * game_framework.frame_time

    for hole in server.holes:
        if server.character.j == 0 and collide(server.character, hole):
            server.character.y -= server.character.j
        elif server.character.j != -11 and collide(server.character, hole):
            if server.character.x > hole.x - 50 and server.character.x < hole.x + 50:
                server.character.j = -11
                server.character.y -= server.character.j

    for tile in server.tiles:
        if collide(server.character, tile):
            if server.character.y >= tile.y + 40:
                server.character.y = tile.y + 75
            else:
                if tile.x > server.character.x:
                    server.character.x -= RUN_SPEED_PPS * game_framework.frame_time
                else:
                    server.character.x += RUN_SPEED_PPS * game_framework.frame_time

    for block in server.blocks:
        if collide(server.character, block):
            if server.character.y >= block.y + 20:
                server.character.y = block.y + 55
            else:
                if block.x > server.character.x and block.y <= server.character.y:
                    server.character.x -= RUN_SPEED_PPS * game_framework.frame_time
                elif block.x < server.character.x and block.y <= server.character.y:
                    server.character.x += RUN_SPEED_PPS * game_framework.frame_time
                else:
                    server.blocks.remove(block)
                    game_world.remove_object(block)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()







