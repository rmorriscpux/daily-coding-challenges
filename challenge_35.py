'''
Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first,
the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
'''

def segregateArray(rgb_list : list):
    # Assuming list is valid; i.e. all items are 'R', 'G', or 'B'.
    r_ptr = 0
    b_ptr = len(rgb_list) - 1
    traverse = 0

    # Set b_ptr to the first non-B value from the end.
    while b_ptr > 0:
        if rgb_list[b_ptr] != 'B':
            break
        b_ptr -= 1

    while r_ptr < b_ptr and traverse <= b_ptr:
        # Case: rgb_list[traverse] == 'R'.
        if rgb_list[traverse] == 'R':
            if traverse == r_ptr:
                # All values at and before r_ptr should be 'R' at this point. Don't swap any values, and increment traverse and r_ptr.
                traverse += 1
                r_ptr += 1
            elif traverse > r_ptr:
                # Swap values at traverse and r_ptr, then increment r_ptr
                temp = rgb_list[traverse]
                rgb_list[traverse] = rgb_list[r_ptr]
                rgb_list[r_ptr] = temp
                r_ptr += 1
            else:
                # Doubt we'll get here; sanity check.
                r_ptr = traverse
        # Case: rgb_list[traverse] == 'B': Swap, then decrement b_ptr
        elif rgb_list[traverse] == 'B':
            temp = rgb_list[traverse]
            rgb_list[traverse] = rgb_list[b_ptr]
            rgb_list[b_ptr] = temp
            b_ptr -= 1
        # Case: rgb_list[traverse] == 'G'
        else:
            traverse += 1

    return

my_rgb = ['G', 'B', 'R', 'R', 'B', 'R', 'G', 'B']
segregateArray(my_rgb)
print(my_rgb)