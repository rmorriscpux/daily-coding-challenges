'''
A knight is placed on a given square on an 8 x 8 chessboard. It is then moved randomly several times,
where each move is a standard knight move. If the knight jumps off the board at any point, however, it is not allowed to jump back on.

After k moves, what is the probability that the knight remains on the board?
'''

from typing import NamedTuple

DIM_SIZE = 8

class Position(NamedTuple):
    x: int
    y: int

    # Addition method for position.
    def move(self, delta):
        assert isinstance(delta, Position)
        return Position(self.x + delta.x, self.y + delta.y)
    
    def isOnBoard(self) -> bool:
        return all([self.x >= 0, self.x < DIM_SIZE, self.y >= 0, self.y < DIM_SIZE])
    
KNIGHT_MOVES = (
    Position(-2, -1),
    Position(-2, 1),
    Position(-1, -2),
    Position(-1, 2),
    Position(1, -2),
    Position(1, 2),
    Position(2, -1),
    Position(2, 1)
)

def knightPlacement(start: Position, k: int) -> float:
    def rKnightPlacement(pos: Position, remaining_k: int) -> float:
        # No moves left and knight is on the board. Return 1.
        if remaining_k == 0:
            return 1.0
        
        on_board_prob = 0.0
        for knight_move in KNIGHT_MOVES:
            next_pos = pos.move(knight_move)
            # Add the probability from the next position divided by the total number of knight moves if the next position is on the board.
            if next_pos.isOnBoard():
                on_board_prob += rKnightPlacement(next_pos, remaining_k-1) / len(KNIGHT_MOVES)

        return on_board_prob
    
    # For when the knight starts off the board.
    if not start.isOnBoard():
        return 0.0
    
    return rKnightPlacement(start, max(0, k))

if __name__ == "__main__":
    print(knightPlacement(Position(3, 3), 1)) # 1.0
    print(knightPlacement(Position(0, 0), 3)) # 0.125
    print(knightPlacement(Position(0, 3), 2)) # 0.40625