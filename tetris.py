from settings import *
import pygame as pg
from pygame.locals import *
from game_surface import GameSurface
from preview_surface import PreviewSurface
from score_surface import ScoreSurface


# Main game class
class Tetris:
    def __init__(self):
        pg.init()

        # Loading images
        self.IMAGES = self.load_images()

        # Creating Display surface (parent screen)
        self.SCREEN = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(CAPTION)
        pg.display.set_icon(self.IMAGES['icon'])

        # Creating Game surface object
        self.game_surface = GameSurface(self.SCREEN, GAME_SURFACE_WIDTH, GAME_SURFACE_HEIGHT, PADDING, PADDING)
        
        # Creating Preview surface object
        self.preview_surface = PreviewSurface(self.SCREEN, SIDE_PANEL_WIDTH, PREVIEW_SURFACE_HEIGHT, PREVIEW_SURFACE_X, PADDING)
        
        # Creating Score surface object
        self.score_surface = ScoreSurface(self.SCREEN, SIDE_PANEL_WIDTH, SCORE_SURFACE_HEIGHT, PREVIEW_SURFACE_X, SCORE_SURFACE_Y)


    # Method to load game images
    def load_images(self):
        images = dict()

        for key, value in IMAGE_FILES.items():
            images[key] = pg.image.load(value)

        return images
    

    @staticmethod
    def close_game_window():
        pg.quit()
        exit()


    def event_handler(self):
        
        for event in pg.event.get():
            
            # Close the game
            if event.type == QUIT:
                self.close_game_window()

    
    def run(self):

        while True:

            self.event_handler()

            self.SCREEN.fill(BG_COLOR)                  # Refresh the screen

            self.game_surface.run()
            self.preview_surface.run()
            self.score_surface.run()

            pg.display.update()


if __name__ == '__main__':
    tetris = Tetris()
    tetris.run()