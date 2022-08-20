#
#
#

import pygame

from settings import *
from player import *

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
        self.delta_time = 0

        # Load assets and objects
        self.player = Player()


    def events(self):
        # Handle events, act accordingly
        for event in pygame.event.get():
            # If user click on X in the window, exit game loop
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self):
        # Update Player AI and ball
        self.player.update(self.delta_time)
        

    def draw(self):
        # Overwrite previous frame by filling in the screen
        self.screen.fill(self.settings.WHITE)

        # Draw interface

        # Draw Player and AI
        self.player.draw(self.screen)

        # After all drawing is finished update screen
        pygame.display.update()

        # At the end of the loop handle FPS
        self.delta_time = self.clock.tick(self.settings.FPS) / 60