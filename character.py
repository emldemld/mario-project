from pico2d import *
import game_framework
import game_world
import server
from object import Ball

# Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 25.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE_DOWN, SPACE_UP, SHIFT, MUSHROOM, DAMAGE = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_d): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_a): LEFT_DOWN,
    (SDL_KEYUP, SDLK_d): RIGHT_UP,
    (SDL_KEYUP, SDLK_a): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN,
    (SDL_KEYUP, SDLK_SPACE): SPACE_UP,
    (SDL_KEYDOWN, SDLK_LSHIFT): SHIFT,
    (SDL_KEYDOWN, SDLK_RSHIFT): DAMAGE
}

class SmallIdleState:
    def enter(character, event):
        if event == RIGHT_DOWN:
            character.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            character.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            character.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            character.velocity += RUN_SPEED_PPS
        elif event == SPACE_UP:
            if character.j != -10:
                character.j = -character.j
        elif event == SPACE_DOWN:
            character.j = 10


    def exit(character, event):
        if event == DAMAGE:
            character.frame = 5
            character.j = 10

    def do(character):
        if character.j > 0:
            character.y += character.j
            character.j -= 0.2
        elif character.j <= 0 and character.j > -10:
            character.j -= 0.2
            character.y += character.j
        elif character.j == -11 or character.frame == 5:
            character.y += character.j
        else:
            character.y += character.j
            character.j = -10
    def draw(character):
        if character.frame == 5:
            character.image.clip_draw(780, 5 * 66, 64, 66, character.cx, character.cy)
        elif character.j > -10 and character.dir == 1 and character.frame != 5:
            character.image.clip_draw(720, 5 * 66, 64, 66, character.cx, character.cy)
        elif character.j > -10 and character.dir == -1 and character.frame != 5:
            character.image.clip_draw(60, 5 * 66, 64, 66, character.cx, character.cy)
        elif character.j == -10 and character.dir == 1:
            character.image.clip_draw(420, 5 * 66, 64, 66, character.cx, character.cy)
        elif character.j == -10 and character.dir == -1:
            character.image.clip_draw(360, 5 * 66, 64, 66, character.cx, character.cy)


class SmallRunState:
    def enter(character, event):
        if event == RIGHT_DOWN:
            character.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            character.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            character.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            character.velocity += RUN_SPEED_PPS
        elif event == SPACE_UP:
            if character.j != -10:
                character.j = -character.j
        elif event == SPACE_DOWN:
            character.j = 10
        character.dir = clamp(-1, character.velocity, 1)

    def exit(character, event):
        if event == DAMAGE:
            character.frame = 5
            character.j = 10

    def do(character):
        character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        character.x += character.velocity * game_framework.frame_time
        if character.j > 0:
            character.y += character.j
            character.j -= 0.2
        elif character.j <= 0 and character.j > -10:
            character.j -= 0.2
            character.y += character.j
        elif character.j == -11 or character.frame == 5:
            character.y += character.j
        else:
            character.y += character.j
            character.j = -10
        character.x = clamp(25, character.x, 5952 - 25)
        #character.y = clamp(90, character.y, server.stage.h - 90)

    def draw(character):
        if character.j > -10 and character.dir == 1:
            character.image.clip_draw(720, 5 * 66, 64, 66, character.cx, character.cy)
        elif character.j > -10 and character.dir == -1:
            character.image.clip_draw(60, 5 * 66, 64, 66, character.cx, character.cy)
        elif character.j == -10 and character.dir == 1:
            character.image.clip_draw(int(character.frame) * 60 + 480, 66 * 5, 64, 66, character.cx, character.cy)
        else:
            character.image.clip_draw(int(character.frame) * -60 + 300, 66 * 5, 64, 66, character.cx, character.cy)


class BigIdleState:
    def enter(character, event):
        if event == RIGHT_DOWN:
            character.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            character.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            character.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            character.velocity += RUN_SPEED_PPS
        elif event == SPACE_UP:
            if character.j != -10:
                character.j = -character.j
        elif event == SPACE_DOWN:
            character.j = 10
        elif event == DAMAGE:
            pass

    def exit(character, event):
        pass

    def do(character):
        if character.j > 0:
            character.y += character.j
            character.j -= 0.2
        elif character.j <= 0 and character.j > -10:
            character.j -= 0.2
            character.y += character.j
        elif character.j == -11 or character.frame == 5:
            character.y += character.j
        else:
            character.y += character.j
            character.j = -10

    def draw(character):
        if character.j > -10 and character.dir == 1:
            character.image.clip_draw(720, 3 * 66, 64, 66, character.cx, character.cy)
        elif character.j > -10 and character.dir == -1:
            character.image.clip_draw(60, 3 * 66, 64, 66, character.cx, character.cy)
        elif character.j == -10 and character.dir == 1:
            character.image.clip_draw(420, 3 * 66, 64, 66, character.cx, character.cy)
        else:
            character.image.clip_draw(360, 3 * 66, 64, 66, character.cx, character.cy)


