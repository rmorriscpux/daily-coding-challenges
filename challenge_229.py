'''
Snakes and Ladders is a game played on a 10 x 10 board, the goal of which is get from square 1 to square 100.
On each turn players will roll a six-sided die and move forward a number of spaces equal to the result.
If they land on a square that represents a snake or ladder, they will be transported ahead or behind, respectively, to a new square.

Find the smallest number of turns it takes to play snakes and ladders.

For convenience, here are the squares representing snakes and ladders, and their outcomes:

snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
'''

def minTurnsSNL():
    # Board layout.
    SNAKES = {
        16: 6, 
        48: 26, 
        49: 11, 
        56: 53, 
        62: 19, 
        64: 60, 
        87: 24, 
        93: 73, 
        95: 75, 
        98: 78
    }

    LADDERS = {
        1 : 38, 
        4 : 14, 
        9 : 31, 
        21: 42, 
        28: 84, 
        36: 44, 
        51: 67, 
        71: 91, 
        80: 100
    }

    def rMinTurnsSNL(space=0, turn_number=0):
        # End of the board.
        if space >= 100:
            return turn_number

        # Count down from 6 past the current space until finding a space without a snake head.
        new_space = space + 6
        while new_space in SNAKES:
            new_space -= 1
            if new_space == space:
                # Case where all spaces 1-6 ahead contain a snake. A board would not have this since it results in a dead end.
                raise ArithmeticError("Game board contains a dead end.")

        # Build move_candidates list with the top of all reachable ladder bottom spaces.
        move_candidates = [rMinTurnsSNL(LADDERS[i], turn_number+1) for i in range(space+1, new_space+1) if i in LADDERS]

        # Get the furthest position without a snake head or ladder bottom and add that to the list, if applicable.
        while (new_space in SNAKES or new_space in LADDERS) and new_space > space:
            new_space -= 1
        if new_space > space:
            move_candidates.append(rMinTurnsSNL(new_space, turn_number+1))

        # Result is the minimum of all recursive results.
        return min(move_candidates)

    # Optional: Check that no space contains both a snake head and ladder bottom.
    assert not set(SNAKES.keys()).intersection(set(LADDERS.keys()))

    return rMinTurnsSNL()

print(minTurnsSNL())