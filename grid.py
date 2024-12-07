import pygame as pg
from settings import COLORS


# Game board
class Grid:
    def __init__(self, parent_screen: pg.Surface, rows: int, columns: int, block_size:int, colors: dict=COLORS):
        self.parent_screen = parent_screen
        self.rows = rows
        self.columns = columns
        self.block_size = block_size
        self.colors = colors

        # Initializing the grid of all zeroes (to get the pink color)
        self.grid = [[0 for _ in range(self.columns)] for _ in range(self.rows)]


    # Method to check the grid values
    def print_grid(self):
        for row in self.grid:
            for column in row:
                print(column, end=' ')
            print()


    def draw(self):

        for row in range(self.rows):
            for column in range(self.columns):
                
                cell_rect = pg.Rect(column * self.block_size + 1, row * self.block_size + 1, self.block_size - 1, self.block_size - 1)
                rect_color = self.colors[self.grid[row][column]]
                pg.draw.rect(self.parent_screen, rect_color, cell_rect)
