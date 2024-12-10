from tetromino import Tetromino
from pygame import Vector2
from settings import COLUMNS


class TBlock(Tetromino):
    def __init__(self, id: int=1):
        super().__init__(id)

        self.blocks_positions = {
            0: [Vector2(0, 1), Vector2(1, 0), Vector2(1, 1), Vector2(1, 2)],
            1: [Vector2(0, 1), Vector2(1, 1), Vector2(1, 2), Vector2(2, 1)],
            2: [Vector2(1, 0), Vector2(1, 1), Vector2(1, 2), Vector2(2, 1)],
            3: [Vector2(0, 1), Vector2(1, 0), Vector2(1, 1), Vector2(2, 1)]
        }

        self.move()


class LBlock(Tetromino):
    def __init__(self, id: int=2):
        super().__init__(id)

        self.blocks_positions = {
            0: [Vector2(0, 2), Vector2(1, 0), Vector2(1, 1), Vector2(1, 2)],
            1: [Vector2(0, 1), Vector2(1, 1), Vector2(2, 1), Vector2(2, 2)],
            2: [Vector2(1, 0), Vector2(1, 1), Vector2(1, 2), Vector2(2, 0)],
            3: [Vector2(0, 0), Vector2(0, 1), Vector2(1, 1), Vector2(2, 1)]
        }

        self.move()


class JBlock(Tetromino):
    def __init__(self, id: int=3):
        super().__init__(id)

        self.blocks_positions = {
            0: [Vector2(0, 0), Vector2(1, 0), Vector2(1, 1), Vector2(1, 2)],
            1: [Vector2(0, 1), Vector2(0, 2), Vector2(1, 1), Vector2(2, 1)],
            2: [Vector2(1, 0), Vector2(1, 1), Vector2(1, 2), Vector2(2, 2)],
            3: [Vector2(0, 1), Vector2(1, 1), Vector2(2, 0), Vector2(2, 1)]
        }

        self.move()


class SBlock(Tetromino):
    def __init__(self, id: int=4):
        super().__init__(id)

        self.blocks_positions = {
            0: [Vector2(0, 1), Vector2(0, 2), Vector2(1, 0), Vector2(1, 1)],
            1: [Vector2(0, 1), Vector2(1, 1), Vector2(1, 2), Vector2(2, 2)],
            2: [Vector2(1, 1), Vector2(1, 2), Vector2(2, 0), Vector2(2, 1)],
            3: [Vector2(0, 0), Vector2(1, 0), Vector2(1, 1), Vector2(2, 1)]
        }

        self.move()


class ZBlock(Tetromino):
    def __init__(self, id: int=5):
        super().__init__(id)

        self.blocks_positions = {
            0: [Vector2(0, 0), Vector2(0, 1), Vector2(1, 1), Vector2(1, 2)],
            1: [Vector2(0, 2), Vector2(1, 1), Vector2(1, 2), Vector2(2, 1)],
            2: [Vector2(1, 0), Vector2(1, 1), Vector2(2, 1), Vector2(2, 2)],
            3: [Vector2(0, 1), Vector2(1, 0), Vector2(1, 1), Vector2(2, 0)]
        }

        self.move()


class IBlock(Tetromino):
    def __init__(self, id: int=6):
        super().__init__(id)

        self.blocks_positions = {
            0: [Vector2(1, 0), Vector2(1, 1), Vector2(1, 2), Vector2(1, 3)],
            1: [Vector2(0, 2), Vector2(1, 2), Vector2(2, 2), Vector2(3, 2)],
            2: [Vector2(2, 0), Vector2(2, 1), Vector2(2, 2), Vector2(2, 3)],
            3: [Vector2(0, 1), Vector2(1, 1), Vector2(2, 1), Vector2(3, 1)]
        }

        self.move((-1, COLUMNS//2 - 2))


class OBlock(Tetromino):
    def __init__(self, id: int=7):
        super().__init__(id)

        self.blocks_positions = {
            0: [Vector2(0, 0), Vector2(0, 1), Vector2(1, 0), Vector2(1, 1)]
        }

        self.move()