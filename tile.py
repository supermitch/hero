import pygame
from pygame.locals import *


class Tile(pygame.sprite.Sprite):
    """
    Tile object is a single tile of a planet.
    """
    def __init__(self, tile_size, pos, kind=None):
        # Initialize base class
        pygame.sprite.Sprite.__init__(self)

        self.TERRAINS = {
            0: 'ocean',
            1: 'lake',
            2: 'stream',
            3: 'sand',
            4: 'plains',
            5: 'grass',
            6: 'swamp',
            7: 'forest',
            8: 'rock',
            9: 'dirt',
        }
        self.COLORS = {
            0: (87, 87, 189), # Dark purple
            1: (8, 129, 209), # Blue
            2: (8, 196, 209), # Light blue
            3: (235, 228, 47), # Yellow
            4: (176, 245, 27), # Light green
            5: (7, 250, 52), # Bright green
            6: (25, 145, 20), # Dark green
            7: (209, 149, 8), # Light brown
            8: (163, 58, 34), # Reddish brown
            9: (94, 35, 4) # Dark brown
        }

        self.size = tile_size
        self.pos = pos  # (x, y) coords
        self.altitude = 0
        if kind is not None:
            self.terrain = kind
        else:
            print('could not match terrain', kind)
            self.terrain = 1
        #self.color = self.COLORS[self.terrain]

        self.image = pygame.Surface((self.size, self.size))
        self.rect = self.image.get_rect()
        self._set_color()

    def _set_color(self):
        color = int(self.terrain * 255/20.0) # 0 to 9 shifted to 0 to 255
        color = (color, color, color)
        #color = self.COLORS[self.terrain]
        self.image.fill(color)

    def _set_terrain(self, terrain):
        """ Set a tile's new terrain type. """
        self.terrain = terrain
        self.color = self.COLORS[self.terrain]
        self.image.fill(self.color)
    
    def draw(self, screen):
        screen.blit(self.image, self.pos)

