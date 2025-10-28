import pygame
from pygame.locals import *
from constants import *


class GameObjectColor(object):

    def __init__(self, identification_number, color):
        # Store id and position pixel size
        self.id = identification_number

        # get representation image
        self.rep = pygame.Surface(REP_POS_SIZE)
        self.rep.fill(color)

    def draw_game_image(self, view, x, y, direction=0):
        pass

    def draw_representation_image(self, view, x, y):
        # map_start is the pixel coordinates of where the game map starts
        # x and y are the position coordinates of this Floor object

        # draw representation image
        view.surface.blit(self.rep, (REP_MAP_START[0] + x * REP_POS_SIZE[0],
                                     REP_MAP_START[1] + y * REP_POS_SIZE[1]))
        pygame.display.flip()


class BumpSpright(GameObjectColor):
    def __init__(self):
        super(BumpSpright, self).__init__(19.0, (255, 0, 0))
