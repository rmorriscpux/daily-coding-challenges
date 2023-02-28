'''
One way to unlock an Android phone is through a pattern of swipes across a 1-9 keypad.

For a pattern to be valid, it must satisfy the following:

All of its keys must be distinct.
It must not connect two keys by jumping over a third key, unless that key has already been used.
For example, 4 - 2 - 1 - 7 is a valid pattern, whereas 2 - 1 - 7 is not.

Find the total number of valid unlock patterns of length N, where 1 <= N <= 9.
'''

# Note: The pattern swipe unlock I've seen on Android phones is a 3x3 grid of dots, not a keypad display.

def validUnlockCount(N: int) -> int:
    # Mapping blocking numbers to the numbers they block from the current position. (e.g. From 1: 2 blocks 3, 4 blocks 7, and 5 blocks 9)
    BLOCKERS = {
        1: {(2, 3), (4, 7), (5, 9)},
        2: {(5, 8)},
        3: {(2, 1), (5, 7), (6, 9)},
        4: {(5, 6)},
        5: {},
        6: {(5, 4)},
        7: {(4, 1), (5, 3), (8, 9)},
        8: {(5, 2)},
        9: {(5, 1), (6, 3), (8, 7)}
    }

    def rValidUnlockCount(remaining_moves: int, location: int, nums_used: set) -> int:
        # End case.
        if remaining_moves == 0:
            return 1

        # Determine what next moves are available. Cannot move to a number used, nor to the current location itself.
        valid_moves = set(BLOCKERS.keys()).difference({location}, nums_used)
        # Only remove blocked numbers if the blocking number hasn't been used yet.
        for block_pair in BLOCKERS[location]:
            if block_pair[0] not in nums_used:
                valid_moves.discard(block_pair[1])

        # Add location to nums_used and count all valid combinations from there. Remove location from nums_used afterward, otherwise it will permeate.
        sub_count = 0
        nums_used.add(location)
        for move in valid_moves:
            sub_count += rValidUnlockCount(remaining_moves-1, move, nums_used)
        nums_used.remove(location)

        return sub_count

    assert 1 <= N <= 9
    # Call subroutine from every starting position, 1 through 9.
    count = 0
    for start in range(1, 10):
        count += rValidUnlockCount(N-1, start, set())

    return count
    
print(validUnlockCount(1))
print(validUnlockCount(2))
print(validUnlockCount(3))
print(validUnlockCount(4))
print(validUnlockCount(5))
print(validUnlockCount(6))
print(validUnlockCount(7))
print(validUnlockCount(8))
print(validUnlockCount(9))