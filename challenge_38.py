'''
You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board
where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.
'''

# In chess, queens can move any number of spaces on the board in any cardinal or diagonal direction.

# Board is represented as a list built up to a length of N.
# Each index represents a row, and the number in each index represents the column where a queen is placed in that row.
# As the board list builds up, checks are made to ensure that each next queen placed does not threaten any other queens previously placed.
def arrangeQueens(N : int, board : list=[]):
    # Subroutine to check if a sub-board as laid out is valid.
    def isValid(sub_board):
        new_queen_row = len(sub_board) - 1
        new_queen_col = sub_board[-1]
        # If any queens from previous rows can attack the last queen placed, sub-board is invalid.
        for row, col in enumerate(sub_board[:-1]):
            col_diff = abs(new_queen_col - col)
            if col_diff == 0 or col_diff == new_queen_row - row: # New queen is in the same column or at a diagonal position from a previous queen.
                return False
        # Loop complete, sub-board is valid.
        return True

    # Sanity check on N
    if N < 0:
        return 0
    
    # Check if we have a complete board. At this point, we can add to the total arrangement count below.
    if N == len(board):
        return 1

    count = 0
    for col in range(N):
        board.append(col)
        if isValid(board):
            count += arrangeQueens(N, board)
        board.pop()
    return count

print(arrangeQueens(8))