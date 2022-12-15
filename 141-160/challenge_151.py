'''
Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C,
replace the color of the given pixel and all adjacent same colored pixels with C.

For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:

B B W
W W W
W W W
B B B

Becomes

B B G
G G G
G G G
B B B
'''

from typing import List, Tuple

def replaceColor(board: List[List[str]], C: str, coordinates: Tuple[int, int]):
    height = len(board)
    width = len(board[0])
    x, y = coordinates

    if x < 0 or x >= width or y < 0 or y >= height:
        raise IndexError("Coordinates out of range.")

    original_color = board[y][x]
    
    board[y][x] = C

    # Up
    if y > 0 and board[y-1][x] == original_color:
        replaceColor(board, C, (x, y-1))
    # Down
    if y < height-1 and board[y+1][x] == original_color:
        replaceColor(board, C, (x, y+1))
    # Left
    if x > 0 and board[y][x-1] == original_color:
        replaceColor(board, C, (x-1, y))
    # Right
    if x < width-1 and board[y][x+1] == original_color:
        replaceColor(board, C, (x+1, y))

    return

def printBoard(board: List[List[str]]):
    for row in board:
        row_str = ""
        for i, color in enumerate(row):
            row_str += color
            if i < len(row)-1:
                row_str += " "
        print(row_str)
    return

board = [
    ['B', 'B', 'W', 'B'],
    ['W', 'W', 'W', 'B'],
    ['W', 'W', 'W', 'W'],
    ['B', 'B', 'B', 'W'],
]

printBoard(board)
replaceColor(board, 'G', (2, 2))
print('--------')
printBoard(board)
print('--------')

board2 = [
    ['B', 'B', 'W', 'B', 'W', 'W'],
    ['W', 'W', 'W', 'B', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'B', 'W'],
    ['B', 'B', 'B', 'W', 'B', 'W'],
]

printBoard(board2)
replaceColor(board2, 'G', (2, 2))
print('--------')
printBoard(board2)