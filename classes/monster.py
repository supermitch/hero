import pygame
from pygame.locals import *

class Monster(pygame.sprite.DirtySprite):

    def __init__(self, kind, x, y):
        pygame.sprite.DirtySprite.__init__(self)  # Call base initialize

        image = {
            'spider': 'spider_1.png',
            'slime': 'slime_1.png'
        }[kind]
        self.image = pygame.image.load('assets/images/monster/'
            + image).convert_alpha()
        self.w, self.h = self.image.get_size()
        self.image = pygame.transform.scale(self.image,
                    (int(self.w * 2), int(self.h * 2)))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 3
        self.v = [0.0, 0.0]

    def update(self):
        pass

    def change_speed(self, key):
        if key:
            directions = {
                LEFT: (0, -1),
                RIGHT: (0, 1),
                UP: (1, -1),
                DOWN: (1, 1)
            }
            self.v = [0.0, 0.0]
            (axis, sign) = directions[key]
            self.v[axis] = sign * self.speed
        if not key_down:
            self.v = [0.0, 0.0]

