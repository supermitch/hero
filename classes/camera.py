from __future__ import division

from pygame import Rect

class Camera(object):

    def __init__(self, map_size, screen_size):
        self.state = Rect(0, 0, map_size[0], map_size[1])
        self.screen_w, self.screen_h = screen_size
        self.half_w = int(self.screen_w / 2)
        self.half_h = int(self.screen_h / 2)

    def update(self, target_rect):
        """ Update our position according to the player's position. """
        l, t, _, _ = target_rect
        _, _, w, h = self.state
        l, t = -l + self.half_w, -t + self.half_h  # Center player

        l = min(0, l)  # stop scrolling at the left edge
        l = max(-(self.state.width - self.screen_w), l)  # Stop at right
        t = max(-(self.state.height - self.screen_h), t)  # Stop at bottom
        t = min(0, t)  # Stop at top
        self.state = Rect(l, t, w, h)

    def apply(self, target_rect):
        """ Return a rectangle centered according to our location. """
        return target_rect.move(self.state.topleft)

