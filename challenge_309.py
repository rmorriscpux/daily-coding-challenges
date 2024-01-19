'''
There are M people sitting in a row of N seats, where M < N.
Your task is to redistribute people such that there are no gaps between any of them,
while keeping overall movement to a minimum.

For example, suppose you are faced with an input of [0, 1, 1, 0, 1, 0, 0, 0, 1],
where 0 represents an empty seat and 1 represents a person. In this case,
one solution would be to place the person on the right in the fourth seat.
We can consider the cost of a solution to be the sum of the absolute distance each person must move, so that the cost here would be 5.

Given an input such as the one above, return the lowest possible cost of moving people to remove all gaps.
'''

from itertools import permutations

def lowestReseatCost(seats: list[int]) -> int:
    # List of all 0 and 1 values.
    assert all(map(lambda x: x in {0, 1}, seats))
    # M = Number of people. N = Number of seats.
    M, N = sum(seats), len(seats)
    if M in {0, 1, N}:
        # Empty, single occupant, or full. No moves needed.
        return 0

    occupied_seats = set([i for i, s in enumerate(seats) if s])

    lowest_moves = float('inf')
    # Go through every sub-list of adjacent seats with length equal to M.
    for offset in range(0, N-M+1):
        sub_seats = set(range(offset, M+offset)) # Indices of the current sub-list.
        occupied_sub_seats = occupied_seats.intersection(sub_seats) # Indices of seats within the sub-list with a person in them.
        # Check for the case where all occupants are already adjacent, hence no moves needed.
        if sub_seats == occupied_sub_seats:
            return 0
        occupied_out_seats = list(occupied_seats.difference(occupied_sub_seats)) # Indices of seats outside the sub-list with a person in them.
        vacant_sub_seats = list(sub_seats.difference(occupied_sub_seats)) # Indices of seats within the sub-list that are vacant.
        # Count the distance moved for every iteration of the order of people outside the sub-list moving to vacant indices within the sub-list.
        for move_order in permutations(range(len(vacant_sub_seats))):
            moves = 0
            for i in range(len(vacant_sub_seats)):
                moves += abs(vacant_sub_seats[i] - occupied_out_seats[move_order[i]])
            # Compare the moves for this iteration with the current lowest_moves value.
            lowest_moves = min(lowest_moves, moves) if lowest_moves else moves
    # If we get to this point and lowest_moves is still infinity, something is wrong.
    assert isinstance(lowest_moves, int)
    return lowest_moves

if __name__ == "__main__":
    print(lowestReseatCost([0, 1, 1, 0, 1, 0, 0, 0, 1])) # 5
    print(lowestReseatCost([0, 0, 0, 0, 0, 1, 1, 1, 1])) # 0
    print(lowestReseatCost([1, 1, 1, 1, 0, 0, 0, 0, 0])) # 0
    print(lowestReseatCost([0, 1, 1, 1, 1, 0, 0, 0, 0])) # 0