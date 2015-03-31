import os, sys

import pytmx
import pygame
from pygame.locals import *

from camera import Camera
from planet import Planet
from player import Player
from monster import Monster

class Game(object):

    def __init__(self):
        # Global setup
        self.screen_w = 640
        self.screen_h = 480
        self.screen_size = (self.screen_w, self.screen_h)

        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption('Hero I')

        self.clock = pygame.time.Clock()
        self.fps = 60

        self.planet = Planet(*self.screen_size)

        self.player = Player(self.screen_w/2, self.screen_h/2)

        self.spider = Monster('spider', 50, 100)
        self.slime = Monster('slime', 200, 400)
        self.monsters = pygame.sprite.Group(self.spider, self.slime)

        self.allsprites = pygame.sprite.Group(self.player, self.monsters)

        self.camera = Camera(self.screen_size)

    def main_loop(self):
        """ This is the Main Loop of the Game. """

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                elif event.type == KEYDOWN:
                    if event.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
                        self.player.change_speed(event.key, key_down=True)
                    elif event.key in (K_ESCAPE, K_q):
                        pygame.event.post(pygame.event.Event(QUIT))
                elif event.type == KEYUP:
                    if event.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
                        self.player.change_speed(event.key, key_down=False)

            self.screen.fill(Color('#FF00FF'))

            self.planet.update()

            self.player.update()

            self.camera.update(self.player.rect.center)

            # Render the map (background)
            print(self.camera.state.center)
            self.screen.blit(self.planet.render(self.camera.state.center), (0, 0))

            for a in self.allsprites:
                if a is not self.player:
                    a.update()
                #self.screen.blit(a.image, self.camera.apply(a.rect))
                self.screen.blit(a.image, a.rect)

            pygame.display.update()

            self.clock.tick(self.fps)

