from pico2d import *
import game_framework
import game_world
import server
from object import Ball

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

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE, SHIFT, MUSHROOM, DAMAGE = range(8)

key_event_table = {
    (SDL_KEYDOWN, SDLK_d): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_a): LEFT_DOWN,
    (SDL_KEYUP, SDLK_d): RIGHT_UP,
    (SDL_KEYUP, SDLK_a): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_LSHIFT): SHIFT
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
        elif event == DAMAGE:
            pass

    def exit(character, event):
        if event == SPACE:
            pass

    def do(character):
        pass

    def draw(character):
        cx, cy = character.x - server.stage.window_left, character.y - server.stage.window_bottom

        if character.dir == 1:
            character.image.clip_draw(420, 5 * 66, 64, 66, cx, cy)
        else:
            character.image.clip_draw(360, 5 * 66, 64, 66, cx, cy)


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
        character.dir = clamp(-1, character.velocity, 1)

    def exit(character, event):
        if event == SPACE:
            pass

    def do(character):
        character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3 + 1
        character.x += character.velocity * game_framework.frame_time
        character.x = clamp(25, character.x, 750 - 25)
        character.y = clamp(90, character.y, server.stage.h - 90)

    def draw(character):
        cx, cy = character.x - server.stage.window_left, character.y - server.stage.window_bottom

        if character.dir == 1:
            character.image.clip_draw(int(character.frame) * 60 + 480, 66 * 5, 64, 66, cx, cy)
        else:
            character.image.clip_draw(int(character.frame) * -60 + 300, 66 * 5, 64, 66, cx, cy)


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
        elif event == DAMAGE:
            pass

    def exit(character, event):
        if event == SPACE:
            pass

    def do(character):
        pass

    def draw(character):
        cx, cy = character.x - server.background.window_left, character.y - server.background.window_bottom

        if character.dir == 1:
            character.image.clip_draw(420, 3 * 66, 64, 66, cx, cy)
        else:
            character.image.clip_draw(360, 3 * 66, 64, 66, cx, cy)


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
        character.dir = clamp(-1, character.velocity, 1)

    def exit(character, event):
        if event == SPACE:
            pass

    def do(character):
        character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3 + 1
        character.x += character.velocity * game_framework.frame_time
        character.x = clamp(25, character.x, 750 - 25)
        character.y = clamp(90, character.y, server.background.h - 90)

    def draw(character):
        cx, cy = character.x - server.background.window_left, character.y - server.background.window_bottom

        if character.dir == 1:
            character.image.clip_draw(character.frame * 60 + 480, 66 * 5, 64, 66, cx, cy)
        else:
            character.image.clip_draw(character.frame * -60 + 300, 66 * 5, 64, 66, cx, cy)


next_state_table = {
    SmallIdleState: {RIGHT_UP: SmallRunState, LEFT_UP: SmallRunState, RIGHT_DOWN: SmallRunState, LEFT_DOWN: SmallRunState,
                     SPACE: SmallIdleState, SHIFT: SmallIdleState, MUSHROOM: BigIdleState, DAMAGE: SmallIdleState},
    SmallRunState: {RIGHT_UP: SmallIdleState, LEFT_UP: SmallIdleState, LEFT_DOWN: SmallIdleState, RIGHT_DOWN: SmallIdleState,
                    SPACE: SmallRunState, SHIFT: SmallRunState, MUSHROOM: BigRunState, DAMAGE: SmallIdleState},
    BigIdleState: {RIGHT_UP: BigRunState, LEFT_UP: BigRunState, RIGHT_DOWN: BigRunState, LEFT_DOWN: BigRunState,
                    SPACE: BigIdleState, SHIFT: BigIdleState, MUSHROOM: BigIdleState, DAMAGE: SmallIdleState},
    BigRunState: {RIGHT_UP: BigIdleState, LEFT_UP: BigIdleState, LEFT_DOWN: BigIdleState, RIGHT_DOWN: BigIdleState,
                    SPACE: BigRunState, SHIFT: BigRunState, MUSHROOM: BigRunState, DAMAGE: SmallRunState},
}

class Character:
    def __init__(self):
        self.image = load_image('smb_mario.png')
        self.x = 400
        self.y = 90
        self.j = -15
        self.frame = 0
        self.dir = 1
        self.velocity = 0
        self.event_que = []
        self.cur_state = SmallIdleState
        self.cur_state.enter(self, None)

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50


    def fire_ball(self):
        server.ball = Ball(self.x, self.y, self.dir * RUN_SPEED_PPS * 10)
        game_world.add_object(server.ball, 1)


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())
        #fill here

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

