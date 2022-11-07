from pole import Pole
from pygame import *


class Mapa:
    def __init__(self):
        self.plansza = Pole()
        self.walls = []
        self.map = Surface((576, 576))
        self.dx = 0
        self.dy = 0
        self.x = 0
        self.y = 0
        self.timer = 0
        self.shadow = None
        self.isshadow = True
        self.korx = 9
        self.kory = 4
        self.region = []

    def set(self, region):
        self.region = region
        for i in range(10):
            for j in range(10):
                self.plansza.set(i, j, 0)
                self.map.blit(self.plansza.texture, self.plansza.body)
        for i in range(10):
            self.walls.append([])
            for j in range(10):
                self.walls[i].append(self.plansza.set(i, j, self.region[self.korx][self.kory][i][j]))
                self.map.blit(self.plansza.texture, self.plansza.body)
                if i == 9 or j == 9:
                    self.walls[i][j] = True
        return self.walls

    def move(self, go, kierunek, isshadow):
        if go:
            self.isshadow = isshadow
            if not isshadow:
                if kierunek == 0:
                    self.kory -= 1
                elif kierunek == 1:
                    self.kory += 1
                elif kierunek == 2:
                    self.korx -= 1
                elif kierunek == 3:
                    self.korx += 1
                self.shadow = Mapa()
                self.shadow.kory = self.kory
                self.shadow.korx = self.korx
                self.walls = self.shadow.set(self.region)
                self.shadow.move(go, kierunek, 1)
                if kierunek == 0:
                    self.shadow.x = 0
                    self.shadow.y = -576
                elif kierunek == 1:
                    self.shadow.x = 0
                    self.shadow.y = 576
                elif kierunek == 2:
                    self.shadow.x = -576
                    self.shadow.y = 0
                elif kierunek == 3:
                    self.shadow.x = 576
                    self.shadow.y = 0
            self.timer = 20
            if kierunek == 0:
                self.dy = 28.8
            elif kierunek == 1:
                self.dy = -28.8
            elif kierunek == 2:
                self.dx = 28.8
            elif kierunek == 3:
                self.dx = -28.8

    def tick(self):
        if not self.isshadow:
            self.shadow.tick()
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
            self.x = 0
            self.y = 0
            if not self.isshadow:
                self.map = self.shadow.map
