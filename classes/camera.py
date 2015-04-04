from __future__ import division

from pygame import Rect

class Camera(object):

    def __init__(self, screen_size):
        self.state = Rect((0, 0), screen_size)

    def update(self, pos):
        """ Update our position according to the player's position. """
        self.state.center = pos

    def apply(self, target_rect):
        """ Return a new ectangle offset according to our location. """
        dx, dy = self.state.topleft
        return target_rect.move(-dx, -dy)

