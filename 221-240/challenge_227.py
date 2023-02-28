'''
Boggle is a game played on a 4 x 4 grid of letters.
The goal is to find as many words as possible that can be formed by a sequence of adjacent letters in the grid,
using each cell at most once. Given a game board and a dictionary of valid words, implement a Boggle solver.
'''

# Word list referenced in this file courtesy of https://github.com/dwyl/english-words
# Format for word list text file: Single word on each line, case-insensitive.

from typing import List, Set

# Standard Boggle is 4x4. 5x5 and 6x6 variations also exist.
ROWS = 4
COLS = 4

# Classes to build a trie out of the word list.
class TrieNode:
    def __init__(self, letter=None):
        self.word = None
        self.letter = letter
        self.next_letters = {}

class WordTrie:
    def __init__(self, word_file_name: str = None):
        self.root = TrieNode()
        # Build the search dictionary if a file name is given.
        if word_file_name:
            try:
                with open(word_file_name, 'r') as word_file:
                    for word in word_file:
                        self.addWord(word.strip().upper())
            except FileNotFoundError:
                print(f"File '{word_file_name}' Not Found!")

    # Add a single word to the trie.
    def addWord(self, word: str):
        if len(word) < 3:
            return self
        
        node_ptr = self.root
        for char in word:
            if char not in node_ptr.next_letters:
                node_ptr.next_letters[char] = TrieNode(letter=char)
            node_ptr = node_ptr.next_letters[char]
        
        node_ptr.word = word
        
        return self

# Boggle solver function. Takes a Boggle board representation and a file name as arguments.
def boggleSolver(board: List[List[str]], word_file_name: str):
    # Shorthanding for determining if an adjacent square is valid and can be traversed to.
    def canTraverse(board: List[List[bool]], available: List[List[bool]], row: int, col: int, cur_letter: TrieNode):
        return ((0 <= row < ROWS) and (0 <= col < COLS) and available[row][col] and board[row][col] in cur_letter.next_letters)

    def rBoggleSolver(board: List[List[str]], available: List[List[bool]], row: int, col: int, cur_letter: TrieNode, words_on_board: Set[str]):
        # Add to the word set if the current node contains a word.
        if cur_letter.word:
            words_on_board.add(cur_letter.word)

        # Special case for Q, which in Boggle is a "Qu" face. Go directly to 'U' child from the trie node. Bypasses going to adjacent squares.
        if cur_letter.letter == 'Q':
            rBoggleSolver(board, available, row, col, cur_letter.next_letters['U'], words_on_board)
            return

        # Go through every adjacent square on the board that hasn't already been used.
        i, j = -1, -1

        while i < 2:
            # Skip the current location.
            if i == 0 and j == 0:
                j += 1

            if canTraverse(board, available, row+i, col+j, cur_letter):
                available[row+i][col+j] = False
                rBoggleSolver(board, available, row+i, col+j, cur_letter.next_letters[board[row+i][col+j]], words_on_board)
                available[row+i][col+j] = True

            j += 1
            if j == 2:
                i += 1
                j = -1

        return

    # Build word database.
    word_db = WordTrie(word_file_name)

    words_on_board = set()
    available = [[True for j in board[i]] for i in range(0, len(board))]

    # Run the recursive algorithm starting from every position on the board.
    for row, letters in enumerate(board):
        for col, ltr in enumerate(letters):
            if ltr in word_db.root.next_letters:
                available[row][col] = False
                rBoggleSolver(board, available, row, col, word_db.root.next_letters[ltr], words_on_board)
                available[row][col] = True

    return sorted(words_on_board)

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

    print(boggleSolver(board, "challenge_227_words.txt"))