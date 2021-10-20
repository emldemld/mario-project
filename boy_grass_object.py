from pico2d import *

# Game object class here

class bg:
    def __init__(self): #생성자
        self.image = load_image('bg-1-1.png')
    def draw(self):
        self.image.draw(0, -15)

class character:
    def __init__(self):
        self.image = load_image('smb_mario.png')
        self.x, self.y = 400, 80
        self.j = -20
        self.frame = 0
        self.state = 5

    def update(self):
        global dir
        self.x += dir * 10
        self.frame = (self.frame+1) % 3
        if self.j > 0:
            self.y += self.j
            self.j -= 1
        elif self.j <= 0 and self.j > -20:
            self.j -= 1
            self.y += self.j
        else:
            self.j = -20
    def draw(self):
        global dr
        if dr == 1 and dir != 0 and self.j == -20:
            self.image.clip_draw(self.frame * 60 + 480, self.state * 64, 64, 60, self.x, self.y)
        elif dr == -1 and dir != 0 and self.j == -20:
            self.image.clip_draw(self.frame * -60 + 300, self.state * 64, 64, 60, self.x, self.y)
        elif dr == 1 and dir == 0 and self.j == -20:
            self.image.clip_draw(420, self.state * 64, 64, 60, self.x, self.y)
        elif dr == -1 and dir == 0 and self.j == -20:
            self.image.clip_draw(360, self.state * 64, 64, 60, self.x, self.y)
        elif dr == 1 and self.j != -20:
            self.image.clip_draw(720, self.state * 64, 64, 60, self.x, self.y)
        elif dr != 1 and self.j != -20:
            self.image.clip_draw(60, self.state * 64, 64, 60, self.x, self.y)


class enemy:
    def __init__(self):
        self.image = load_image('enemies.png')
        self.x, self.y = 400, 80
        self.j = -20
        self.frame = 0
        self.state = 5

    def update(self):
        global dir
        self.x += dir * 10
        self.frame = (self.frame + 1) % 3
        if self.j > 0:
            self.y += self.j
            self.j -= 1
        elif self.j <= 0 and self.j > -20:
            self.j -= 1
            self.y += self.j
        else:
            self.j = -20

    def draw(self):

def handle_events():
    global running
    global dir
    global dr
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_d:
               dir += 1
               dr = 1
            elif event.key == SDLK_a:
                dr = -1
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_SPACE:
                character.j = 20

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_d:
                dir -= 1
            elif event.key == SDLK_a:
                dir += 1
            elif event.key == SDLK_SPACE:
                character.j = -character.j

# initialization code

open_canvas(1000, 500)

bg =bg()
character = character()

dr = 1
dir = 0
running = True

# game main loop code
while running:

    handle_events()

    #Game logic
    character.update()

    #Game drawing
    clear_canvas()

    bg.draw()
    character.draw()

    update_canvas()

    delay(0.05)

# finalization code