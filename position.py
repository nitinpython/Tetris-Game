# Class to create Position objects with row and column attributes
class Position:
    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column


    # Method to add two Position objects
    def __add__(self, other):
        row = self.row + other.row
        column = self.column + other.column

        return Position(row, column)