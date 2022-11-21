import mysql.connector
import pygame
import sys
import random
from mapa import Mapa
from postac import Postac
from menu import Menu
from pygame import *


mydb = mysql.connector.connect(host="localhost", user="root", password="Mamatata1", port='3306', database='pokedex')
pygame.init()
pygame.display.set_caption('Polslmon')
pygame.display.set_icon(image.load('icon.png'))
screen = display.set_mode((768, 576))
screen.blit(image.load('loading.png'), (0, 0), (0, 0, 768, 576))
display.flip()
time.Clock().tick(0)
onmap = True
pause = False
hero = Postac()
pokemon = Postac()
lista = mydb.cursor()
lista.execute("SELECT id, nazwa FROM pokedex_poki WHERE typ='normalny' OR typ='latajacy'")
lista = lista.fetchall()
los = random.randrange(len(lista))
print('Wild ', lista[los][1], ' appear')
pokeid = lista[los][0]
pokemon.wild(lista[los][0]-1)
setpokemon = False
klocki = []
hudimg = image.load('hud.png')
hud = Surface((192, 768))
hud.blit(hudimg, (0, 0, 192, 768))
znacznik = Surface((8, 8)).convert_alpha()
znacznik.fill((255, 255, 255, 8))
draw.rect(znacznik, (255, 255, 255), (0, 0, 2, 8))
draw.rect(znacznik, (255, 255, 255), (0, 0, 8, 2))
draw.rect(znacznik, (255, 255, 255), (6, 0, 2, 8))
draw.rect(znacznik, (255, 255, 255), (0, 6, 8, 2))

region = []
regionbg = []
for i in range(12):
    region.append([])
    regionbg.append([])
    for j in range(12):
        region[i].append([])
        regionbg[i].append(1)
        if j < 2:
            regionbg[i][j] = 2#gory
        if j > 8:
            regionbg[i][j] = 4#piasek
        if i < 3:
            regionbg[i][j] = 1#laka
        if i > 9:
            regionbg[i][j] = 5#zima
        if j > 10:
            regionbg[i][j] = 3#woda
        if i < 1:
            regionbg[i][j] = 6#dom
        if i == 6 and j == 5:
            regionbg[i][j] = 3
        for k in range(10):
            region[i][j].append([])
            for l in range(10):
                region[i][j][k].append(0)
                if 0 < i < 3 and 2 < j < 9:
                    region[i][j][k][l] = 90 + random.randrange(10)  #kwiatki
                if ((i==1 or i==10 or i==4) and k==0 and not (j==5 and 2<l<6)) or (i==6 and k==2 and (j==2 or j==8)):
                    region[i][j][k][l] = 15     #drzewo lewo
                if ((i== 11 or i==2 or i==8) and k==8 and not (not i==11 and j==5 and 2<l<6)) or (i==6 and k==6 and (j==2 or j==8)):
                    region[i][j][k][l] = 16     #drzewo prawo
                if (j == 3 or j == 0 or j==9) and l == 1 and not (not j == 0 and i == 6 and 2 < k < 6):
                    region[i][j][k][l-1] = 11 + (k % 2)
                    region[i][j][k][l] = 13 + (k % 2)   #drzewo dol
                    if i == 6 and k>4:
                        region[i][j][k][l - 1] = 11 + abs(1- k % 2)
                        region[i][j][k][l] = 13 + abs(1- k % 2)  # drzewo dol
                if i==6 and (j==3 or j==9) and k==6 and l==1:
                    region[i][j][k-4][l - 1] = 18
                    region[i][j][k-4][l] = 17
                    region[i][j][k][l-1] = 20
                    region[i][j][k][l] = 19
                if i == 6 and j == 4 and l == 8:
                    region[i][j][k][l] = 3
                if i == 5 and j == 5 and k == 8:
                    region[i][j][k][l] = 3
                if i == 7 and j == 5 and k == 0:
                    region[i][j][k][l] = 3
                if i == 6 and j == 6 and l == 0:
                    region[i][j][k][l] = 3

mapbg = Surface((576, 576))

menu = Menu()
plansza = Mapa()
wall = plansza.set(region, regionbg)

TICK = pygame.USEREVENT + 1
time.set_timer(TICK, 1000)

mapscreen = Surface((576, 576))

fightscreen = Surface((576, 576)).convert_alpha()
liczi = 0
liczj = 0
liczk = 0
initialfight = True
fightbg = transform.scale(image.load('fightbg.png'), (576, 576))
hud.blit(hudimg, (0, 0, 192, 768))
hud.blit(znacznik, (44 + 8 * plansza.korx, 44 + 8 * plansza.kory, 8, 8))
screen.blit(hud, (576, 0, 192, 768))
timer = 0
trener = 'gracz'

