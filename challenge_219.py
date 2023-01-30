'''
Connect 4 is a game where opponents take turns dropping red or black discs into a 7 x 6 vertically suspended grid.
The game ends either when one player creates a line of four consecutive discs of their color (horizontally,
vertically, or diagonally), or when there are no more spots left in the grid.

Design and implement Connect 4.
'''

import os

# Custom exception name to raise when a selected column is full.
class ColumnFullError(Exception):
    pass

class Connect4:
    def __init__(self, play: bool=True):
        # Standard Connect 4 game is 7 columns and 6 rows. Modify the below two values here to customize the grid.
        # These values should be greater than or equal to 4 for the game to work properly. Also, values much higher than standard will cause issues with displaying.
        self._COLS = 7
        self._ROWS = 6
        # The board is inverted from how matrices are typically represented for ease of placing discs.
        self.board = [['open' for i in range(0, self._ROWS)] for j in range(0, self._COLS)]
        # Symbol map for printing the board.
        self._SYMBOLS = {
            'open' : " ",
            'Red' : "○",
            'Black' : "●"
        }
        # Counters for how many open spaces are left. Quicker than counting open spaces in a column every time an attempt at placing a disc is made.
        self._open_spaces = [self._ROWS for i in range(0, self._COLS)]
        # Plays automatically when instantiated by default.
        if play:
            self.start()

    # Prints a representation of the current Connect 4 board.
    def printBoard(self):
        # Clear terminal window. 'cls' is used for Windows (os.name == 'nt') and 'clear' is used for Mac/Linux/ChromeOS (os.name == 'posix')
        os.system('cls') if os.name == 'nt' else os.system('clear')
        # Title
        print("|" + "CONNECT 4".center(self._COLS * 4 - 1) + "|")
        # Column headers
        col_label_str = "|"
        for j in range(1, self._COLS+1):
            col_label_str += str(j).center(3) + "|"
        print(col_label_str)
        print("|===" * self._COLS + "|")
        # Grid
        for i in range(0, self._ROWS):
            row_str = "|"
            for j in range(0, self._COLS):
                row_str += " " + self._SYMBOLS[self.board[j][i]] + " |"
            print(row_str)
            if i < self._ROWS - 1:
                print("|---" * self._COLS + "|")
        # Board Bottom
        print("|===" * self._COLS + "|")
        return

    # Play one turn.
    # Note: Be careful! The board's lists are 0-indexed, but the display and interaction are 1-indexed.
    def playRound(self, color: str):
        # Subroutine to handle input. Will rerun until an input representing a valid move is entered.
        def inputHandler(color, err_msg=None):
            self.printBoard()
            if err_msg:
                print(err_msg)
            print(f"{color}'s turn.")
            try:
                # Input must be resolvable to an integer. ValueError is raised if it is not.
                play_col = int(input(f"Select Column 1-{self._COLS}: ")) - 1
                # Integer value must be within the columns on the board.
                if not (0 <= play_col < self._COLS):
                    raise ValueError
                # Cannot place disc if the column is already full.
                if self._open_spaces[play_col] == 0:
                    raise ColumnFullError

            except ValueError:
                play_col = inputHandler(color, f"Invalid Input. Must be an integer between 1 and {self._COLS}")

            except ColumnFullError:
                play_col = inputHandler(color, f"Column {play_col+1} is full. Select again.")

            return play_col

        # Sanity check.
        assert color in {'Red', 'Black'}
        # Get input and drop disc into corresponding column.
        play_col = inputHandler(color)
        self._open_spaces[play_col] -= 1
        self.board[play_col][self._open_spaces[play_col]] = color
        # Run evaluation.
        self.evaluate(self._open_spaces[play_col], play_col)

        return

    # Routine to evaluate the board for a win after a player's turn.
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

        # \ Diagonal
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

        # / Diagonal
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
        elif sum(self._open_spaces) == 0:
            # Board is completely full. Game ends in a draw.
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
        if sum(self._open_spaces) <= 0:
            raise ValueError("_ROWS and/or _COLS values are invalid. Check Connect4 class definition.")
        self.playRound("Red")
        return

if __name__ == "__main__":
    Connect4()