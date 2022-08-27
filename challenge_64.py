'''
A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N chessboard.
'''

class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if type(other) != Position:
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

def countKnightsTours(N: int):
    # Invalid Boards
    if N <= 0:
        return 0

    def rCountKnightsTours(N, start_pos, visited_pos):
        # Completed Tour: All positions visited.
        if len(visited_pos) == N * N:
            return 1

        # The knight moves 1 position straight then 1 position diagonal on a chess board. Represent these position deltas in a list of tuples.
        knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        # Now build a list of possible moves on the board, omitting any positions the knight already visited.
        valid_moves = []
        for i, j in knight_moves:
            new_pos = Position(start_pos.x + i, start_pos.y + j)
            if (new_pos.x >= 0 and new_pos.x < N and
                new_pos.y >= 0 and new_pos.y < N and
                new_pos not in visited_pos):
                valid_moves.append(new_pos)

        # Now get the count by recurring into the routine adding each valid move.
        count = 0
        for move in valid_moves:
            count += rCountKnightsTours(N, move, visited_pos.union(set([move])))

        return count

    count = 0
    for i in range(0, N):
        for j in range(0, N):
            start = Position(i, j)
            count += rCountKnightsTours(N, start, set([start]))

    return count

# Note: This gets very time intensive. O((N^2)!)
print(countKnightsTours(1))
print(countKnightsTours(2))
print(countKnightsTours(3))
print(countKnightsTours(4))
print(countKnightsTours(5))