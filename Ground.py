import sys
import pygame as pg

class Ground(pg.sprite.Sprite):
    def __init__(self, init_x, init_y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('/home/student/Documents/python_insights/pygame/fuppybirb/assets/ground.png')
        self.image = pg.transform.scale(self.image, (650, 70))
        self.rect = self.image.get_rect()
        self.rect.x = init_x
        self.rect.y = init_y
        self.dx = -3

    def update(self):
        self.rect.x += self.dx

    def get_rect(self):
        return self.rect
