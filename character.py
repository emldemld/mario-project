from pico2d import *
import game_framework
import game_world

# Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Character:
    def __init__(self):
        self.image = load_image('smb_mario.png')
        self.x = 400
        self.y = 90
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

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_d:
                self.dir += 1
                self.dr = 1
            elif event.key == SDLK_a:
                self.dr = -1
                self.dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_SPACE:
                self.j = 15
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_d:
                self.dir -= 1
            elif event.key == SDLK_a:
                self.dir += 1
            elif event.key == SDLK_SPACE:
                self.j = -self.j