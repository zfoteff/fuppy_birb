import sys
import pygame as py

class Pipe(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = py.image.load('assets/pipe.png')
        self.rect = py.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
