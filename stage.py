from pico2d import *
import server

class Background:

    def __init__(self):
        self.image = load_image('overworld_bg.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def draw(self):
        # fill here
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, server.stage.canvas_width, server.stage.canvas_height, 0, 0)
        pass

    def update(self):
        # fill here
        self.window_left = clamp(0, int(server.character.x) - server.stage.canvas_width //2, server.stage.w - server.stage.canvas_width)
        self.window_bottom = clamp(0, int(server.character.y) - server.stage.canvas_height // 2, server.stage.h - server.stage.canvas_height)
        pass

    def handle_event(self, event):
        pass

holepos = [1300, 2200, 3100]

class Hole:
    def __init__(self, i):
        self.image = load_image('hole.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.x, self.y = holepos[i], 29
        self.cx, self.y = self.x, self.y

    def get_bb(self):
        return self.cx - 30, self.y - 50, self.cx + 30, self.y + 50

    def update(self):
        self.cx = self.x - server.stage.window_left

    def draw(self):
        self.image.draw(self.cx, self.y, 100, 100)
        #draw_rectangle(*self.get_bb())
        #self.font.draw(self.cx - 60, self.y + 50, '(x: %3.2f)' % self.x, (255, 255, 0))

class Goal:
    def __init__(self):
        self.image = load_image('goal.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.x, self.y = 5500, 204
        self.cx, self.y = self.x, self.y

    def get_bb(self):
        return self.cx - 10, self.y - 150, self.cx + 10, self.y - 25

    def update(self):
        self.cx = self.x - server.stage.window_left

    def draw(self):
        self.image.draw(self.cx, self.y, 256, 256)
        #draw_rectangle(*self.get_bb())
        #self.font.draw(self.cx - 60, self.y + 50, '(x: %3.2f)' % self.x, (255, 255, 0))

    class Hole:
        def __init__(self, i):
            self.image = load_image('hole.png')
            self.font = load_font('ENCR10B.TTF', 16)
            self.x, self.y = holepos[i], 29
            self.cx, self.y = self.x, self.y

        def get_bb(self):
            return self.cx - 30, self.y - 50, self.cx + 30, self.y + 50

        def update(self):
            self.cx = self.x - server.stage.window_left

        def draw(self):
            self.image.draw(self.cx, self.y, 100, 100)
            # draw_rectangle(*self.get_bb())

tilepos = [600, 3600, 4800]

class Tile:
    def __init__(self, i):
        self.image = load_image('tile.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.x, self.y = tilepos[i], 128
        self.cx, self.y = self.x, self.y

    def get_bb(self):
        return self.cx - 36, self.y - 50, self.cx + 36, self.y + 40

    def update(self):
        self.cx = self.x - server.stage.window_left

    def draw(self):
        self.image.draw(self.cx, self.y, 100, 100)
        draw_rectangle(*self.get_bb())