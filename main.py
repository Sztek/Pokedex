import sys, pygame, random
from pygame import *


class Pole:
    def __init__(self):
        self.kolizja = False
        self.body = Rect(0, 0, 64, 64)
        self.texture = 0

    def set(self, x, y, tile):
        sizex = (64, 64)
        self.texture = Surface(sizex)
        img = image.load('Tile-SpringGround.png')
        img = transform.scale(img, (160*4, 112*4))
        img.scroll(64, 64)
        if tile == 0:
            self.texture.blit(img, (0, 0), (512, 128, 64, 64))
        else:
            self.texture.blit(img, (0, 0), (128, 128, 64, 64))
        self.body = Rect(x * 64, y * 64, 64, 64)
        self.texture.scroll(64, 64)


class Postac:
    def __init__(self):
        self.x = 4
        self.y = 4
        self.dx = 0
        self.dy = 0
        self.timer = 0
        self.body = Rect(self.x*64, self.y*64, 64, 64)
        self.texture = image.load('ele.png')

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

    def move(self, kierunek, kolizja):
        if not self.timer and not self.dx and not self.dy and not kolizja:
            self.timer = 20
            if kierunek == 0:
                self.dy = -0.05
            elif kierunek == 1:
                self.dy = 0.05
            elif kierunek == 2:
                self.dx = -0.05
            elif kierunek == 3:
                self.dx = 0.05


pygame.init()
size = width, height = 768, 576
black = 0, 0, 0
hero = Postac()
plansza = []
hud = image.load('hud.png')

for i in range(9):
    plansza.append([])
    for j in range(9):
        plansza[i].append(Pole())
        plansza[i][j].set(i, j, random.randrange(7))
        if i == 0 or j == 0 or i == 8 or j == 8:
            plansza[i][j].kolizja = True

screen = display.set_mode(size)

while 1:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if pygame.key.get_pressed()[K_w]:
        hero.move(0, plansza[int(hero.x)][int(hero.y)-1].kolizja)
    elif pygame.key.get_pressed()[K_s]:
        hero.move(1, plansza[int(hero.x)][int(hero.y)+1].kolizja)
    elif pygame.key.get_pressed()[K_a]:
        hero.move(2, plansza[int(hero.x)-1][int(hero.y)].kolizja)
    elif pygame.key.get_pressed()[K_d]:
        hero.move(3, plansza[int(hero.x)+1][int(hero.y)].kolizja)

    hero.tick()
    screen.fill(black)
    for i in range(9):
        for j in range(9):
            #draw.rect(screen, Color(50+j*20, 150, 50+i*20), plansza[i][j].body)
            screen.blit(plansza[i][j].texture, plansza[i][j].body)
    screen.blit(hero.texture, hero.body)
    screen.blit(hud, (576, 0, 192, 768))
    display.flip()
