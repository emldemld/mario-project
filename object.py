from pico2d import *
from character import Character
import game_world

class item:
    def __init__(self, m, n): #생성자
        self.image = load_image('smb_items_sheet.png')
        self.x, self.y = 300, 80
        self.m, self.n = m, n
    def update(self):
        if Character.x <= self.x + 15 and Character.x >= self.x - 15:
            if Character.y <= self.y + 15 and Character.y >= self.y - 15:
                self.x = -25
                self.y = -25
                Character.state = 3
        elif self.x == -25 and self.y == -25:
            self.x = -50
            self.y = -50
            Character.state = 5
        elif self.x == -50 and self.y == -50:
            self.x = -75
            self.y = -75
            Character.state = 3
        elif self.x == -75 and self.y == -75:
            self.x = -100
            self.y = -100
            Character.state = 5
        elif self.x == -100 and self.y == -100:
            Character.state = 3
    def draw(self):
        self.image.clip_draw(self.m * 60, self.n * 60, 60, 60, self.x, self.y)

class Enemy:
    def __init__(self):
        self.image = load_image('enemies.png')
        self.x, self.y = 600, 80-2
        self.frame = 0
        self.n = 0
        self.count = 0
        self.dir = 1

    def update(self):
        if 0 < self.count <= 20 and self.dir != 0:
            self.x += self.dir * 5
            self.count += 1
        elif self.count <= 0 and self.dir != 0:
            self.x -= self.dir * 5
            self.count += 1
        elif self.dir == 0:
            self.x = -100
            self.y = -100
        else:
            self.count = -20
            self.dir = -self.dir
        if Character.x <= self.x + 15 and Character.x >= self.x - 15:
            if Character.y >= self.y + 20 and Character.y <= self.y + 40:
                self.dir = 0
            else:
                if Character.state == 5:
                    Character.frame = 5
                    Character.j = 15
                else:
                    Character.state += 2

        self.frame = (self.frame + 1) % 2

    def draw(self):
        if self.dir != 0:
            self.image.clip_draw(self.frame * 60, 480, 60, 60, self.x, self.y)
        else:
            self.image.clip_draw(120, 480, 60, 60, self.x, self.y - 10)

class Ball:
    image = None

    def __init__(self, x=400, y=300, velocity=1):
        if self.image == None:
            self.image = load_image('enemies.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
         self.image.clip_draw(720, 120, 60, 60, self.x, self.y)

    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 750 - 25:
            game_world.remove_object(self)