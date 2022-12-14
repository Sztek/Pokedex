import random
import mysql.connector
from pygame import *


class Postac:
    def __init__(self):
        self.x = 4
        self.y = 4
        self.dx = 0
        self.dy = 0
        self.timer = 0
        self.body = Rect(self.x * 64, self.y * 64, 64, 64)
        self.texture = image.load('gracz.png')
        self.alife = True
        self.img = image.load('pokeset.png')

    def catch(self, trener, pokeid):
        self.x = -1
        self.y = -1
        self.alife = False
        self.tick()
        mydb = mysql.connector.connect(host="localhost",user="root",password="Mamatata1",port='3306',database='pokedex')
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM pokedex_poki WHERE id="+str(pokeid))
        myresult = mycursor.fetchall()
        print(myresult[0])
        mycursor = mydb.cursor()
        sql = "INSERT INTO pokemony (nazwa, iv, wlasciciel, zdrowie, poziom) VALUES (%s, %s, %s, %s, %s)"
        val = (myresult[0][1], random.randrange(5)+1, trener, 100, 1)
        mycursor.execute(sql, val)
        mydb.commit()

    def wild(self, pokeid):
        self.texture = Surface((64, 64)).convert_alpha()
        self.texture.fill((0, 0, 0, 0))
        self.texture.blit(self.img, (0, 0), (pokeid * 64, 0, 64, 64))
        self.x = 3
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

    def poketick(self, px, py, trener, pokeid):
        if self.alife:
            self.tick()
            if self.x == px and self.y == py:
                self.catch(trener, pokeid)
                return False
        return True

    def idle(self, kolizje):
        kierunek = random.randrange(4)
        if not (kierunek == 0 and self.y == 0):
            if not (kierunek == 1 and self.y == 8):
                if not (kierunek == 2 and self.x == 0):
                    if not (kierunek == 3 and self.x == 8):
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
