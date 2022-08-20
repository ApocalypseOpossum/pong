#
#
#

import pygame

from settings import *

class AI():

    def __init__(self):
        self.settings = Settings()
        self.width = 10
        self.height = 100
        self.x = self.settings.SCREENWIDTH - 10 - self.width
        self.y = self.settings.SCREENHEIGHT / 2
        self.middle = self.y + self.height / 2
        self.y_vel = 30
        self.score = 0

    def update(self, dt):
        # Check if ai has moved past boundary and reposition
        if self.y <= 0:
            self.y = 0;
        if self.y + self.height >= self.settings.SCREENHEIGHT:
            self.y = self.settings.SCREENHEIGHT - self.height

    def draw(self, surface):
        pygame.draw.rect(surface, self.settings.BLUE, (self.x, self.y, self.width, self.height))