'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6]
'''

def mult_array_around_i(int_arr): # Note: Input cleanse omitted for brevity.
    # Initialize output array.
    mult_arr = []
    # Nested for loop that multiplies through the input array.
    for i in range(0, len(int_arr)):
        # Initialize 
        cur_mult = 1
        for j in range(0, len(int_arr)):
            # Check that the current iteration doesn't match the parent iteration before multiplying.
            if i != j:
                cur_mult = cur_mult * int_arr[j]
        mult_arr.append(cur_mult)
    
    return mult_arr

print(mult_array_around_i([1, 2, 3, 4, 5]))
print(mult_array_around_i([3, 2, 1]))
print(mult_array_around_i([3, 2, -1]))