import sys
import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, init_x, init_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('/home/student/Documents/python_insights/pygame/fuppybirb/assets/background.png')
        self.image = pygame.transform.scale(self.image, (1528, 750))
        self.rect = self.image.get_rect()
        self.rect.x = init_x
        self.rect.y = init_y
        self.dx = -1

    def update(self):
        self.rect.x += self.dx

    def get_rect(self):
        return self.rect
