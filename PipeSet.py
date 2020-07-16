import sys
import pygame

class PipeSet(pygame.sprite.Sprite):
    def __init__(self, pipe_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('/home/student/Documents/python_insights/pygame/fuppybirb/assets/pipeset.png')
        self.image = pygame.transform.scale(self.image, (115, 1050))
        self.rect = self.image.get_rect()
        self.rect.x = 650
        self.rect.y = pipe_pos
        self.dx = -3

    def update(self):
        self.rect.x += self.dx

        if self.rect.left < -135:
            self.kill()

    def get_rect():
        return self.rect
