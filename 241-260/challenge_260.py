'''
The sequence [0, 1, ..., N] has been jumbled, and the only clue you have for its order is an array representing whether each number is larger or smaller than the last.
Given this information, reconstruct an array that is consistent with it. For example, given [None, +, +, -, +], you could return [1, 2, 3, 0, 4].
'''

def deduceNumArray(key_arr: list):
    assert key_arr[0] == None and all(map(lambda s: s in ['+', '-'], key_arr[1:]))
    # Setup. Lower bound is 0, upper bound is N-1.
    num_arr = []
    min_num = 0
    max_num = len(key_arr) - 1

    for key in key_arr[:0:-1]: # Loop through the input array in reverse, omitting the first element (None)
        if key == '+':
            # Insert max_num at the start of num_arr and decrement max_num.
            num_arr.insert(0, max_num)
            max_num -= 1
        elif key == '-':
            # Insert min_num at the start of num_arr and incrment min_num.
            num_arr.insert(0, min_num)
            min_num += 1
    # At the end, min_num == max_num.
    num_arr.insert(0, min_num)

    return num_arr

print(deduceNumArray([None, '+', '+', '-', '+']))