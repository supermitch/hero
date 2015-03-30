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
        # Display surface
        self.surface = pygame.Surface((self.screen_w, self.screen_h))

    def _gen_map(self):
        """ Generates our entire map's geological features. """
        pass

    def update(self):
        """ Update map elements that may be changing. """
        pass

    def render(self, center):
        """ Returns the entire map as an image. """
        half_w = self.screen_w / 2
        half_h = self.screen_h / 2

        # The edges of the visible screen, in pixels
        # assuming screen is centered on center
        x, y = center
        left, right = x - half_w, x + half_w
        top, bottom = y - half_h, y + half_h

        # map tile indices
        min_i = left / self.map.tilewidth
        max_i = right / self.map.tilewidth
        min_j = top / self.map.tilewidth
        max_j = bottom / self.map.tilewidth

        # Bound possible indices
        min_i = max(min_i, 0)
        max_i = min(max_i, self.width)
        min_j = max(min_j, 0)
        max_j = min(max_j, self.height, max_j)
        layer = 0
        for x in range(min_i, max_i):
            for y in range(min_j, max_j):
                image = self.map.get_tile_image(x, y, layer)
                if image is not None:
                    position = x * self.map.tilewidth, y * self.map.tileheight
                    self.surface.blit(image, position)
        return self.surface

        #for i, j in product(xrange(l, r), xrange(t, b)):
        #    self.surface.blit(self.tile_map[i][j].image,
        #                    self.tile_map[i][j].pos)
        #self.view.image = background
        #self.view.rect = pygame.Rect(0, 0,
        #    self.screen_w * self.tile_size, self.screen_h * self.tile_size )
        #return self.view

