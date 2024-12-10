import pygame as pg
from settings import *


# Individual block object in a Tetromino
class Block(pg.sprite.Sprite):
    def __init__(self, x:int, y:int, color, width: int=BLOCK_SIZE - 1, height: int=BLOCK_SIZE - 1):
        super().__init__()
        x = x * BLOCK_SIZE + 1
        y = y * BLOCK_SIZE + 1

        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))


# Base class for all the game blocks/tetrominos
class Tetromino:
    def __init__(self, id:int):
        self.id = id                    # Each Tetromino shape has a unique id
        self.colors = COLORS

        self.blocks_positions = dict()          # Pos for each block in tetromino
        self.rotation_state = 0
        self.block_sprites = pg.sprite.Group()

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

        for position in positions:
            block_color = self.colors[self.id]
            block = Block(position.y, position.x, block_color)
            self.block_sprites.add(block)

        self.block_sprites.draw(parent_screen)
        