import pygame as pg
from settings import *


# Base class for all the game blocks/tetrominos
class Tetromino:
    def __init__(self, id:int):
        self.id = id                    # Each Tetromino shape has a unique id
        self.colors = COLORS

        self.block_size = BLOCK_SIZE    # Size of individual block in tetromino
        
        self.blocks_positions = dict()          # Pos for each block in tetromino
        self.rotation_state = 0

        self.offset = pg.Vector2(0, 0)          # Offset to position blocks


    # Method to set the offset value
    def move(self, offset:tuple=(0, COLUMNS//2 - 1)):
        offset = pg.Vector2(offset)
        self.offset += offset


    # Returns new cell positions after applying offset
    def get_cell_positions(self):
        new_positions = list()
        positions = self.blocks_positions[self.rotation_state]

        for position in positions:
            new_positions.append(position + self.offset)

        return new_positions

    
    # Draw tetromino on the Game Surface
    def draw(self, parent_screen:pg.Surface):
        positions = self.get_cell_positions()

        rect_color = self.colors[self.id]
        
        for position in positions:
            rect = pg.Rect(
                position.y * self.block_size + 1,
                position.x * self.block_size + 1, 
                self.block_size - 1, 
                self.block_size - 1)
            
            pg.draw.rect(parent_screen, rect_color, rect)
        