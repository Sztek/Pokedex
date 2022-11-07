import random
from pygame import *


class Postac:
    def __init__(self):
        self.x = 4
        self.y = 4
        self.dx = 0
        self.dy = 0
        self.timer = 0
        self.body = Rect(self.x * 64, self.y * 64, 64, 64)
        self.texture = image.load('ele.png')
        self.alife = True
        self.img = image.load('pokemon.png')

    def __del__(self):
        print('pika')
        self.x = -1
        self.y = -1
        self.alife = False
        self.tick()

    def wild(self):
        self.texture = Surface((64, 64)).convert_alpha()
        self.texture.fill((0, 0, 0, 0))
        self.texture.blit(self.img, (0, 0), (2 * 64, 0, 64, 64))
        #self.texture = image.load('chi.png')
        self.x = 2
        self.y = 2
        self.alife = True

    def tick(self):
        self.body = Rect(self.x * 64, self.y * 64, 64, 64)
        if self.timer:
            self.timer -= 1
            self.x += self.dx
            self.y += self.dy
            if not self.timer:
                self.x = round(self.x)
                self.y = round(self.y)
        else:
            self.dx = 0
            self.dy = 0

    def poketick(self, px, py):
        if self.alife:
            self.tick()
            if self.x == px and self.y == py:
                self.__del__()
                return False
        return True

    def idle(self, kolizje):
        kierunek = random.randrange(4)
        self.move(kierunek, kolizje[kierunek], False)

    def move(self, kierunek, kolizja, onedge):
        scale = 1
        if onedge:
            scale = -8
        if not self.timer and not self.dx and not self.dy and (not kolizja or onedge):
            self.timer = 20
            if kierunek == 0:
                self.dy = -0.05 * scale
            elif kierunek == 1:
                self.dy = 0.05 * scale
            elif kierunek == 2:
                self.dx = -0.05 * scale
            elif kierunek == 3:
                self.dx = 0.05 * scale
        return onedge
