import pygame as pg
from settings import *
from position import Position


# Base class for all the game blocks/tetrominos
class Tetromino:
    def __init__(self, id:int):
        self.id = id                    # Each Tetromino shape has a unique id
        self.colors = COLORS

        self.block_size = BLOCK_SIZE    # Size of individual block in tetromino
        
        self.blocks_positions = dict()          # Pos for each block in tetromino
        self.rotation_state = 0

        self.offset = Position(0, 0)          # Offset to position blocks


    # Method to set the offset value
    def move(self, offset: Position=Position(0, COLUMNS//2 - 1)):
        self.offset += offset


    # Returns new cell positions after applying offset
    def get_cell_positions(self):
        new_positions = list()
        positions = self.blocks_positions[self.rotation_state]

        for position in positions:
            new_positions.append(position + self.offset)

        return new_positions

    
    def rotate(self):
        if self.rotation_state < len(self.blocks_positions) - 1:
            self.rotation_state += 1

        # Reset the rotation state if it is equal to 3
        else:
            self.rotation_state = 0


    def undo_rotate(self):
        if self.rotation_state > 0:
            self.rotation_state -= 1

        # Set rotation state to 3 if it is equal to 0
        else:
            self.rotation_state = len(self.blocks_positions) - 1

    
    # Draw tetromino on the Game Surface
    def draw(self, parent_screen:pg.Surface):
        positions = self.get_cell_positions()

        rect_color = self.colors[self.id]
        
        for position in positions:
            rect = pg.Rect(
                position.column * self.block_size + 1,
                position.row * self.block_size + 1, 
                self.block_size - 1, 
                self.block_size - 1)
            
            pg.draw.rect(parent_screen, rect_color, rect)
        