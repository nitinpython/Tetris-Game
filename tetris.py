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

        # Clock object
        self.clock = pg.time.Clock()

        # Game timer
        self.GAME_UPDATE = pg.USEREVENT
        pg.time.set_timer(self.GAME_UPDATE, GAME_SPEED)

        # Loading images
        self.IMAGES = self.load_images()

        # Loading Background music
        pg.mixer.music.load(SOUND_FILES['bgm'])

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
            
            pg.mouse.set_cursor()           # Change the cursor back to default
            return True
        
        return False
    

    def resume_game(self):
        self.playing = True
        pg.mixer.music.unpause()                # Resume BGM


    def restart_game(self):
        self.__init__()
        pg.mixer.music.play(-1)


    @staticmethod
    def play_sound(filename: str):
        sound = pg.mixer.Sound(filename)
        sound.play()
    
    
    def event_handler(self):
        
        for event in pg.event.get():
            
            # Close the game
            if event.type == QUIT:
                self.close_game_window()

            # Check for user input only if the game is running and not over
            if self.playing and not self.game_surface.game_over:
                
                # Control game speed through the game timer
                if event.type == self.GAME_UPDATE:
                    self.game_surface.move_down()           # Gravity
            
                # Keyboard event
                if event.type == KEYDOWN:
                    
                    # Pause the game
                    if event.key == K_SPACE:
                        self.play_sound(SOUND_FILES['move'])
                        self.playing = False

                    elif event.key == K_LEFT:
                        self.play_sound(SOUND_FILES['move'])
                        self.game_surface.move_left()
                        
                    elif event.key == K_RIGHT:
                        self.play_sound(SOUND_FILES['move'])
                        self.game_surface.move_right()
                        
                    elif event.key == K_DOWN:
                        self.play_sound(SOUND_FILES['move'])
                        self.game_surface.move_down()

                    elif event.key == K_UP:
                        self.play_sound(SOUND_FILES['move'])
                        self.game_surface.rotate()

 
    def run(self):

        pg.mixer.music.play(-1)               # Play BGM

        while True:

            self.clock.tick(FPS)
            
            self.event_handler()

            self.SCREEN.fill(BG_COLOR)                  # Refresh the screen

            if self.playing:
                self.game_surface.run()
                self.preview_surface.run(self.game_surface.next_tetromino)
                self.score_surface.run(self.game_surface.score)

                # If game over
                if self.game_surface.game_over:

                    pg.mixer.music.stop()           # Stop BGM

                    # Blit restart button
                    restart_game_button = self.SCREEN.blit(self.IMAGES['restart game'], RESTART_BUTTON_COORDINATES)
                    
                    # Restart the game
                    if self.button_clicked(restart_game_button):
                        self.restart_game()


            # Game paused
            else:
                
                pg.mixer.music.pause()              # Pause BGM

                # Blit the menu buttons
                resume_button = self.SCREEN.blit(self.IMAGES['resume'], RESUME_BUTTON_COORDINATES)
                restart_button = self.SCREEN.blit(self.IMAGES['restart'], RESTART_BUTTON_COORDINATES)
                exit_button = self.SCREEN.blit(self.IMAGES['exit'], EXIT_BUTTON_COORDINATES)

                self.generate_hover_effect(resume_button, restart_button, exit_button)

                # Check which button is clicked and perform the action
                if self.button_clicked(resume_button):
                    self.resume_game()

                elif self.button_clicked(restart_button):
                    self.restart_game()

                elif self.button_clicked(exit_button):
                    self.close_game_window()                # Close the game

            
            pg.display.update()


if __name__ == '__main__':
    tetris = Tetris()
    tetris.run()