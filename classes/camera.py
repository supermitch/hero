from __future__ import division

from pygame import Rect

class Camera(object):

    def __init__(self, level_w, level_h, screen_w, screen_h):
        self.state = Rect(0, 0, level_w, level_h)
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.half_w = int(screen_w / 2)
        self.half_h = int(screen_h / 2)

    def apply(self, target_rect):
        return target_rect.move(self.state.topleft)

    def update(self, target_rect):
        l, t, _, _ = target_rect
        _, _, w, h = self.state
        # center player
        l, t, _, _ = -l + self.half_w, -t + self.half_h, w, h

        # stop scrolling at the left edge
        l = min(0, l)
        # stop scrolling at the right edge
        l = max(-(self.state.width - self.screen_w), l)
        # stop scrolling at the bottom
        t = max(-(self.state.height - self.screen_h), t)
        # stop scrolling at the top
        t = min(0, t)
        self.state = Rect(l, t, w, h)

