'''
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

    10 = max(10, 5, 2)
    7 = max(5, 2, 7)
    8 = max(2, 7, 8)
    8 = max(7, 8, 7)

Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.
'''

# Effectively, the challenge is to do this with a single, unnested loop.

def max_val_in_subset(int_arr, k):
    # Get initial max_val and print.
    max_val = int_arr[0]
    for i in range(1, k):
        if int_arr[i] > max_val:
            max_val = int_arr[i]
    print(max_val)

    # Now pop out the first vals and shift, until the list length is k.
    while len(int_arr) > k:
        # If the max val was removed, check over the whole length.
        removed_val = int_arr.pop(0)
        if removed_val == max_val:
            max_val = int_arr[0]
            for i in range(1, k):
                if int_arr[i] > max_val:
                    max_val = int_arr[i]
        else: # Just need to check the new value.
            max_val = int_arr[k-1] if int_arr[k-1] > max_val else max_val
        # Now print.
        print(max_val)

max_val_in_subset([10, 5, 2, 7, 8, 7], 3)