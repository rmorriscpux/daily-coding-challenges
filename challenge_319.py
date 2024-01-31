'''
An 8-puzzle is a game played on a 3 x 3 board of tiles, with the ninth tile missing.
The remaining tiles are labeled 1 through 8 but shuffled randomly.
Tiles may slide horizontally or vertically into an empty space, but may not be removed from the board.

Design a class to represent the board, and find a series of steps to bring the board to the state [[1, 2, 3], [4, 5, 6], [7, 8, None]].
'''

from random import choice
from copy import deepcopy
from typing import NamedTuple

class Coord(NamedTuple):
    x: int
    y: int

class EightPuzzle:
    def __init__(self, randomize: bool=True):
        self.FINISH_STATE = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, None]
        ]
        self.board = deepcopy(self.FINISH_STATE)
        self._blank = Coord(2, 2)
        if randomize:
            self.randomize()
        else:
            self.reset()

    def __repr__(self) -> str:
        squares = []
        for row in self.board:
            for val in row:
                str_val = str(val) if val else " "
                squares.append(str_val)
        return f"┌─┬─┬─┐\n│{squares[0]}│{squares[1]}│{squares[2]}│\n├─┼─┼─┤\n│{squares[3]}│{squares[4]}│{squares[5]}│\n├─┼─┼─┤\n│{squares[6]}│{squares[7]}│{squares[8]}│\n└─┴─┴─┘"

    def __eq__(self, other):
        if not isinstance(other, EightPuzzle):
            raise TypeError(f"Cannot compare type <class 'EightPuzzle'> to type {type(other)}.")
        return self.board == other.board

    def __hash__(self):
        return hash(tuple(self.board[0] + self.board[1] + self.board[2]))

    def reset(self):
        self.board = deepcopy(self.FINISH_STATE)
        return self
    
    # Coordinates for the blank space on the board.
    @property
    def blank(self) -> Coord:
        return self._blank
                
    # Coordinates for any specific tile.
    def find(self, value: int=None) -> Coord:
        if value not in set(self.board[0] + self.board[1] + self.board[2]):
            value = None
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x] == value:
                    return Coord(x, y)

    # Simple representation of the board class instance.
    def toString(self) -> str:
        out_str = "|"
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                out_str += " |" if self.board[y][x] == None else str(self.board[y][x]) + "|"
        return out_str
    
    # Single move methods.
    def moveLeft(self):
        b = self.blank
        if b.x < 2:
            self.board[b.y][b.x] = self.board[b.y][b.x+1]
            self.board[b.y][b.x+1] = None
            self._blank = Coord(b.x+1, b.y)
        return self
    
    def moveRight(self):
        b = self.blank
        if b.x > 0:
            self.board[b.y][b.x] = self.board[b.y][b.x-1]
            self.board[b.y][b.x-1] = None
            self._blank = Coord(b.x-1, b.y)
        return self
        
    def moveUp(self):
        b = self.blank
        if b.y < 2:
            self.board[b.y][b.x] = self.board[b.y+1][b.x]
            self.board[b.y+1][b.x] = None
            self._blank = Coord(b.x, b.y+1)
        return self
        
    def moveDown(self):
        b = self.blank
        if b.y > 0:
            self.board[b.y][b.x] = self.board[b.y-1][b.x]
            self.board[b.y-1][b.x] = None
            self._blank = Coord(b.x, b.y-1)
        return self
            
    # Method to randomize the board via random valid tile moves.
    # Starts at FINISH_STATE to ensure that the randomized board can be returned to FINISH_STATE.
    # https://en.wikipedia.org/wiki/15_Puzzle#Solvability
    def randomize(self, turns: int=100):
        self.reset()
        for _ in range(turns):
            movelist = []
            if self.blank.x < 2:
                movelist.append(self.moveLeft)
            if self.blank.x > 0:
                movelist.append(self.moveRight)
            if self.blank.y < 2:
                movelist.append(self.moveUp)
            if self.blank.y > 0:
                movelist.append(self.moveDown)
            move = choice(movelist)
            move()
        return self

    def solve(self):
        pass
    
if __name__ == "__main__":
    ep = EightPuzzle()
    print("Starting board:")
    print(ep)
    print(f"Completed in {ep.solve()} moves.")