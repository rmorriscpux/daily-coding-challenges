'''
Connect 4 is a game where opponents take turns dropping red or black discs into a 7 x 6 vertically suspended grid.
The game ends either when one player creates a line of four consecutive discs of their color (horizontally,
vertically, or diagonally), or when there are no more spots left in the grid.

Design and implement Connect 4.
'''

import os

class Connect4:
    def __init__(self, play: bool=True):
        # Standard Connect 4 game is 7 columns and 6 rows. Modify the below two values here to customize the grid.
        self._COLS = 7
        self._ROWS = 6
        # The board is inverted from how matrices are typically represented, for ease of placing discs.
        self.board = [['open' for i in range(0, self._ROWS)] for j in range(0, self._COLS)]
        # Symbol map for printing the board.
        self._SYMBOLS = {
            'open' : " ",
            'Red' : "○",
            'Black' : "●"
        }
        # Counters for how many open spaces are left. Quicker than counting open spaces in a column every time an attempt at placing a disc is made.
        self._open_spaces = [self._ROWS for i in range(0, self._COLS)]
        # Plays automatically when instantiated.
        if play:
            self.start()

    # Prints a representation of the current Connect 4 board.
    def printBoard(self):
        # Clear terminal window. os.system('cls') is used for Windows ('nt') and os.system('clear') is used for Mac/Linux ('posix')
        os.system('cls') if os.name == 'nt' else os.system('clear')
        print("|" + "CONNECT 4".center(self._COLS * 4 - 1) + "|")
        print("|===" * self._COLS + "|")
        for i in range(0, self._ROWS):
            row_str = "|"
            for j in range(0, self._COLS):
                row_str += " " + self._SYMBOLS[self.board[j][i]] + " |"
            print(row_str)
            if i < self._ROWS - 1:
                print("|---" * self._COLS + "|")
        print("|===" * self._COLS + "|")
        return

    def playRound(self, color: str):
        # Subroutine to handle input.
        def inputHandler(color):
            print(f"{color}'s Turn.")
            input_col = input(f"Select Column 1-{self._COLS}: ")
            while not (input_col.isnumeric() and int(input_col) >= 1 and int(input_col) <= self._COLS):
                self.printBoard()
                print("Invalid Input.")
                print(f"{color}'s Turn.")
                input_col = input(f"Select Column 1-{self._COLS}: ")
            return int(input_col) - 1

        assert color in {'Red', 'Black'}
        self.printBoard()
        play_col = inputHandler(color)
        # Check that column is not full.
        while not self._open_spaces[play_col]:
            self.printBoard()
            print(f"Column {play_col+1} is full. Select again.")
            play_col = inputHandler(color)
        # With valid input, drop disc into corresponding column.
        self._open_spaces[play_col] -= 1
        self.board[play_col][self._open_spaces[play_col]] = color
        # Run evaluation.
        self.evaluate(self._open_spaces[play_col], play_col)

        return

    def evaluate(self, row: int, col: int):
        # To save time, evaluation only needs to be done starting with the last dropped disc.
        color = self.board[col][row]
        assert color in {'Red', 'Black'}
        win_flag = False

        # Horizontal
        count = 1
        col_ptr = col - 1
        while col_ptr >= 0 and self.board[col_ptr][row] == color:
            count += 1
            col_ptr -= 1
        col_ptr = col + 1
        while col_ptr < self._COLS and self.board[col_ptr][row] == color:
            count += 1
            col_ptr += 1
        if count >= 4:
            win_flag = True

        # Vertical
        if not win_flag:
            count = 1
            row_ptr = row - 1
            while row_ptr >= 0 and self.board[col][row_ptr] == color:
                count += 1
                row_ptr -= 1
            row_ptr = row + 1
            while row_ptr < self._ROWS and self.board[col][row_ptr] == color:
                count += 1
                row_ptr += 1
            if count >= 4:
                win_flag = True

        # Diagonal \
        if not win_flag:
            count = 1
            col_ptr = col - 1
            row_ptr = row - 1
            while col_ptr >= 0 and row_ptr >= 0 and self.board[col_ptr][row_ptr] == color:
                count += 1
                col_ptr -= 1
                row_ptr -= 1
            col_ptr = col + 1
            row_ptr = row + 1
            while col_ptr < self._COLS and row_ptr < self._ROWS and self.board[col_ptr][row_ptr] == color:
                count += 1
                col_ptr += 1
                row_ptr += 1
            if count >= 4:
                win_flag = True

        # Diagonal /
        if not win_flag:
            count = 1
            col_ptr = col - 1
            row_ptr = row + 1
            while col_ptr >= 0 and row_ptr < self._ROWS and self.board[col_ptr][row_ptr] == color:
                count += 1
                col_ptr -= 1
                row_ptr += 1
            col_ptr = col + 1
            row_ptr = row - 1
            while col_ptr < self._COLS and row_ptr >= 0 and self.board[col_ptr][row_ptr] == color:
                count += 1
                col_ptr += 1
                row_ptr -= 1
            if count >= 4:
                win_flag = True

        if win_flag:
            # Four-in-a-row found on the last player's turn. Game ends with that player winning.
            self.printBoard()
            print(f"{color} Wins!")
        elif all(map(lambda col: col == 0, self._open_spaces)):
            # Board is completely full. Game is a draw.
            self.printBoard()
            print("Draw!")
        else:
            # Continue game.
            next_color = 'Black' if color == 'Red' else 'Red'
            self.playRound(next_color)

        return

    # Sets up to start a new game. Fresh board, Red goes first.
    def start(self):
        self.board = [['open' for i in range(0, self._ROWS)] for j in range(0, self._COLS)]
        self._open_spaces = [self._ROWS for i in range(0, self._COLS)]
        self.playRound("Red")
        return

if __name__ == "__main__":
    Connect4()