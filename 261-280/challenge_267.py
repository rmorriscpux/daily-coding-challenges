'''
You are presented with an 8 by 8 matrix representing the positions of pieces on a chess board.
The only pieces on the board are the black king and various white pieces. Given this matrix, determine whether the king is in check.

For details on how each piece moves, see here: https://en.wikipedia.org/wiki/Chess_piece#Moves_of_the_pieces

For example, given the following matrix:

...K....
........
.B......
......P.
.......R
..N.....
........
.....Q..

You should return True, since the bishop is attacking the king diagonally.
'''

from typing import List

MAX_SIZE = 8

# LEGEND
# BK - Black King
# K - White King
# Q = Queen
# B - Bishop
# N - Knight
# R - Rook
# P - Pawn
# . - Empty

def isKingInCheck(board: List[List[str]]):
    def attackable(board: List[List[str]], piece: str, x: int, y: int, bk_x: int, bk_y: int):
        is_attackable = False
        # King attacks over one space in any direction.
        if piece == 'K':
            is_attackable = (bk_x in [x-1, x, x+1]) and (bk_y in [y-1, y, y+1])
        # Queen attacks over any number of empty spaces in any direction.
        elif piece == 'Q':
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if i == 0 and j == 0:
                        continue
                    pos_x, pos_y = x+j, y+i
                    while 0 <= pos_x < MAX_SIZE and 0 <= pos_y < MAX_SIZE:
                        if pos_x == bk_x and pos_y == bk_y:
                            is_attackable = True
                        if board[pos_y][pos_x] != '.':
                            break
                        pos_x += j
                        pos_y += i
                    if is_attackable:
                        break
                if is_attackable:
                    break
        # Bishop attacks over any number of empty spaces in any diagonal direction.
        elif piece == 'B':
            for i in [-1, 1]:
                for j in [-1, 1]:
                    pos_x, pos_y = x+j, y+i
                    while 0 <= pos_x < MAX_SIZE and 0 <= pos_y < MAX_SIZE:
                        if pos_x == bk_x and pos_y == bk_y:
                            is_attackable = True
                        if board[pos_y][pos_x] != '.':
                            break
                        pos_x += j
                        pos_y += i
                    if is_attackable:
                        break
                if is_attackable:
                    break
        # Knight attacks a position one space cardinal plus one space diagonal.
        elif piece == 'N':
            is_attackable = ((bk_x == x+1 and bk_y == y+2) or
                             (bk_x == x+2 and bk_y == y+1) or
                             (bk_x == x+2 and bk_y == y-1) or
                             (bk_x == x+1 and bk_y == y-2) or
                             (bk_x == x-1 and bk_y == y+2) or
                             (bk_x == x-2 and bk_y == y+1) or
                             (bk_x == x-2 and bk_y == y-1) or
                             (bk_x == x-1 and bk_y == y-2))
        # Rook attacks over any number of spaces in any cardinal direction.
        elif piece == 'R':
            if x == bk_x:
                for i in [-1, 1]:
                    pos_y = y+i
                    while 0 <= pos_y < MAX_SIZE:
                        if pos_y == bk_y:
                            is_attackable = True
                        if board[pos_y][x] != '.':
                            break
                        pos_y += i
                    if is_attackable:
                        break
            if y == bk_y:
                for j in [-1, 1]:
                    pos_x = x+j
                    while 0 <= pos_x < MAX_SIZE:
                        if pos_x == bk_x:
                            is_attackable = True
                        if board[y][pos_x] != '.':
                            break
                        pos_x += j
                    if is_attackable:
                        break
        # Pawn attacks over one space in a forward diagonal direction.
        elif piece == "P":
            is_attackable = bk_y == y-1 and (bk_x == x-1 or bk_x == x+1)

        return is_attackable
    
    # Locate Black King
    for bk_y in range(0, MAX_SIZE):
        bk_found = False
        for bk_x in range(0, MAX_SIZE):
            if board[bk_y][bk_x] == "BK":
                bk_found = True
                break
        if bk_found:
            break
    else:
        return False # No BK on board.
    
    for y in range(0, MAX_SIZE):
        for x in range(0, MAX_SIZE):
            if board[y][x] in ['K', 'Q', 'B', 'N', 'R', 'P']:
                if attackable(board, board[y][x], x, y, bk_x, bk_y):
                    return True
                
    return False

board = [['.' for x in range(0, MAX_SIZE)] for y in range(0, MAX_SIZE)]

board[0][3] = 'BK'
board[3][6] = 'P'
board[4][7] = 'R'
board[5][2] = 'N'
board[7][5] = 'Q'

# board[1][3] = 'K' # Test King
# board[7][3] = 'Q' # Test Queen
# board[2][1] = 'B' # Test Bishop
# board[1][1] = 'N' # Test Knight
# board[0][6] = 'R' # Test Rook
# board[1][4] = 'P' # Test Pawn

print(isKingInCheck(board))