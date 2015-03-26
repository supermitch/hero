import os
import sys

import pygame
import pytmx
from pygame.locals import *

class Planet(object):
    """
    Planet object is the map.

    """
    def __init__(self, screen_w, screen_h):

        self.screen_w = screen_w
        self.screen_h = screen_h

        self.load_map('corsa')

    def load_map(self, map_name):
        self.map = pytmx.load_pygame('maps/' + map_name + '.tmx')
        self.width = self.map.width
        self.height = self.map.height
        self.size = (self.width, self.height)

    def _gen_map(self):
        """ Generates our entire map's geological features. """
        pass

    def update(self):
        """ Update map elements that may be changing. """
        pass

    def render(self, center):
        """ Returns the entire map as an image. """
        x, y = center
        half_w = self.screen_w / 2
        half_h = self.screen_h / 2
        l = (x - half_w - 20) / self.tile_size
        r = (x + half_w - 2) / self.tile_size
        t = (y - half_h) / self.tile_size
        b = (y + half_h) / self.tile_size

        background = pygame.Surface((self.width, self.height))
        for i, j in product(xrange(l, r), xrange(t, b)):
            background.blit(self.tile_map[i][j].image,
                            self.tile_map[i][j].pos)
        self.view.image = background
        self.view.rect = pygame.Rect(0, 0,
            self.screen_w * self.tile_size, self.screen_h * self.tile_size )
        return self.view

