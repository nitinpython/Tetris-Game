from surface import Surface
from grid import Grid
from settings import *
from game_blocks import *
from random import choice
from position import Position
from pygame.mixer import Sound


# Game board logic
class GameSurface(Surface):
    def __init__(self, parent_screen, width, height, x, y):
        super().__init__(parent_screen, width, height, x, y)

        # Creating grid object
        self.grid = Grid()

        # Defining the tetrominos
        self.tetrominos = [TBlock(), LBlock(), JBlock(), SBlock(), ZBlock(), IBlock(), OBlock()]

        self.current_tetromino = self.get_random_tetromino()
        self.next_tetromino = self.get_random_tetromino()

        self.game_over = False


    # Return a random tetromino block object from the tetrominos object list
    def get_random_tetromino(self):        

        # If the list is empty, fill it again
        if not len(self.tetrominos):
            self.tetrominos = [TBlock(), LBlock(), JBlock(), SBlock(), ZBlock(), IBlock(), OBlock()]

        tetromino = choice(self.tetrominos)             # Choose a random tetromino 
        self.tetrominos.remove(tetromino)           # Remove the chosen tetromino from the list to avoid repetition

        return tetromino

    
    # Check if the tetromino is inside the game surface
    def tetromino_is_inside(self):
        positions = self.current_tetromino.get_cell_positions()

        for position in positions:
            if not self.grid.is_inside(position):
                return False
            
        return True

    
    # Methods to move the tetromino according to the user input
    
    def move_left(self):
        self.current_tetromino.move(Position(0, -1))

        # If the tetromino goes out or overlaps other tetromino then undo the move
        if not self.tetromino_is_inside() or not self.tetromino_fits():              
            self.current_tetromino.move(Position(0, 1))
            
    
    def move_right(self):
        self.current_tetromino.move(Position(0, 1))

        if not self.tetromino_is_inside() or not self.tetromino_fits():              
            self.current_tetromino.move(Position(0, -1))
    
    
    def move_down(self):
        self.current_tetromino.move(Position(1, 0))

        if not self.tetromino_is_inside() or not self.tetromino_fits():              
            self.current_tetromino.move(Position(-1, 0))
            self.lock_block()


    def rotate(self):
        self.current_tetromino.rotate()

        if not self.tetromino_is_inside() or not self.tetromino_fits():
            self.current_tetromino.undo_rotate()


    # Disable the movement of tetromino when it reaches at the bottom and generates a new tetromino
    def lock_block(self):
        
        positions =  self.current_tetromino.get_cell_positions()

        # Changing the grid values
        for position in positions:
            self.grid.grid[position.row][position.column] = self.current_tetromino.id

        # Updating the current and next tetromino
        self.current_tetromino = self.next_tetromino
        self.next_tetromino = self.get_random_tetromino()

        # Clear rows if full
        rows_cleared = self.grid.clear_full_rows()

        if rows_cleared:
            self.play_sound(SOUND_FILES['clear'])


        # Game over if the block overlaps at the top
        if not self.tetromino_fits():
            self.run_game_over()


    # Method to check tetrominos overlapping
    def tetromino_fits(self):
        positions = self.current_tetromino.get_cell_positions()

        for position in positions:
            if not self.grid.is_empty(position):
                return False
            
        return True
    

    def run_game_over(self):
        self.game_over = True
        self.play_sound(SOUND_FILES['game over'])

    
    @staticmethod
    def play_sound(filename: str):
        sound = Sound(filename)
        sound.play()
    
    
    # Calls all the necessary methods of the GameSurface class
    def run(self):
        self.draw()
        self.grid.draw(self.surface)
        self.current_tetromino.draw(self.surface)
        