class BigRunState:
    def enter(character, event):
        if event == RIGHT_DOWN:
            character.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            character.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            character.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            character.velocity += RUN_SPEED_PPS
        elif event == SPACE_UP:
            if character.j != -10:
                character.j = -character.j
        elif event == SPACE_DOWN:
            character.j = 10
        character.dir = clamp(-1, character.velocity, 1)

    def exit(character, event):
        pass

    def do(character):
        character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        character.x += character.velocity * game_framework.frame_time
        if character.j > 0:
            character.y += character.j
            character.j -= 0.2
        elif character.j <= 0 and character.j > -10:
            character.j -= 0.2
            character.y += character.j
        elif character.j == -11 or character.frame == 5:
            character.y += character.j
        else:
            character.y += character.j
            character.j = -10
        character.x = clamp(25, character.x, 5952 - 25)
        #character.y = clamp(90, character.y, server.background.h - 90)

    def draw(character):

        if character.j > -10 and character.dir == 1:
            character.image.clip_draw(720, 3 * 66, 64, 66, character.cx, character.cy)
        elif character.j > -10 and character.dir == -1:
            character.image.clip_draw(60, 3 * 66, 64, 66, character.cx, character.cy)
        elif character.j == -10 and character.dir == 1:
            character.image.clip_draw(int(character.frame) * 60 + 480, 66 * 3, 64, 66, character.cx, character.cy)
        else:
            character.image.clip_draw(int(character.frame) * -60 + 300, 66 * 3, 64, 66, character.cx, character.cy)

next_state_table = {
    SmallIdleState: {RIGHT_UP: SmallRunState, LEFT_UP: SmallRunState, RIGHT_DOWN: SmallRunState, LEFT_DOWN: SmallRunState,
                     SPACE_UP: SmallIdleState, SPACE_DOWN: SmallIdleState, SHIFT: SmallIdleState, MUSHROOM: BigIdleState, DAMAGE: SmallIdleState},
    SmallRunState: {RIGHT_UP: SmallIdleState, LEFT_UP: SmallIdleState, LEFT_DOWN: SmallIdleState, RIGHT_DOWN: SmallIdleState,
                    SPACE_UP: SmallRunState, SPACE_DOWN: SmallRunState, SHIFT: SmallRunState, MUSHROOM: BigRunState, DAMAGE: SmallIdleState},
    BigIdleState: {RIGHT_UP: BigRunState, LEFT_UP: BigRunState, RIGHT_DOWN: BigRunState, LEFT_DOWN: BigRunState,
                    SPACE_UP: BigIdleState, SPACE_DOWN: BigIdleState, SHIFT: BigIdleState, MUSHROOM: BigIdleState, DAMAGE: SmallIdleState},
    BigRunState: {RIGHT_UP: BigIdleState, LEFT_UP: BigIdleState, LEFT_DOWN: BigIdleState, RIGHT_DOWN: BigIdleState,
                    SPACE_UP: BigRunState, SPACE_DOWN: BigRunState, SHIFT: BigRunState, MUSHROOM: BigRunState, DAMAGE: SmallRunState},
}

class Character:
    def __init__(self):
        self.image = load_image('smb_mario.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.x, self.y = 300, 120
        self.cx, self.cy = self.x, self.y
        self.j = -10
        self.frame = 0
        self.dir = 1
        self.velocity = 0
        self.event_que = []
        self.cur_state = BigIdleState
        self.cur_state.enter(self, None)

    def get_bb(self):
        return self.cx - 18, self.y - 35, self.cx + 18, self.y + 35


    def fire_ball(self):
        server.ball = Ball(self.x, self.y, self.dir * RUN_SPEED_PPS * 10)
        game_world.add_object(server.ball, 1)


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cx, self.cy = self.x - server.stage.window_left, self.y - server.stage.window_bottom
        if self.j == -10:
            self.y = clamp(120, self.y, server.stage.h - 120)
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())
        self.font.draw(self.cx - 60, self.y + 50, '(x: %3.2f)' % self.x, (255, 255, 0))
        #self.font.draw(self.cx - 60, self.y + 75, '(cx: %3.2f)' % self.cx, (255, 255, 0))


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

