from pico2d import *
import server

class Background:

    def __init__(self):
        self.image = load_image('bg-1-1.png')
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