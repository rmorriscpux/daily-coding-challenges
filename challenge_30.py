'''
You are given an array of non-negative integers that represents a two-dimensional elevation map
where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index
(we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
'''

def waterFilled(height_array):
    # The trick is to alternate approaches from the beginning and the end, going from low to high.
    # Start from the lowest height, switch when a wall higher than the other side is reached.
    left_ptr = 0
    right_ptr = len(height_array) - 1

    fill_amount = 0

    max_left = 0
    max_right = 0

    while left_ptr <= right_ptr:
        if height_array[left_ptr] <= height_array[right_ptr]:
            # The left-side wall is lower or the same height. Approach from the left.
            if height_array[left_ptr] >= max_left:
                # Shift the maximum height on the left side to where left_ptr is now.
                max_left = height_array[left_ptr]
            else:
                # height at left_ptr is lower than the current max height. Add to the fill.
                fill_amount += max_left - height_array[left_ptr]
            left_ptr += 1
        else:
            # The right side wall is lower. Approach from the right.
            if height_array[right_ptr] >= max_right:
                # Shift the maximum height on the right side to where right_ptr is now.
                max_right = height_array[right_ptr]
            else:
                # Height at right_ptr is lower than the current max height. Add to the fill.
                fill_amount += max_right - height_array[right_ptr]
            right_ptr -= 1

    return fill_amount

print(waterFilled([3, 0, 1, 4, 0, 5, 0, 2]))