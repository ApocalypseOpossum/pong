#
#
#

import pygame

from settings import *

class Game():

    # Initialize class
    def __init__(self):
        # Initialize settings object
        self.settings = Settings()
        self.is_running = True
        # Initialize pygame, create a screen to draw to and a clock to handle fps
        self.pygame = pygame.init()
        self.screen = pygame.display.set_mode((self.settings.SCREENWIDTH, self.settings.SCREENHEIGHT))
        self.title = pygame.display.set_caption(self.settings.TITLE)
        self.clock = pygame.time.Clock()


    def events(self):
        # Handle events, act accordingly
        for event in pygame.event.get():
            # If user click on X in the window, exit game loop
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self):
        pass

    def draw(self):
        # Overwrite previous frame by filling in the screen
        self.screen.fill(self.settings.GREY)

        # At the end of the loop handle FPS
        self.clock.tick(self.settings.FPS)