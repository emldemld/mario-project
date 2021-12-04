from pico2d import *

class Stage:
    def __init__(self): #생성자
        self.image = load_image('bg-1-1.png')
    def draw(self):
        self.image.draw(0, -15)