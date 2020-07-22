import sys
import pygame

class Birb(pygame.sprite.Sprite):
    def __init__(self, init_x=200, init_y=250):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/birb.png')
        self.image = pygame.transform.scale(self.image, (125, 125))
        self.rect = self.image.get_rect()
        self.rect.x = init_x
        self.rect.y = init_y
        self.dx = 4
        self.dy = 3
        self.alive = True
        self._godmode = False

    def update(self):
        if self._godmode:
            self.rect.x += self.dx
            self.rect.y += self.dy

        else:
            self.rect.y += self.dy
            self.dy += 1.55

            if self.dy > 9:
                self.dy = 9

            if not self.alive and (self.rect.y >= 830 or self.rect.y < -130):
                self.kill()


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
        if self._godmode:
            self.dx = 3

    def go_left(self):
        if self._godmode:
            self.dx = -3

    def stop(self):
        if self._godmode:
            self.dx = 0
            self.dy = 0

    def die(self):
        if not self._godmode:
            self.alive = False
            self.dy = 15

    def _set_godmode(self):
        self.dx = 0
        self.dy = 0
        self._godmode = True

    def _set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y


class Logo(pygame.sprite.Sprite):
    def __init__ (self, init_x=360, init_y=200):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/logo.png')
        self.image = pygame.transform.scale(self.image, (215, 235))
        self.rect = self.image.get_rect()
        self.rect.x = init_x
        self.rect.y = init_y
        self.dy = 5

    def update (self):
        self.rect.y += self.dy

        if self.rect.y > 240 or self.rect.y <= 180:
            self.dy *= -1


class Pipe(pygame.sprite.Sprite):
    def __init__(self, init_x=400, init_y=450):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/pipe.png')
        self.image = pygame.transform.scale(self.image, (135, 350))
        self.rect = self.image.get_rect()
        self.rect.x = init_x
        self.rect.y = init_y


class PipeSet(pygame.sprite.Sprite):
    def __init__(self, pipe_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/pipeset.png')
        self.image = pygame.transform.scale(self.image, (115, 1050))
        self.rect = self.image.get_rect()
        self.rect.x = 650
        self.rect.y = pipe_pos
        self.dx = -3

    def update(self):
        self.rect.x += self.dx

        if self.rect.left < -110:
            self.kill()

    def get_rect():
        return self.rect


class Ground(pygame.sprite.Sprite):
    def __init__(self, init_x, init_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/ground.png')
        self.image = pygame.transform.scale(self.image, (650, 70))
        self.rect = self.image.get_rect()
        self.rect.x = init_x
        self.rect.y = init_y
        self.dx = -3

    def update(self):
        self.rect.x += self.dx

    def get_rect(self):
        return self.rect


class Background(pygame.sprite.Sprite):
    def __init__(self, init_x, init_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/background.png')
        self.image = pygame.transform.scale(self.image, (1528, 750))
        self.rect = self.image.get_rect()
        self.rect.x = init_x
        self.rect.y = init_y
        self.dx = -1

    def update(self):
        self.rect.x += self.dx

    def get_rect(self):
        return self.rect
