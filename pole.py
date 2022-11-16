from pygame import *


class Pole:
    def __init__(self):
        self.kolizja = False
        self.body = Rect(0, 0, 64, 64)
        self.texture = Surface((64, 64)).convert_alpha()
        self.img = image.load('tileset.png')
        self.img = transform.scale2x(self.img)
        self.img.scroll(64, 64)

    def set(self, px, py, tile):
        self.texture.fill((0, 0, 0, 0))
        if tile == 0:
            self.kolizja = False
        elif tile == 1:
            self.texture.blit(self.img, (0, 0), (2 * 64, 2 * 64, 64, 64))
            self.kolizja = False
        elif tile == 2:
            self.texture.blit(self.img, (0, 0), (10 * 64, 2 * 64, 64, 64))
            self.kolizja = False
        elif tile == 3:
            self.texture.blit(self.img, (0, 0), (20 * 64, 4 * 64, 64, 64))
            self.kolizja = False
        elif tile == 4:
            self.texture.blit(self.img, (0, 0), (6 * 64, 2 * 64, 64, 64))
            self.kolizja = False
        elif tile == 5:
            self.texture.blit(self.img, (0, 0), (2 * 64, 6 * 64, 64, 64))
            self.kolizja = False
        elif tile == 11:
            self.texture.blit(self.img, (0, 0), (14 * 64, 15 * 64, 64, 64))
            self.kolizja = True
        elif tile == 12:
            self.texture.blit(self.img, (0, 0), (15 * 64, 15 * 64, 64, 64))
            self.kolizja = True
        elif tile == 13:
            self.texture.blit(self.img, (0, 0), (14 * 64, 16 * 64, 64, 64))
            self.kolizja = True
        elif tile == 14:
            self.texture.blit(self.img, (0, 0), (15 * 64, 16 * 64, 64, 64))
            self.kolizja = True
        elif tile == 15:
            self.texture.blit(self.img, (0, 0), (16 * 64, 14 * 64, 64, 64))
            self.kolizja = True
        elif tile == 16:
            self.texture.blit(self.img, (0, 0), (13 * 64, 14 * 64, 64, 64))
            self.kolizja = True
        elif tile == 17:
            self.texture.blit(self.img, (0, 0), (16 * 64, 16 * 64, 64, 64))
            self.kolizja = False
        elif tile == 18:
            self.texture.blit(self.img, (0, 0), (16 * 64, 15 * 64, 64, 64))
            self.kolizja = True
        elif tile == 19:
            self.texture.blit(self.img, (0, 0), (13 * 64, 16 * 64, 64, 64))
            self.kolizja = False
        elif tile == 20:
            self.texture.blit(self.img, (0, 0), (13 * 64, 15 * 64, 64, 64))
            self.kolizja = True
        elif tile == 90:
            self.texture.blit(self.img, (0, 0), (14 * 64, 11 * 64, 64, 64))
            self.kolizja = False
        elif tile == 91:
            self.texture.blit(self.img, (0, 0), (15 * 64, 11 * 64, 64, 64))
            self.kolizja = False
        elif tile == 92:
            self.texture.blit(self.img, (0, 0), (16 * 64, 11 * 64, 64, 64))
            self.kolizja = False
        elif tile == 93:
            self.texture.blit(self.img, (0, 0), (14 * 64, 12 * 64, 64, 64))
            self.kolizja = False
        elif tile == 94:
            self.texture.blit(self.img, (0, 0), (15 * 64, 12 * 64, 64, 64))
            self.kolizja = False
        elif tile == 95:
            self.texture.blit(self.img, (0, 0), (16 * 64, 12 * 64, 64, 64))
            self.kolizja = False
        self.body = Rect(px * 64, py * 64, 64, 64)
        self.texture.scroll(64, 64)
        return self.kolizja
