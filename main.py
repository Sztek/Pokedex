import mysql.connector
import pygame
import random
import sys
from pole import Pole
from mapa import Mapa
from postac import Postac
from pygame import *


screen = display.set_mode((768, 576))
screen.blit(image.load('loading.png'), (0, 0), (0, 0, 768, 576))
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

screen.blit(image.load('loading.png'), (0, 0), (0, 0, 768, 576))
mapbg = Surface((576, 576))


plansza = Mapa()
wall = plansza.set(region)

TICK = pygame.USEREVENT + 1
time.set_timer(TICK, 1000)


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
            #for i in range(liczi):
             #   for j in range(liczi):
              #      draw.rect(fightscreen, (0, 0, 0), klocki[i][j].body)
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
