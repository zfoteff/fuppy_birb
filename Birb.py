import sys
import pygame

class Birb(pygame.sprite.Sprite):
    def __init__(self, init_x, init_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('/home/student/Documents/python_insights/pygame/fuppybirb/assets/birb.png')
        self.image = pygame.transform.scale(self.image, (125, 125))
        self.rect = self.image.get_rect()
        self.rect.x = init_x
        self.rect.y = init_y
        self.dx = 4
        self.dy = 3
        self.alive = True
        self.godmode = False

    def update(self):
        if self.godmode:
            self.rect.x += self.dx
            self.rect.y += self.dy

        elif not self.godmode:
            self.rect.y += self.dy
            self.dy += 1.55

            if self.dy > 9:
                self.dy = 9

    def get_rect(self):
        return self.rect

    """
    Sets dy as + which will slowly decrease in the update function
    Creates a smooth curve for the bird to follow while it jumps
    """
    def jump(self):
        self.dy = -20.0

    def go_up(self):
        self.dy = -3

    def go_down(self):
        self.dy = 3

    def go_right(self):
        self.dx = 3

    def go_left(self):
        if self.godmode:
            self.dx = -3

    def die(self):
        if self.godmode:
            self.dy = 30

    def set_godmode(self):
        self.dx = 0
        self.dy = 0
        self.godmode = True

    def stop(self):
        if self.godmode:
            self.dx = 0
            self.dy = 0
