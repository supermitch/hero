import os, sys

import pygame
from pygame.locals import *

from planet import Planet
from hero import Hero
            
class Game(object):
    
    def __init__(self):
        # Global setup
        self.width = 640
        self.height = 480
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Hero I')

        self.clock = pygame.time.Clock()
        self.fps = 60

        self.planet = Planet(self.width, self.height)
        self.background = self.planet.render()

        self.hero = Hero(self.width, self.height)
        self.allsprites = pygame.sprite.Group(self.hero)

    def main_loop(self):
        """ This is the Main Loop of the Game. """

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    return None
                elif event.type == KEYDOWN:
                    if event.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
                        self.hero.change_speed(event.key, key_down=True)
                    elif event.key in (K_ESCAPE, K_q):
                        pygame.event.post(pygame.event.Event(QUIT))
                elif event.type == KEYUP:
                    if event.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
                        self.hero.change_speed(event.key, key_down=False)

            bg_pos = (0, 0)
            
            #self.planet.update()
            self.screen.blit(self.background, bg_pos)
            self.allsprites.update()
            self.allsprites.draw(self.screen)
            pygame.display.update()
            
            self.clock.tick(self.fps)

