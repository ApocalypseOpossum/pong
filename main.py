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

if __name__ == '__main__':
    main()