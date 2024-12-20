from surface import Surface
from settings import *
from grid import Grid
from position import Position
import pygame as pg


# Preview surface to show the next block
class PreviewSurface(Surface):
    
    def __init__(self, parent_screen, width, height, x, y):
        super().__init__(parent_screen, width, height, x, y)

        self.grid = Grid(PREVIEW_ROWS, PREVIEW_COLUMNS, BLOCK_SIZE)

        self.font_size = 20
        self.font = pg.font.SysFont('consolas', self.font_size, True)

    
    def show_text(self):
        text = 'Next Block'
        color = 'black'

        rendered_text = self.font.render(text, False, color)

        self.surface.blit(rendered_text, (self.grid.block_size, 3 * self.grid.block_size))

    
    def show_next(self, next_tetromino):
        positions = next_tetromino.blocks_positions[0]

        rect_color = next_tetromino.colors[next_tetromino.id]

        for position in positions:
            position += Position(self.grid.rows//2, 1)      # Manual offset
            
            rect = pg.Rect(
                position.column * self.grid.block_size + 1,
                position.row * self.grid.block_size + 1,
                self.grid.block_size - 1, 
                self.grid.block_size - 1
                )

            pg.draw.rect(self.surface, rect_color, rect)

    
    # Calls all the necessary methods of the PreviewSurface class
    def run(self, next_tetromino):
        self.draw()
        self.grid.draw(self.surface)
        self.surface.fill(COLORS[0])        # BG color
        self.show_text()
        self.show_next(next_tetromino)