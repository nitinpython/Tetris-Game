import pygame as pg
from settings import *
from position import Position


# Game board
class Grid:
    def __init__(self, rows: int=ROWS, columns: int=COLUMNS, block_size:int=BLOCK_SIZE, colors: dict=COLORS):
        self.rows = rows
        self.columns = columns
        self.block_size = block_size
        self.colors = colors

        # Initializing the grid of all zeroes (to get the pink color)
        self.grid = [[0 for _ in range(self.columns)] for _ in range(self.rows)]


    # Method to check the grid values
    def print_grid(self):
        for row in self.grid:
            for column in row:
                print(column, end=' ')
            print()


    # Check if a pos is inside the game surface
    def is_inside(self, pos: Position):
        if pos.row < self.rows and pos.column in range(0, self.columns):
            return True
        
        return False
    
    
    # Check if a tetromino already exist at a perticular position or not (to avoid overlapping)
    def is_empty(self, pos: Position):
        if self.grid[pos.row][pos.column] == 0:
            return True
        
        return False
    

    # Check if a row is full
    def is_row_full(self, row: int):    
        
        if 0 in self.grid[row]:
            return False
            
        return True
    

    # Clear a row
    def clear_row(self, row: int):
        self.grid[row] = [0] * self.columns


    # Move a row down when the below row gets cleared
    def move_row_down(self, row: int, num_rows: int):
        self.grid[row + num_rows] = self.grid[row]


    # Clear rows if full
    def clear_full_rows(self):
        completed_rows = 0              # Counter to track the no of cleared rows

        # Iterating each row from downwards
        for row in range(self.rows - 1, 0, -1):
            
            if self.is_row_full(row):
                self.clear_row(row)
                completed_rows += 1

            elif completed_rows:
                self.move_row_down(row, completed_rows)

        return completed_rows
    
    
    def draw(self, parent_screen: pg.Surface):

        for row in range(self.rows):
            for column in range(self.columns):
                
                cell_rect = pg.Rect(column * self.block_size + 1, row * self.block_size + 1, self.block_size - 1, self.block_size - 1)
                rect_color = self.colors[self.grid[row][column]]
                pg.draw.rect(parent_screen, rect_color, cell_rect)
