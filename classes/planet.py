import os
import sys
import random
from itertools import product

import pygame
from pygame.locals import *
from noise import snoise2, pnoise2

from tile import Tile

class Planet(object):
    """
    Planet object is the map.

    """
    def __init__(self, map_w, map_h):

        self.width = map_w
        self.height = map_h
        self.tile_size = 8
        # TODO: Args
        self.screen_w = 640
        self.screen_h = 480

        # Build our tile map
        self.tile_map = self._gen_map()
        self.tile_group = pygame.sprite.Group()
        self.view = pygame.sprite.Sprite()

    def _gen_map(self):
        """ Generates our entire map's geological features. """
        print('Generating map...')

        tile_size = self.tile_size
        height = self.height / tile_size
        width = self.width / tile_size

        simplex = []
        d_i = random.randint(-2000, 2000)
        d_j = random.randint(-2000, 2000)
        f = 80.0
        octaves = 2
        persistence = 4
        lacunarity = 0.4
        tile_map = [[None for y in xrange(height)] \
                     for x in xrange(width)]
        for i, j in product(xrange(width), xrange(height)):
            # simplex, -1 to 1 shifted to 0 to 9
            z = snoise2(i/f + d_i, j/f + d_j, octaves, \
                persistence, lacunarity) * 4.5 + 4.5
            pos = (i * tile_size, j * tile_size)
            if i in (0, width -1):
                kind = -1
            if j in (0, height -1):
                kind = -1
            tile_map[i][j] = Tile(tile_size, pos, kind=int(z))

        print('\t... done.')
        return tile_map

    def update(self):
        """ Update map elements that may be changing. """
        pass
        #for i, j in product(xrange(self.width), xrange(self.height)):
        #    self.tile_map[i][j].rect.move_ip((2,0))

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

