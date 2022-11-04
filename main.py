import mysql.connector
import pygame
import random
import sys

from pygame import *


class Pole:
    def __init__(self):
        self.kolizja = False
        self.body = Rect(0, 0, 64, 64)
        self.texture = Surface((64, 64))
        self.img = image.load('tileset.png')
        self.img = transform.scale2x(self.img)
        self.img.scroll(64, 64)

    def set(self, px, py, tile):
        if tile == 0:
            self.texture.blit(self.img, (0, 0), (2 * 64, 2 * 64, 64, 64))
        elif tile == 1:
            self.texture.blit(self.img, (0, 0), (2 * 64, 2 * 64, 64, 64))
        elif tile == 2:
            self.texture.blit(self.img, (0, 0), (20 * 64, 4 * 64, 64, 64))
        self.body = Rect(px * 64, py * 64, 64, 64)
        self.texture.scroll(64, 64)
        return self.kolizja


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

    def set(self):
        for i in range(10):
            for j in range(10):
                self.plansza.set(i, j, 0)
                self.map.blit(self.plansza.texture, self.plansza.body)
        for i in range(10):
            self.walls.append([])
            for j in range(10):
                self.walls[i].append(self.plansza.set(i, j, region[self.korx][self.kory][i][j]))
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
                self.walls = self.shadow.set()
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

    def __del__(self):
        print('pika')
        self.x = -1
        self.y = -1
        self.alife = False
        self.tick()

    def wild(self):
        self.texture = Surface((64, 64))
        self.texture.blit(image.load('pokemon.png'), (0, 0), (2 * 64, 0, 64, 64))
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


mydb = mysql.connector.connect(host="localhost", user="root", password="Mamatata1", port='3306', database='pokedex')
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM pokedex_poki")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

pygame.init()
pygame.display.set_caption('Polslmon')
pygame.display.set_icon(image.load('icon.png'))
onmap = True
hero = Postac()
pokemon = Postac()
pokemon.wild()
klocki = []
hud = image.load('hud.png')


region = []
regionbg = []
for i in range(17):
    region.append([])
    regionbg.append([])
    for j in range(11):
        region[i].append([])
        regionbg[i].append(0)
        for k in range(10):
            region[i][j].append([])
            for l in range(10):
                region[i][j][k].append(1)
                if i == k or j == l:
                    region[i][j][k][l] = 0
                if i == 9 and j == 5:
                    region[i][j][k][l] = 2


mapbg = Surface((576, 576))
for i in range(10):
    klocki.append([])
    for j in range(10):
        klocki[i].append(Pole())
        klocki[i][j].set(i, j, 0)

plansza = Mapa()
wall = plansza.set()

TICK = pygame.USEREVENT + 1
time.set_timer(TICK, 1000)

screen = display.set_mode((768, 576))
screen.blit(hud, (576, 0, 192, 768))
mapscreen = Surface((576, 576))

fightscreen = Surface((576, 576)).convert_alpha()
liczi = 0
initialfight = True
fightbg = transform.scale(image.load('fightbg.png'), (576, 576))
fightpokemon = transform.scale(image.load('chi.png').convert_alpha(), (512, 512))

timer = 0

while 1:
    pygame.time.Clock().tick(60)
    if onmap:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == TICK:
                pokemon.idle([
                    wall[pokemon.x][pokemon.y-1],
                    wall[pokemon.x][pokemon.y+1],
                    wall[pokemon.x-1][pokemon.y],
                    wall[pokemon.x][pokemon.y+1]])

        if timer == 0:
            timer = 20
            if pygame.key.get_pressed()[K_w]:
                plansza.move(hero.move(0, wall[int(hero.x)][int(hero.y) - 1], hero.y == 0), 0, 0)
            elif pygame.key.get_pressed()[K_s]:
                plansza.move(hero.move(1, wall[int(hero.x)][int(hero.y) + 1], hero.y == 8), 1, 0)
            elif pygame.key.get_pressed()[K_a]:
                plansza.move(hero.move(2, wall[int(hero.x) - 1][int(hero.y)], hero.x == 0), 2, 0)
            elif pygame.key.get_pressed()[K_d]:
                plansza.move(hero.move(3, wall[int(hero.x) + 1][int(hero.y)], hero.x == 8), 3, 0)
            else:
                timer = 0
        else:
            timer -= 1

        hero.tick()
        plansza.tick()
        onmap = pokemon.poketick(hero.x, hero.y)
        mapscreen.blit(plansza.map, (plansza.x, plansza.y, 576, 576))
        if plansza.timer > 0:
            mapscreen.blit(plansza.shadow.map, (plansza.shadow.x, plansza.shadow.y, 576, 576))
            pokemon.wild()
        else:
            mapscreen.blit(pokemon.texture, pokemon.body)
        mapscreen.blit(hero.texture, hero.body)
        screen.blit(mapscreen, (0, 0, 576, 576))

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if initialfight:
            pygame.time.Clock().tick(30)
            fightscreen.fill((0, 0, 0, 0))
            for i in range(liczi):
                for j in range(liczi):
                    draw.rect(fightscreen, (0, 0, 0), klocki[i][j].body)
            if liczi < 9:
                liczi += 1
            else:
                initialfight = False
        else:
            if pygame.key.get_pressed()[K_SPACE]:
                onmap = True
                initialfight = True
                liczi = 0
            fightscreen.blit(fightbg, (0, 0, 576, 576))
            fightscreen.blit(fightpokemon, (32, 32, 512, 512))
        screen.blit(fightscreen, (0, 0, 576, 576))
    display.flip()
