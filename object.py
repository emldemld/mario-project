from pico2d import *

# Game object class here

class character:
    def __init__(self):
        self.image = load_image('smb_mario.png')
        self.x, self.y = 400, 90
        self.j = -15
        self.frame = 0
        self.state = 5
        self.dir = 0
        self.dr = 1

    def update(self):
        if self.frame != 5:
            self.x += self.dir * 10
            self.frame = (self.frame + 1) % 3
        else:
            self.y -= 5
            self.frame = 5
        if self.j > 0:
            self.y += self.j
            self.j -= 1
        elif self.j <= 0 and self.j > -15:
            self.j -= 1
            self.y += self.j
        else:
            self.j = -15

    def draw(self):
        if self.frame == 5:
            self.image.clip_draw(780, self.state * 66, 64, 66, self.x, self.y)
        elif self.dr == 1 and self.dir != 0 and self.j == -15:
            self.image.clip_draw(self.frame * 60 + 480, self.state * 66, 64, 66, self.x, self.y)
        elif self.dr == -1 and self.dir != 0 and self.j == -15:
            self.image.clip_draw(self.frame * -60 + 300, self.state * 66, 64, 66, self.x, self.y)
        elif self.dr == 1 and self.dir == 0 and self.j == -15:
            self.image.clip_draw(420, self.state * 66, 64, 66, self.x, self.y)
        elif self.dr == -1 and self.dir == 0 and self.j == -15:
            self.image.clip_draw(360, self.state * 66, 64, 66, self.x, self.y)
        elif self.dr == 1 and self.j != -15:
            self.image.clip_draw(720, self.state * 66, 64, 66, self.x, self.y)
        elif self.dr != 1 and self.j != -15:
            self.image.clip_draw(60, self.state * 66, 64, 66, self.x, self.y)

class item:
    def __init__(self, m, n): #생성자
        self.image = load_image('smb_items_sheet.png')
        self.x, self.y = 300, 80
        self.m, self.n = m, n
    def update(self):
        if character.x <= self.x + 15 and character.x >= self.x - 15:
            if character.y <= self.y + 15 and character.y >= self.y - 15:
                self.x = -25
                self.y = -25
                character.state = 3
        elif self.x == -25 and self.y == -25:
            self.x = -50
            self.y = -50
            character.state = 5
        elif self.x == -50 and self.y == -50:
            self.x = -75
            self.y = -75
            character.state = 3
        elif self.x == -75 and self.y == -75:
            self.x = -100
            self.y = -100
            character.state = 5
        elif self.x == -100 and self.y == -100:
            character.state = 3
    def draw(self):
        self.image.clip_draw(self.m * 60, self.n * 60, 60, 60, self.x, self.y)

