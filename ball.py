#
#
#

import pygame

from settings import *

class Ball():

    def __init__(self):
        self.settings = Settings()
        self.x = self.settings.SCREENWIDTH / 2
        self.y = self.settings.SCREENHEIGHT / 2
        self.width = 20
        self.height = 20
        self.middle = self.y + self.height / 2
        self.y_vel = 0
        self.x_vel = 0 

    def update(self, dt):
        pass

    def draw(self, surface):
        pygame.draw.rect(surface, self.settings.BLUE, (self.x, self.y, self.width, self.height))