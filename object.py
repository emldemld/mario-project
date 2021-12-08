from pico2d import *
import game_framework
import server

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Mushroom:
    def __init__(self): #생성자
        self.image = load_image('smb_items_sheet.png')
        self.x, self.y = 900, 405
        self.cx, self.y = self.x, self.y

    def get_bb(self):
        return self.cx - 20, self.y - 20, self.cx + 20, self.y + 20

    def update(self):
        self.cx = self.x - server.stage.window_left

    def draw(self):
        self.image.clip_draw(360, 120, 60, 60, self.cx, self.y)

blockpos = [(820, 200), (860, 200), (900, 200), (940, 200), (980, 200),
            (2520, 200), (2600, 200), (2680, 200), (2760, 200),
            (2600, 400),  (2680, 400),
            (3820, 200), (3860, 200), (3900, 200), (3940, 200), (3980, 200), (4020, 200), (4060, 200), (4100, 200),
            (4220, 200), (4260, 200), (4300, 200), (4340, 200), (4380, 200), (4420, 200), (4460, 200), (4500, 200),
            (4020, 400), (4100, 400), (4140, 400), (4180, 400), (4220, 400), (4300, 400)
            ]

class Block:
    def __init__(self, i):
        self.image = load_image('block.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.x, self.y = blockpos[i]
        self.cx, self.y = self.x, self.y

    def get_bb(self):
        return self.cx - 20, self.y - 20, self.cx + 20, self.y + 20

    def update(self):
        self.cx = self.x - server.stage.window_left

    def draw(self):
        self.image.clip_draw(0, 40, 40, 40, self.cx, self.y)
        draw_rectangle(*self.get_bb())

iblockpos = [(900, 400), (2560, 200), (2640, 200), (2720, 200), (2640, 400),
             (4060, 400), (4260, 400)]

class IBlock:
    def __init__(self, i):
        self.image = load_image('block.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.x, self.y = iblockpos[i]
        self.cx, self.y = self.x, self.y

    def get_bb(self):
        return self.cx - 20, self.y - 20, self.cx + 20, self.y + 20

    def update(self):
        self.cx = self.x - server.stage.window_left

    def draw(self):
        self.image.clip_draw(0, 0, 40, 40, self.cx, self.y)
        draw_rectangle(*self.get_bb())

class Ball:
    def __init__(self, x, y, velocity=1):
        self.image = load_image('enemies.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.origin = self.x
        self.cx, self.y = self.x, self.y

    def get_bb(self):
        return self.cx - 20, self.y - 20, self.cx + 20, self.y + 20

    def update(self):
        self.cx = self.x - server.stage.window_left
        self.x += self.velocity
        if self.x - self.origin > 200 or self.x - self.origin < -200:
            server.balls.remove(self)

    def draw(self):
        if self.velocity > 0:
            self.image.clip_draw(0, 120, 60, 40, self.cx, self.y)
        else:
            self.image.clip_draw(0, 0, 60, 40, self.cx, self.y)
        draw_rectangle(*self.get_bb())


class Coin:
    def __init__(self, i): #생성자
        self.image = load_image('smb_items_sheet.png')
        self.x, self.y = iblockpos[i + 1]
        self.cx, self.y = self.x, self.y + 10
        self.frame, self.count = 0, 0

    def get_bb(self):
        return self.cx , self.y , self.cx, self.y

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.cx = self.x - server.stage.window_left

    def draw(self):
        self.image.clip_draw(240 + int(self.frame) * 60, 0, 60, 60, self.cx, self.y)