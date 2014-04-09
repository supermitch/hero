import pygame
from pygame.locals import *

class Player(pygame.sprite.DirtySprite):

    def __init__(self, screen_width, screen_height):
        pygame.sprite.DirtySprite.__init__(self)  # Call base initialize

        self.image = pygame.image.load('images/player.png').convert_alpha()
        self.w, self.h = self.image.get_size()
        self.image = pygame.transform.scale(self.image,
                    (int(self.w * 2), int(self.h * 2)))
        self.rect = self.image.get_rect(center=(screen_width / 2, screen_height / 2))
        self.speed = 3
        self.v = [0.0, 0.0]

    def update(self):
        self.rect.move_ip((self.v[0], self.v[1]))
        self.dirty = 1

    def change_speed(self, key, key_down):
        if key_down:
            directions = {K_LEFT: (0, -1),
                          K_RIGHT: (0, 1),
                          K_UP: (1, -1),
                          K_DOWN: (1, 1)}
            self.v = [0.0, 0.0]
            (axis, sign) = directions[key]
            self.v[axis] = sign * self.speed
        if not key_down:
            self.v = [0.0, 0.0]

