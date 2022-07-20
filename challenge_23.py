'''
You are given an M by N matrix consisting of booleans that represents a board.
Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps
required to reach the end coordinate from the start. If there is no possible path, then return null.
You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]

and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7,
since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
'''

# Takes in 2D boolean list 'board' and coordinate tuples 'start' and 'end' with 2 integers each
def shortestPath(board, start, end):
    # Recursive function. i and j are the current cell coordinates
    def rShortestPath(board, traversed, i, j, x, y, min_distance, cur_distance):
        # End condition
        if (i == x) and (j == y):
            min_distance[0] = cur_distance if cur_distance < min_distance[0] else min_distance[0]
            return

        traversed[i][j] = True
        
        # Up
        if isValidMove(board, traversed, i-1, j):
            rShortestPath(board, traversed, i-1, j, x, y, min_distance, cur_distance+1)
        # Down
        if isValidMove(board, traversed, i+1, j):
            rShortestPath(board, traversed, i+1, j, x, y, min_distance, cur_distance+1)
        # Left
        if isValidMove(board, traversed, i, j-1):
            rShortestPath(board, traversed, i, j-1, x, y, min_distance, cur_distance+1)
        # Right
        if isValidMove(board, traversed, i, j+1):
            rShortestPath(board, traversed, i, j+1, x, y, min_distance, cur_distance+1)

        traversed[i][j] = False
    
    # Conditions for a space that can be moved to:
    # - x and y coordinates are within the board.
    # - The space is not a wall.
    # - The space has not been traversed already.
    def isValidMove(board, traversed, x, y):
        can_move = ((x >= 0 and x < len(board)) and
            (y >= 0 and y < len(board[0])) and
            board[x][y] == False and
            traversed[x][y] == False)
        return can_move

    # Set Variables
    start_x, start_y = start
    end_x, end_y = end
    M = len(board)
    N = len(board[0])

    # Set Traversed board
    traversed = [[False for j in range(0, N)] for i in range(0, M)]

    # Set distance
    distance = [2147483647] # Arbitrarily high number.

    rShortestPath(board, traversed, start_x, start_y, end_x, end_y, distance, 0)

    if distance[0] < 2147483647:
        return distance[0]
    return None

board = [
    [False, False, False, False],
    [True, True, False, True],
    [False, False, False, False],
    [False, False, False, False],
]

print(shortestPath(board, (4, 0), (0, 0)))