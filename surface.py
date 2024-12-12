import pygame as pg


# Base class to create game, preview and score surfaces
class Surface:
    def __init__(self, parent_screen: pg.Surface, width: int, height: int, x: int, y: int):
        self.parent_screen = parent_screen
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.surface = pg.Surface((self.width, self.height))


    def draw(self):
        self.parent_screen.blit(self.surface, (self.x, self.y))
        