'''
You are given a 2 x N board, and instructed to completely cover the board with the following shapes:

Dominoes, or 2 x 1 rectangles.
Trominoes, or L-shapes.
For example, if N = 4, here is one possible configuration, where A is a domino, and B and C are trominoes.

A B B C
A B C C
Given an integer N, determine in how many ways this task is possible.
'''

# Solution with arrays.
def boardArrangement(N: int) -> int:
    def rBoardArrangement(board: list[list[bool]]) -> int:
        # Full board.
        if len(board[0]) == 0:
            return 1
        # One column left.
        elif len(board[0]) == 1:
            # One open space: Not a valid board config.
            if board[0][0] ^ board[1][0]:
                return 0
            # Both in column empty (just needs one vertical domino) or full.
            else:
                return 1
        # More than one column.
        count = 0
        # Case: First two columns are completely empty.
        if not any(board[0][:2] + board[1][:2]):
            # Add two horizontal dominoes.
            count += rBoardArrangement([board[0][2:], board[1][2:]])
            # Inserting an L-shaped tromino.
            board[0][1] = True
            count += rBoardArrangement([board[0][1:], board[1][1:]])
            board[0][1] = False
            # Inserting a r-shaped tromino.
            board[1][1] = True
            count += rBoardArrangement([board[0][1:], board[1][1:]])
            board[1][1] = False
        # Case: First column is completely empty.
        if not (board[0][0] or board[1][0]):
            # Insert vertical domino.
            count += rBoardArrangement([board[0][1:], board[1][1:]])
        # Case: Filled top in the first column.
        if board[0][0] and not (board[1][0] or board[0][1] or board[1][1]):
            # Inserting a J-shaped tromino.
            count += rBoardArrangement([board[0][2:], board[1][2:]])
            # Add horizontal domino to the bottom.
            board[1][1] = True
            count += rBoardArrangement([board[0][1:], board[1][1:]])
            board[1][1] = False
        # Case: Filled bottom in the first column.
        if board[1][0] and not (board[0][0] or board[0][1] or board[1][1]):
            # Inserting a 7-shaped tromino.
            count += rBoardArrangement([board[0][2:], board[1][2:]])
            # Add horizontal domino to the top.
            board[0][1] = True
            count += rBoardArrangement([board[0][1:], board[1][1:]])
            board[0][1] = False

        return count
    
    if N < 1:
        return 0
    
    board = [[False for i in range(N)] for j in range(2)]

    return rBoardArrangement(board)

# Solution without arrays.
def boardArrangement2(N: int):
    def rBoardArrangement2(remaining_cols: int, top: bool=False, bottom: bool=False) -> int:
        if remaining_cols == 0:
            return 1
        elif remaining_cols == 1:
            return int(not top ^ bottom)
        # if remaining_cols >= 2:
        count = 0

        if not (top or bottom):
            count += rBoardArrangement2(remaining_cols-2, False, False) # Add two horizontal dominoes
            count += rBoardArrangement2(remaining_cols-1, False, False) # Add vertical domino
            count += rBoardArrangement2(remaining_cols-1, True, False)  # Add 'r'-shaped tromino
            count += rBoardArrangement2(remaining_cols-1, False, True)  # Add 'L'-shaped tromino

        if top ^ bottom:
            count += rBoardArrangement2(remaining_cols-2, False, False)        # Add '7'-shaped or 'J'-shaped tromino
            count += rBoardArrangement2(remaining_cols-1, not top, not bottom) # Add horizontal domino on top or bottom

        return count
    
    if N < 1:
        return 0
    
    return rBoardArrangement2(N)

if __name__ == "__main__":
    print(boardArrangement(4))
    print(boardArrangement2(4))