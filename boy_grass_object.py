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
        self.j = -15
        self.frame = 0
        self.state = 5
        self.dir = 0
        self.dr = 1

    def update(self):
        self.x += self.dir * 10
        self.frame = (self.frame+1) % 3
        if self.j > 0:
            self.y += self.j
            self.j -= 1
        elif self.j <= 0 and self.j > -15:
            self.j -= 1
            self.y += self.j
        else:
            self.j = -15

    def draw(self):
        if self.dr == 1 and self.dir != 0 and self.j == -15:
            self.image.clip_draw(self.frame * 60 + 480, self.state * 64, 64, 60, self.x, self.y)
        elif self.dr == -1 and self.dir != 0 and self.j == -15:
            self.image.clip_draw(self.frame * -60 + 300, self.state * 64, 64, 60, self.x, self.y)
        elif self.dr == 1 and self.dir == 0 and self.j == -15:
            self.image.clip_draw(420, self.state * 64, 64, 60, self.x, self.y)
        elif self.dr == -1 and self.dir == 0 and self.j == -15:
            self.image.clip_draw(360, self.state * 64, 64, 60, self.x, self.y)
        elif self.dr == 1 and self.j != -15:
            self.image.clip_draw(720, self.state * 64, 64, 60, self.x, self.y)
        elif self.dr != 1 and self.j != -15:
            self.image.clip_draw(60, self.state * 64, 64, 60, self.x, self.y)

class enemy:
    def __init__(self):
        self.image = load_image('enemies.png')
        self.x, self.y = 600, 80-2
        self.frame = 0
        self.count = 0
        self.dir = 1

    def update(self):
        if 0 < self.count <= 20:
            self.x += self.dir * 5
            self.count += 1
        elif self.count <= 0:
            self.x -= self.dir * 5
            self.count += 1
        else:
            self.count = -20
            self.dir = -self.dir
        self.frame = (self.frame + 1) % 2

    def draw(self):
        if self.dir != 0:
            self.image.clip_draw(self.frame * 60, 480, 60, 60, self.x, self.y)
        else:
            self.image.clip_draw(120, 480, 60, 60, self.x, self.y - 10)

class item:
    def __init__(self, m, n): #생성자
        self.image = load_image('smb_items_sheet.png')
        self.x, self.y = 300, 80
        self.m, self.n = m, n
    def update(self):
        if character.x < self.x + 10 and character.x > self.x - 10:
            if character.y < self.y + 10 and character.y > self.y - 10:
                self.m = 10
                self.n = 10
                character.state = 3
    def draw(self):
        self.image.clip_draw(self.m * 60, self.n * 60, 60, 60, self.x, self.y)

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

bg = bg()
character = character()
enemy = enemy()
mush = item(6, 2)
running = True

# game main loop code
while running:

    handle_events()

    #Game logic
    character.update()
    enemy.update()
    mush.update()

    #Game drawing
    clear_canvas()

    bg.draw()
    character.draw()
    enemy.draw()
    mush.draw()

    update_canvas()

    delay(0.05)

# finalization code