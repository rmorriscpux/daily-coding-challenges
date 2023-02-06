'''
Boggle is a game played on a 4 x 4 grid of letters.
The goal is to find as many words as possible that can be formed by a sequence of adjacent letters in the grid,
using each cell at most once. Given a game board and a dictionary of valid words, implement a Boggle solver.
'''

from typing import List, Set

ROWS = 4
COLS = 4

class TrieNode:
    def __init__(self, letter=None, data=None):
        self.word = data
        self.letter = letter
        self.children = {}

class WordTrie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str):
        if len(word) < 3:
            return self
        
        node_ptr = self.root
        for char in word:
            if char not in node_ptr.children:
                node_ptr[char] = TrieNode(letter=char)
            node_ptr = node_ptr[char]
        
        node_ptr.word = word
        
        return self

def boggleSolver(board: List[List[str]], word_file_name: str):
    def canTraverse(board: List[List[bool]], available: List[List[bool]], row: int, col: int, cur_letter: TrieNode):
        return ((0 <= row < ROWS) and (0 <= col < COLS) and available[row][col] and board[row][col] in cur_letter.children)

    def rBoggleSolver(board: List[List[str]], available: List[List[bool]], row: int, col: int, cur_letter: TrieNode, words_on_board: Set[str]):
        if cur_letter.word:
            words_on_board.add(cur_letter.word)

        # Special case for Q, which in Boggle is a "Qu" face. Go directly to 'U' child from the trie node.
        if cur_letter.letter == 'Q':
            rBoggleSolver(board, available, row, col, cur_letter.children['U'], words_on_board)
            return

        i, j = -1, -1

        while i < 2:
            if i == 0 and j == 0:
                j += 1

            if canTraverse(board, available, row+i, col+j, cur_letter):
                available[row+i][col+j] = False
                rBoggleSolver(board, available, row+i, col+j, cur_letter.children[board[row+i][col+j]])
                available[row+i][col+j] = True

            j += 1
            if j == 2:
                i += 1
                j = -1
        #NW
        # if canTraverse(board, available, row-1, col-1, cur_letter):
        #     available[row-1][col-1] = False
        #     rBoggleSolver(board, available, row-1, col-1, cur_letter.children[board[row-1][col-1]])
        #     available[row-1][col-1] = True

        # #N
        # if canTraverse(board, available, row-1, col, cur_letter):
        #     available[row-1][col] = False
        #     rBoggleSolver(board, available, row-1, col, cur_letter.children[board[row-1][col]])
        #     available[row-1][col] = True

        # #NE
        # if canTraverse(board, available, row-1, col+1, cur_letter):
        #     available[row-1][col+1] = False
        #     rBoggleSolver(board, available, row-1, col+1, cur_letter.children[board[row-1][col+1]])
        #     available[row-1][col+1] = True

        # #W
        # if canTraverse(board, available, row, col-1, cur_letter):
        #     available[row][col-1] = False
        #     rBoggleSolver(board, available, row, col-1, cur_letter.children[board[row][col-1]])
        #     available[row][col-1] = True

        # #E
        # if canTraverse(board, available, row, col+1, cur_letter):
        #     available[row][col+1] = False
        #     rBoggleSolver(board, available, row, col+1, cur_letter.children[board[row][col+1]])
        #     available[row][col+1] = True

        # #SW
        # if canTraverse(board, available, row+1, col-1, cur_letter):
        #     available[row+1][col-1] = False
        #     rBoggleSolver(board, available, row+1, col-1, cur_letter.children[board[row+1][col-1]])
        #     available[row+1][col-1] = True

        # #S
        # if canTraverse(board, available, row+1, col, cur_letter):
        #     available[row+1][col] = False
        #     rBoggleSolver(board, available, row-1, col-1, cur_letter.children[board[row+1][col]])
        #     available[row+1][col] = True

        # #SE
        # if canTraverse(board, available, row+1, col+1, cur_letter):
        #     available[row+1][col+1] = False
        #     rBoggleSolver(board, available, row+1, col+1, cur_letter.children[board[row+1][col+1]])
        #     available[row+1][col+1] = True

    # Build word database.
    word_db = WordTrie()
    with open(word_file_name, 'r') as word_file:
        for word in word_file:
            word_db.addWord(word.upper())

    words_on_board = set()
    available = [[True for j in board[i]] for i in range(0, len(board))]

    for row, letters in enumerate(board):
        for col, ltr in enumerate(letters):
            if ltr in word_db.root.children:
                available[row][col] = False
                rBoggleSolver(board, available, row, col, word_db.root.children[ltr], words_on_board)
                available[row][col] = True

    return words_on_board

if __name__ == "__main__":
    from random import randrange, shuffle

    BOGGLE_DICE = [
        ['A', 'A', 'E', 'E', 'G', 'N'],
        ['A', 'B', 'B', 'J', 'O', 'O'],
        ['A', 'C', 'H', 'O', 'P', 'S'],
        ['A', 'F', 'F', 'K', 'P', 'S'],
        ['A', 'O', 'O', 'T', 'T', 'W'],
        ['C', 'I', 'M', 'O', 'T', 'U'],
        ['D', 'E', 'I', 'L', 'R', 'X'],
        ['D', 'E', 'L', 'R', 'V', 'Y'],
        ['D', 'I', 'S', 'T', 'T', 'Y'],
        ['E', 'E', 'G', 'H', 'N', 'W'],
        ['E', 'E', 'I', 'N', 'S', 'U'],
        ['E', 'H', 'R', 'T', 'V', 'W'],
        ['E', 'I', 'O', 'S', 'S', 'T'],
        ['E', 'L', 'R', 'T', 'T', 'Y'],
        ['H', 'I', 'M', 'N', 'U', 'Q'],
        ['H', 'L', 'N', 'N', 'R', 'Z'],
    ]

    board = [[None for j in range(COLS)] for i in range(ROWS)]

    dice_order = list(range(0, ROWS * COLS))
    shuffle(dice_order)

    for i, place in enumerate(dice_order):
        board[place//COLS][place%COLS] = BOGGLE_DICE[i][randrange(0, len(BOGGLE_DICE[i]))]

### Print Board ###
    print("┌──" + "─┬──" * (COLS-1) + "─┐")
    for i, row in enumerate(board):
        row_str = "│"
        for ltr in row:
            row_str += f" {ltr} │"
        print(row_str)
        if i < ROWS-1:
            print("├──" + "─┼──" * (COLS-1) + "─┤")
    print("└──" + "─┴──" * (COLS-1) + "─┘")
### End Print Board ###