import random
import game_framework
from BT import BehaviorTree, SelectorNode, SequenceNode, LeafNode
from pico2d import *

import server

# zombie Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10


class Enemy:

    def __init__(self):
        self.x, self.y = random.randint(500, 6500), 95
        self.cx, self.cy = self.x, self.y
        self.image = load_image('enemies.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = random.random() % 3 - 1
        self.speed = 0
        self.timer = 2.0  # change direction every 1 sec when wandering
        self.wait_timer = 2.0
        self.frame = 0
        self.build_behavior_tree()



    def wander(self):
        self.speed = RUN_SPEED_PPS
        self.timer -= game_framework.frame_time
        if self.timer <= 0:
            self.timer = 5.0
            self.dir = -self.dir
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING


    def wait(self):
        self.speed = 0
        self.wait_timer -= game_framework.frame_time
        if self.wait_timer <= 0:
            self.wait_timer = 2.0
            return BehaviorTree.SUCCESS
        return BehaviorTree.RUNNING



    def find_player(self):
        distance = server.character.cx - self.cx ** 2
        if distance < (PIXEL_PER_METER / 100) ** 2:
            return BehaviorTree.SUCCESS
        else:
            self.speed = 0
            return BehaviorTree.FAIL


    def move_to_player(self):
        self.speed = RUN_SPEED_PPS
        if server.character.x - self.x >= 0:
            self.dir = 1
        else:
            self.dir = -1
        return BehaviorTree.SUCCESS


    def build_behavior_tree(self):
        wander_node = LeafNode("Wander", self.wander)
        find_player_node = LeafNode("Find Player", self.find_player)
        move_to_player_node = LeafNode("Move to Player", self.move_to_player)
        chase_node = SequenceNode("Chase")
        chase_node.add_children(find_player_node, move_to_player_node)
        wander_chase_node = SelectorNode("WanderChase")
        wander_chase_node.add_children(wander_node, chase_node)
        self.bt = BehaviorTree(wander_chase_node)




    def get_bb(self):
        return self.cx - 25, self.y - 25, self.cx + 25, self.y + 25

    def update(self):
        self.cx = self.x - server.stage.window_left
        self.bt.run()
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        self.x += self.speed * self.dir * game_framework.frame_time


    def draw(self):
        if self.dir != 0:
            self.image.clip_draw(int(self.frame) * 60, 480, 60, 60, self.cx, self.y)
        else:
            self.image.clip_draw(120, 480, 60, 60, self.cx, self.y - 10)
        draw_rectangle(*self.get_bb())
        #self.font.draw(cx - 60, self.y + 50, '(x: %3.2f)' % cx, (255, 255, 0))
        #self.font.draw(cx - 60, self.y + 75, '(cx: %3.2f)' % cx, (255, 255, 0))

    def handle_event(self, event):
        pass

