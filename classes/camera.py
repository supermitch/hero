from __future__ import division

from pygame import Rect

class Camera(object):

    def __init__(self, screen_size):
        self.state = Rect((0, 0), screen_size)

    def update(self, pos):
        """ Update our position according to the player's position. """
        self.state.center = pos

    def apply(self, target_rect):
        """ Return a rectangle centered according to our location. """
        return target_rect.move(self.state.topleft)

