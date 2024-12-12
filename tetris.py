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

        # Constants
        self.playing = True

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


    @ staticmethod
    def generate_hover_effect(*args: pg.Rect):
        
        # Checking if the mouse hovers on the buttons
        if (
            args[0].collidepoint(pg.mouse.get_pos()) or
            args[1].collidepoint(pg.mouse.get_pos()) or
            args[2].collidepoint(pg.mouse.get_pos())
            ):
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)

        else:
            pg.mouse.set_cursor()


    @staticmethod
    def button_clicked(button: pg.Rect):
        # Checking if the mouse is clicked while hovering on the button
        if button.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            return True
        
        return False
    
    
    def event_handler(self):
        
        for event in pg.event.get():
            
            # Close the game
            if event.type == QUIT:
                self.close_game_window()

            # Keyboard event
            elif event.type == KEYDOWN:
                
                # Pause the game
                if event.key == K_SPACE:
                    self.playing = False

                # Check for user input only if the game is running
                if self.playing:

                    if event.key == K_LEFT:
                        self.game_surface.move_left()
                    
                    elif event.key == K_RIGHT:
                        self.game_surface.move_right()
                    
                    elif event.key == K_DOWN:
                        self.game_surface.move_down()

    
    def run(self):

        while True:

            self.event_handler()

            self.SCREEN.fill(BG_COLOR)                  # Refresh the screen

            if self.playing:
                self.game_surface.run()
                self.preview_surface.run()
                self.score_surface.run()

            # Game paused
            else:
                
                # Blit the menu buttons
                resume_button = self.SCREEN.blit(self.IMAGES['resume'], RESUME_BUTTON_COORDINATES)
                restart_button = self.SCREEN.blit(self.IMAGES['restart'], RESTART_BUTTON_COORDINATES)
                exit_button = self.SCREEN.blit(self.IMAGES['exit'], EXIT_BUTTON_COORDINATES)

                self.generate_hover_effect(resume_button, restart_button, exit_button)

                # Check which button is clicked and perform the action
                if self.button_clicked(resume_button):
                    self.playing = True                     # Resume game

                elif self.button_clicked(restart_button):
                    self.__init__()                         # Restart game

                elif self.button_clicked(exit_button):
                    self.close_game_window()                # Close the game

            
            pg.display.update()


if __name__ == '__main__':
    tetris = Tetris()
    tetris.run()