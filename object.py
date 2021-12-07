from pico2d import *
import game_world

class item:
    def __init__(self, m, n): #생성자
        self.image = load_image('smb_items_sheet.png')
        self.x, self.y = 300, 80
        self.m, self.n = m, n
    def update(self):
        pass
    def draw(self):
        self.image.clip_draw(self.m * 60, self.n * 60, 60, 60, self.x, self.y)

class Ball:
    image = None

    def __init__(self, x=400, y=300, velocity=1):
        if self.image == None:
            self.image = load_image('enemies.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.origin = self.x

    def draw(self):
         self.image.clip_draw(720, 120, 60, 60, self.x, self.y)

    def update(self):
        self.x += self.velocity

        if self.x - self.origin > 100 or self.x - self.origin < -100:
            game_world.remove_object(self)