while 1:
    pygame.time.Clock().tick(60)
    if pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(menu.okno, (32, 32, 512, 512))
        if mouse.get_pressed()[0] and mouse.get_pos()[0] < 600:
            pause = False
        if menu.isdex:
            menu.dextick(mouse.get_pos()[1])
    else:
        if mouse.get_pressed()[0] and mouse.get_pos()[0] > 600 and mouse.get_pos()[1] > 430:
            pause = True
            menu.gracze()
        elif mouse.get_pressed()[0] and mouse.get_pos()[0] > 600 and mouse.get_pos()[1] > 285:
            pause = True
            menu.pokemony()
        elif mouse.get_pressed()[0] and mouse.get_pos()[0] > 600 and mouse.get_pos()[1] > 160:
            pause = True
            menu.pokedex()

        if onmap:
            wall = plansza.walls
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
            if not plansza.timer:
                onmap = pokemon.poketick(hero.x, hero.y, trener, pokeid)
            else:
                time.set_timer(TICK, 1000)
            mapscreen.blit(plansza.map, (plansza.x, plansza.y, 576, 576))
            if plansza.timer > 0:
                mapscreen.blit(plansza.shadow.map, (plansza.shadow.x, plansza.shadow.y, 576, 576))
                if setpokemon:
                    lista = mydb.cursor()
                    if regionbg[plansza.korx][plansza.kory] == 1:
                        lista.execute("SELECT id, nazwa FROM pokedex_poki WHERE typ='normalny' OR typ='latajacy'")
                    elif regionbg[plansza.korx][plansza.kory] == 2:
                        lista.execute("SELECT id, nazwa FROM pokedex_poki WHERE typ='ziemia' OR typ='ogien'")
                    elif regionbg[plansza.korx][plansza.kory] == 3:
                        lista.execute("SELECT id, nazwa FROM pokedex_poki WHERE typ='woda' OR typ='latajacy'")
                    elif regionbg[plansza.korx][plansza.kory] == 4:
                        lista.execute("SELECT id, nazwa FROM pokedex_poki WHERE typ='woda' OR typ='ogien'")
                    elif regionbg[plansza.korx][plansza.kory] == 5:
                        lista.execute("SELECT id, nazwa FROM pokedex_poki WHERE typ='legendarny' OR typ='lod'")
                    elif regionbg[plansza.korx][plansza.kory] == 6:
                        lista.execute("SELECT id, nazwa FROM pokedex_poki WHERE typ='legendarny'")
                    lista = lista.fetchall()
                    los = random.randrange(len(lista))
                    print('Wild ', lista[los][1], ' appear')
                    pokeid = lista[los][0]
                    pokemon.wild(lista[los][0]-1)
                    setpokemon = False
                    hud.blit(hudimg, (0, 0, 192, 768))
                    hud.blit(znacznik, (44 + 8 * plansza.korx, 44 + 8 * plansza.kory, 8, 8))
                    screen.blit(hud, (576, 0, 192, 768))
            else:
                mapscreen.blit(pokemon.texture, pokemon.body)
                setpokemon = True
            mapscreen.blit(hero.texture, hero.body)
            screen.blit(mapscreen, (0, 0, 576, 576))

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            if initialfight:
                pygame.time.Clock().tick(120)
                fightscreen.fill((0, 0, 0, 0))
                draw.rect(fightscreen, (0, 0, 0), (liczi*64, liczj*64, 64, 64))
                if liczk == 6:
                    initialfight = False
                if liczi < 8-liczk and liczj == 0+liczk:
                    liczi += 1
                elif liczi == 8-liczk and liczj < 8-liczk:
                    liczj += 1
                elif liczj == 8-liczk and liczi > 0+liczk:
                    liczi -= 1
                elif liczi == 0+liczk and liczj > 1+liczk:
                    liczj -= 1
                else:
                    liczk += 1
            else:
                if pygame.key.get_pressed()[K_SPACE]:
                    onmap = True
                    initialfight = True
                    liczi = 0
                    liczj = 0
                    liczk = 0
                fightscreen.blit(fightbg, (0, 0, 576, 576))
                fightscreen.blit(transform.scale(pokemon.texture, (512, 512)), (32, 32, 512, 512))
            screen.blit(fightscreen, (0, 0, 576, 576))
    display.flip()
