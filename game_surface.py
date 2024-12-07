from surface import Surface
from grid import Grid
from settings import *


# Game board logic
class GameSurface(Surface):
    def __init__(self, parent_screen, width, height, x, y):
        super().__init__(parent_screen, width, height, x, y)

        # Creating grid object
        self.grid = Grid(self.surface, ROWS, COLUMNS, BLOCK_SIZE)


    # Calls all the necessary methods of the GameSurface class
    def run(self):
        self.draw()
        self.grid.draw()
        