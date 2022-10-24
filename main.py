import mysql.connector
import pygame
import random
import sys

from pygame import *


class Pole:
    def __init__(self):
        self.kolizja = False
        self.body = Rect(0, 0, 64, 64)
        self.texture = 0

    def set(self, px, py, tile):
        sizex = (64, 64)
        self.texture = Surface(sizex)
        img = image.load('Tile-SpringGround.png')
        img = transform.scale(img, (160 * 4, 112 * 4))
        img.scroll(64, 64)
        if tile == 0:
            self.texture.blit(img, (0, 0), (512, 128, 64, 64))
        else:
            self.texture.blit(img, (0, 0), (128, 128, 64, 64))
        self.body = Rect(px * 64, py * 64, 64, 64)
        self.texture.scroll(64, 64)


class Postac:
    def __init__(self):
        self.x = 4
        self.y = 4
        self.dx = 0
        self.dy = 0
        self.timer = 0
        self.body = Rect(self.x * 64, self.y * 64, 64, 64)
        self.texture = image.load('ele.png')

    def __del__(self):
        print('pika')

    def wild(self):
        self.texture = image.load('bat.png')
        self.x = 2
        self.y = 2

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
        self.tick()
        if self.x == px and self.y == py:
            self.__del__()
            return False
        return True

    def idle(self, kolizje):
        kierunek = random.randrange(4)
        self.move(kierunek, kolizje[kierunek])

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


mydb = mysql.connector.connect(host="localhost", user="root", password="Mamatata1", port='3306', database='pokedex')
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM pokedex_poki")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

pygame.init()
onmap = True
black = 0, 0, 0
hero = Postac()
pokemon = Postac()
pokemon.wild()
plansza = []
hud = image.load('hud.png')
fightbg = image.load('fightbg.png')

for i in range(9):
    plansza.append([])
    for j in range(9):
        plansza[i].append(Pole())
        plansza[i][j].set(i, j, random.randrange(7))
        if i == 0 or j == 0 or i == 8 or j == 8:
            plansza[i][j].kolizja = True

TICK = pygame.USEREVENT + 1
time.set_timer(TICK, 1000)

screen = display.set_mode((768, 576))
mapscreen = Surface((576, 576))
fightscreen = Surface((576, 576))
fightscreen = fightscreen.convert_alpha()
liczi = 0
liczj = 0
initialfight = True

while 1:
    pygame.time.Clock().tick(60)
    if onmap:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == TICK:
                pokemon.idle([
                    plansza[pokemon.x][pokemon.y-1].kolizja,
                    plansza[pokemon.x][pokemon.y+1].kolizja,
                    plansza[pokemon.x-1][pokemon.y].kolizja,
                    plansza[pokemon.x][pokemon.y+1].kolizja])

        if pygame.key.get_pressed()[K_w]:
            hero.move(0, plansza[int(hero.x)][int(hero.y) - 1].kolizja)
        elif pygame.key.get_pressed()[K_s]:
            hero.move(1, plansza[int(hero.x)][int(hero.y) + 1].kolizja)
        elif pygame.key.get_pressed()[K_a]:
            hero.move(2, plansza[int(hero.x) - 1][int(hero.y)].kolizja)
        elif pygame.key.get_pressed()[K_d]:
            hero.move(3, plansza[int(hero.x) + 1][int(hero.y)].kolizja)

        hero.tick()
        onmap = pokemon.poketick(hero.x, hero.y)
        mapscreen.fill(black)
        for i in range(9):
            for j in range(9):
                # draw.rect(screen, Color(50+j*20, 150, 50+i*20), plansza[i][j].body)
                mapscreen.blit(plansza[i][j].texture, plansza[i][j].body)
        mapscreen.blit(hero.texture, hero.body)
        mapscreen.blit(pokemon.texture, pokemon.body)
        screen.blit(mapscreen, (0, 0, 576, 576))
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if pygame.key.get_pressed()[K_SPACE]:
            onmap = True
        if initialfight:
            pygame.time.Clock().tick(30)
            fightscreen.fill((0, 0, 0, 0))
            for i in range(liczi):
                for j in range(liczj):
                    draw.rect(fightscreen, (0, 0, 0), plansza[i][j].body)
            if liczi < 9:
                liczi += 1
                liczj += 1
            else:
                initialfight = False
        else:
            fightscreen.blit(fightbg, (0, 0, 576, 576))
        screen.blit(fightscreen, (0, 0, 576, 576))
    screen.blit(hud, (576, 0, 192, 768))
    display.flip()
