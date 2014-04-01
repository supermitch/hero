import os, sys
import random as rnd

import pygame
from pygame.locals import *

from noise import snoise2, pnoise2

from tile import Tile

class Planet(object):
    """
    Planet object is the map.

    """
    def __init__(self, width, height):

        self.width = int(width * 1)
        self.height = int(height * 1)
        self.tile_size = 2

        # Generation settings: (1 to 10)
        self.island_gen = {
            'count': 5,
            'altitude': 3,
            'gradient': 4,
            'density': 9
        }

        # Build our tile map
        self.tile_map = self._gen_map()
        self.tile_group = pygame.sprite.Group()

    def _seed_islands(self, island_count):
        """ Seeds 'volcanoes' in the ocean to create the continents. """
        coords = []
        for i in range(island_count):
            x = rnd.randint(0, self.width)
            y = rnd.randint(0, self.height)
            coords.append( (x, y) )
        return coords
         
    def _gen_map(self):
        """ Generates our map's geological features. """
        rnd.seed()   # Initialize generator
        island_count = self.island_gen['count'] * rnd.randint(5,9)
        island_coords = self._seed_islands(island_count)

        simplex = []
        d_i = rnd.randint(-2000, 2000)
        d_j = rnd.randint(-2000, 2000)
        f = 80.0
        octaves = 2
        persistence = 4
        lacunarity = 0.5 
        tile_map = [[None for y in xrange(self.height)] \
                     for x in xrange(self.width)]
        for i in xrange(self.width):
            for j in xrange(self.height):
                # simplex, -1 to 1 shifted to 0 to 9
                z = snoise2(i/f + d_i, j/f + d_j, octaves, \
                    persistence, lacunarity) * 4.5 + 4.5
                pos = (i * self.tile_size, j * self.tile_size)
                tile_map[i][j] = Tile(self.tile_size, pos, kind =int(z))

        return tile_map

    def update(self):
        for i in xrange(self.width):
            for j in xrange(self.height):
                self.tile_map[i][j].rect.move_ip((1,0))

    def render(self):
        """ Returns the entire map as an image. """
        background = pygame.Surface((self.width * self.tile_size,
                                    self.height * self.tile_size))
        for i in xrange(self.width):
            for j in xrange(self.height):
                background.blit(self.tile_map[i][j].image,
                                self.tile_map[i][j].pos)
        return background

