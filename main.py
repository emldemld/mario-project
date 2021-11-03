from pico2d import *
import game_framework
import object
import stage

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_d:
               character.dir += 1
               character.dr = 1
            elif event.key == SDLK_a:
                character.dr = -1
                character.dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_SPACE:
                character.j = 15

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_d:
                character.dir -= 1
            elif event.key == SDLK_a:
                character.dir += 1
            elif event.key == SDLK_SPACE:
                character.j = -character.j

# initialization code

open_canvas(1000, 500)

bg = stage.bg()
character = object.character()
enemy = object.enemy()
mush = object.item(6, 2)
running = True

# game main loop code
while running:

    handle_events()

    #Game logic
    mush.update()
    enemy.update()
    character.update()

    #Game drawing
    clear_canvas()

    bg.draw()
    mush.draw()
    enemy.draw()
    character.draw()

    update_canvas()

    delay(0.05)

# finalization code