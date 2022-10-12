'''
Conway's Game of Life takes place on an infinite two-dimensional board of square cells.
Each cell is either dead or alive, and at each tick, the following rules apply:

    Any live cell with less than two live neighbours dies.
    Any live cell with two or three live neighbours remains living.
    Any live cell with more than three live neighbours dies.
    Any dead cell with exactly three live neighbours becomes a live cell.

A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life.
It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for.
Once initialized, it should print out the board state at each step.
Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
'''

from typing import List, Tuple
import copy

def gameOfLife(coords : List[Tuple[int, int]], steps : int):
    def printBoard(board, grid):
        out_str = " |"
        for i in range(grid['min_x'], grid['max_x']):
            out_str += str(i)
        out_str += "\n"
        out_str += "-" * (grid['max_x'] - grid['min_x'] + 2) + '\n'
        for i in range(grid['min_y'], grid['max_y']):
            out_str += str(i) + '|'
            for j in range(grid['min_x'], grid['max_x']):
                out_str += board[i][j]
            out_str += '\n'
        print(out_str)
        return

    def checkCell(cell):
        return 1 if cell == '*' else 0

    def countLiveNeighbors(board, x, y):
        count = 0
        # spots off the board are considered dead. In this way we can exclude over-the-edge spaces in the count.
        left_end = x == 0
        right_end = x == len(board[0]) - 1
        top_end = y == 0
        bottom_end = y == len(board) - 1

        # Above
        if not top_end:
            if not left_end:
                count += checkCell(board[y-1][x-1])
            count += checkCell(board[y-1][x])
            if not right_end:
                count += checkCell(board[y-1][x+1])
        # Same Row
        if not left_end:
            count += checkCell(board[y][x-1])
        if not right_end:
            count += checkCell(board[y][x+1])
        # Below
        if not bottom_end:
            if not left_end:
                count += checkCell(board[y+1][x-1])
            count += checkCell(board[y+1][x])
            if not right_end:
                count += checkCell(board[y+1][x+1])

        return count

    def calculateGrid(board):
        min_x, min_y, max_x, max_y = len(board[0]), len(board), 0, 0
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == '*':
                    if x < min_x:
                        min_x = x
                    if x+1 > max_x:
                        max_x = x+1
                    if y < min_y:
                        min_y = y
                    if y > max_y:
                        max_y = y+1
        return {
            'min_x' : min_x,
            'min_y' : min_y,
            'max_x' : max_x,
            'max_y' : max_y,
        }

    # Get the initial size of the 2D list necessary.
    min_x, min_y = float('inf'), float('inf')
    max_x, max_y = 0, 0
    for live_cell in coords:
        if live_cell[0] < min_x:
            min_x = live_cell[0]
        if live_cell[1] < min_y:
            min_y = live_cell[1]
        if live_cell[0]+1 > max_x:
            max_x = live_cell[0]+1
        if live_cell[1]+1 > max_y:
            max_y = live_cell[1]+1
    
    # Build 2D list
    board = [['.' for i in range(0, max_x+1)] for j in range(0, max_y+1)]
    for live_cell in coords:
        board[live_cell[1]][live_cell[0]] = '*'
        
    print("Step 0")
    printBoard(board, {'min_x' : min_x, 'min_y' : min_y, 'max_x' : max_x, 'max_y' : max_y})

    for step in range(0, steps):
        new_board = copy.deepcopy(board)

        # Check Live/Dead Flips on current board
        for y in range(0, len(board)):
            for x in range(0, len(board[0])):
                # Any dead cell with exactly three live neighbours becomes a live cell.
                if board[y][x] == '.' and countLiveNeighbors(board, x, y) == 3:
                    new_board[y][x] = '*'
                    if x < min_x:
                        min_x = x
                    if y < min_y:
                        min_y = y
                # Any live cell with less than two or more than three live neighbours dies.
                elif board[y][x] == '*':
                    live_neighbors = countLiveNeighbors(board, x, y)
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_board[y][x] = '.'

        # Edge Checks
        # Right Edge
        right_edge = len(board[0])-1
        for y in range(1, len(board)-1):
            # If we have 3 adjacent live cells, add a new column to new_board if needed, then make the cell in row y a '*'
            if board[y-1][right_edge] == '*' and board[y][right_edge] == '*' and board[y+1][right_edge] == '*':
                if len(new_board[0]) == len(board[0]):
                    for i in range(0, len(new_board)):
                        new_board[i].append('.')
                new_board[y][len(board[0])] = '*'

        # Left Edge
        left_edge_shifted = False
        for y in range(1, len(board)-1):
            if board[y-1][0] == '*' and board[y][0] == '*' and board[y+1][0] == '*':
                if not left_edge_shifted:
                    for i in range(0, len(new_board)):
                        new_board[i].insert(0, '.')
                    left_edge_shifted = True
                new_board[y][0] = '*'

        # Bottom Edge
        bottom_edge = len(board)-1
        for x in range(1, len(board[0])-1):
            # If we have 3 adjacent live cells, add a new row to new_board if needed, then make the cell in column x a '*'
            if board[bottom_edge][x-1] == '*' and board[bottom_edge][x] == '*' and board[bottom_edge][x+1] == '*':
                if len(new_board) == len(board):
                    new_board.append(['.' for i in range(0, len(new_board[0]))])
                new_board[len(board)][x] = '*'

        # Top Edge
        top_edge_shifted = False
        for x in range(1, len(board[0])-1):
            if board[0][x-1] == '*' and board[0][x] == '*' and board[0][x+1] == '*':
                if not top_edge_shifted:
                    new_board.insert(0, ['.' for i in range(0, len(new_board[0]))])
                    top_edge_shifted = True
                new_board[0][x] = '*'

        board = new_board
        grid = calculateGrid(board)
        print("Step " + str(step + 1))
        printBoard(board, grid)
        
    return

gameOfLife([(3, 3), (3, 4), (4, 3), (4, 5), (4, 4)], 5)