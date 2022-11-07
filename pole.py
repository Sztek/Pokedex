from pygame import *


class Pole:
    def __init__(self):
        self.kolizja = False
        self.body = Rect(0, 0, 64, 64)
        self.texture = Surface((64, 64))
        print(1)
        self.img = image.load('tileset.png')
        self.img = transform.scale2x(self.img)
        self.img.scroll(64, 64)
        print(2)

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
