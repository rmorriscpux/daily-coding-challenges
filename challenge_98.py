'''
Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where “adjacent” cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.
'''

from typing import List

def findWord(board: List[List[str]], word: str):
    def rFindWord(board, remaining_word, traversed, x, y):
        # End case.
        if len(remaining_word) == 0:
            return True

        traversed[y][x] = True

        word_found = False

        # Up
        if (y > 0 and
            remaining_word[0] == board[y-1][x] and
            not traversed[y-1][x]):
            word_found = rFindWord(board, remaining_word[1:], traversed, x, y-1)
            if word_found:
                return word_found

        # Left
        if (x > 0 and
            remaining_word[0] == board[y][x-1] and
            not traversed[y][x-1]):
            word_found = rFindWord(board, remaining_word[1:], traversed, x-1, y)
            if word_found:
                return word_found

        # Down
        if (y < len(board)-1 and
            remaining_word[0] == board[y+1][x] and
            not traversed[y+1][x]):
            word_found = rFindWord(board, remaining_word[1:], traversed, x, y+1)
            if word_found:
                return word_found

        # Right
        if (x < len(board[0])-1 and
            remaining_word[0] == board[y][x+1] and
            not traversed[y][x+1]):
            word_found = rFindWord(board, remaining_word[1:], traversed, x+1, y)
            if word_found:
                return word_found

        # Backtrack
        traversed[y][x] = False

        return word_found

    traversed = [[False for i in range(0, len(board[0]))] for j in range(0, len(board))]

    for y in range(0, len(board)):
        for x in range(0, len(board[0])):
            if board[y][x] == word[0]:
                if rFindWord(board, word[1:], traversed, x, y):
                    return True

    return False

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

print(findWord(board, "ABCCEDF"))
print(findWord(board, "SEE"))
print(findWord(board, "ABCB"))