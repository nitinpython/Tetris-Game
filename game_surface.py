from surface import Surface
from grid import Grid
from settings import *
from game_blocks import *


# Game board logic
class GameSurface(Surface):
    def __init__(self, parent_screen, width, height, x, y):
        super().__init__(parent_screen, width, height, x, y)

        # Creating grid object
        self.grid = Grid()

        # Testing game blocks
        self.t = TBlock()


    # Calls all the necessary methods of the GameSurface class
    def run(self):
        self.draw()
        self.grid.draw(self.surface)
        self.t.draw(self.surface)
        