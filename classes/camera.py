import pygame

class Camera(object):

    def __init__(self, screen_size):
        self.state = pygame.Rect((0, 0), screen_size)

    def update(self, reference_position):
        """ Update our position according to the player's position """
        self.state.center = reference_position

    def apply(self, target_pos):
        """ Return a new position, offset according to camera location """
        dx, dy = self.state.topleft
        return (target_pos[0] - dx, target_pos[1] - dy)

