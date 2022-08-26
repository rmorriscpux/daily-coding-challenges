'''
Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.
'''

from typing import List

def findWord(char_board: List[List[str]], word: str):

    def vertical_check(char_board, word, x, y):
        for i in range(0, len(word)):
            if word[i] != char_board[y+i][x]:
                return False
        return True

    x_limit = len(char_board[0]) - len(word)
    y_limit = len(char_board) - len(word)

    for i in range(0, len(char_board)):
        for j in range(0, len(char_board[0])):
            if j <= x_limit:
                if "".join(char_board[i][j:j+len(word)]) == word:
                    return True
            if i <= y_limit:
                if vertical_check(char_board, word, j, i):
                    return True
    
    return False

board = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']
]

assert findWord(board, "FOAM")
assert findWord(board, "MASS")
assert not findWord(board, "NEWS")