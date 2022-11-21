from pygame import *
import mysql.connector


class Menu:
    def __init__(self):
        self.font = font.Font('arial.ttf', 12)
        self.okno = Surface((512, 512))
        self.okno.fill((255, 255, 255))
        self.isdex = False
        self.skok = 16
        self.img = image.load('pokeset.png')
        self.texture = Surface((64, 64)).convert_alpha()
        self.texture.fill((0, 0, 0, 0))

    def pokedex(self):
        self.isdex = True
        self.okno.fill((255, 255, 255))
        mydb = mysql.connector.connect(host="localhost", user="root", password="Mamatata1", port='3306', database='pokedex')
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM pokedex_poki")
        myresult = mycursor.fetchall()
        i=0
        for x in myresult:
            tekst = ''
            for j in range(7):
                tekst+=str(x[j])
                tekst += ' '
            text = self.font.render(tekst, True, (0, 0, 0), (255, 255, 255))
            self.okno.blit(text, (0,i*self.skok,0,0))
            i+=1

    def pokemony(self):
        self.isdex = False
        self.okno.fill((255, 255, 255))
        mydb = mysql.connector.connect(host="localhost", user="root", password="Mamatata1", port='3306', database='pokedex')
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM pokemony")
        myresult = mycursor.fetchall()
        i=0
        for x in myresult:
            tekst = ''
            for j in range(6):
                tekst+=str(x[j])
                tekst += ' '
            text = self.font.render(tekst, True, (0, 0, 0), (255, 255, 255))
            self.okno.blit(text, (0,i*self.skok,0,0))
            i+=1

    def gracze(self):
        self.isdex = False
        self.okno.fill((255, 255, 255))
        mydb = mysql.connector.connect(host="localhost", user="root", password="Mamatata1", port='3306', database='pokedex')
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM trenerzy")
        myresult = mycursor.fetchall()
        i=0
        for x in myresult:
            tekst = ''
            for j in range(6):
                tekst+=str(x[j])
                tekst += ' '
            text = self.font.render(tekst, True, (0, 0, 0), (255, 255, 255))
            self.okno.blit(text, (0,i*self.skok,0,0))
            i+=1

    def dextick(self, poz):
        self.texture.fill((255, 255, 255))
        poz -= 32
        poz /= self.skok
        if 1 <= poz <= 30:
            self.texture.blit(self.img, (0, 0), (round(poz) * 64, 0, 64, 64))
            self.okno.blit(transform.scale2x(self.texture),(256,0,64,64))

