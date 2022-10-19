import sys, pygame
from pygame import *


class Pole:
    def __init__(self):
        self.kolizja = False
        self.body = Rect(0, 0, 64, 64)

    def set(self, x, y):
        self.body = Rect(i*64, j*64, 64, 64)


class Postac:
    def __init__(self):
        self.body = Rect(4*64+8, 4*64, 48, 64)


pygame.init()
size = width, height = 768, 576
black = 0, 0, 0
hero = Postac()
plansza = []
hud = image.load('hud.png')
for i in range(12):
    plansza.append([])
    for j in range(9):
        plansza[i].append(Pole())
        plansza[i][j].set(i, j)

print(plansza[0])
screen = display.set_mode(size)

while 1:
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)
    for i in range(9):
        for j in range(9):
            draw.rect(screen, Color(50+j*20, 150, 50+i*20), plansza[i][j].body)
    draw.rect(screen, Color(255, 255, 255), hero.body)
    screen.blit(hud, (576, 0, 192, 768))
    display.flip()
