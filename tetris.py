from settings import *
import pygame as pg
from pygame.locals import *


# Main game class
class Tetris:
    def __init__(self):
        pg.init()

        # Loading images
        self.IMAGES = self.load_images()

        # Creating display surface
        self.SCREEN = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(CAPTION)
        pg.display.set_icon(self.IMAGES['icon'])


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


            pg.display.update()


if __name__ == '__main__':
    tetris = Tetris()
    tetris.run()