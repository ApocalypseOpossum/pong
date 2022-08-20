#
#
#

from game import *

def main():
    # Create a new instance of game
    game = Game()

    # Start game loop
    while game.is_running:
        game.events()
        game.update()
        game.draw()

# Check to see if main was imported or ran directly
if __name__ == '__main__':
    main()