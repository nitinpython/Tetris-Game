from surface import Surface
from grid import Grid
from settings import *
from game_blocks import *
from random import choice


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


    # Return a random tetromino block object from the tetrominos object list
    def get_random_tetromino(self):
        
        # Create a copy to prevent modifying original list
        tetrominos = self.tetrominos.copy()         

        # If the list is empty, fill it again
        if not len(tetrominos):
            del tetrominos                          # Delete the object to clear memory
            tetrominos = self.tetrominos.copy()             # Create new copy

        tetromino = choice(tetrominos)             # Choose a random tetromino 
        tetrominos.remove(tetromino)           # Remove the chosen tetromino from the list to avoid repetition

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
        self.current_tetromino.move((0, -1))

        # If the tetromino goes out then undo the move
        if not self.tetromino_is_inside():              
            self.current_tetromino.move((0, 1))
            
    
    def move_right(self):
        self.current_tetromino.move((0, 1))

        if not self.tetromino_is_inside():              
            self.current_tetromino.move((0, -1))
    
    
    def move_down(self):
        self.current_tetromino.move((1, 0))

        if not self.tetromino_is_inside():              
            self.current_tetromino.move((-1, 0))
    
    
    # Calls all the necessary methods of the GameSurface class
    def run(self):
        self.draw()
        self.grid.draw(self.surface)
        self.current_tetromino.draw(self.surface)
        