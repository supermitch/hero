from __future__ import division

from pygame import Rect

class Camera(object):

    def __init__(self, level_w, level_h, screen_w, screen_h):
        self.offset = (0, 0)  # (Left, Top)
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.half_w = int(screen_w / 2)
        self.half_h = int(screen_h / 2)

    def update(self, target_rect):
        """ Update our position according to the player's position. """
        print('target', target_rect)
        l, t, _, _ = target_rect
        print('l, t', l, t)
        l, t = -l + self.half_w, -t + self.half_h  # Center player
        print('l, t', l, t)

        print('offset', self.offset)
        l = min(0, l)  # stop scrolling at the left edge
        print('screen', self.screen_w, self.screen_h)
        l = max(-(self.offset[0] - self.screen_w), l)  # Stop at right
        print('l', l)
        t = max(-(self.offset[1] - self.screen_h), t)  # Stop at bottom
        t = min(0, t)  # Stop at top
        print('t', t)
        self.offset = l, t

    def apply(self, target_rect):
        """ Move a rectangle by the current camera offset. """
        return target_rect.move(self.offset)

