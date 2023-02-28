'''
Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer.
For example, given [10, 7, 76, 415], you should return 77641510.
'''

from typing import List

def largestPossibleInteger(int_list: List[int]):
    num_dict = {}

    for i in int_list:
        first_digit = str(i)[0]
        if first_digit not in num_dict:
            num_dict[first_digit] = []
        num_dict[first_digit].append(str(i))

    sorted_nums = sorted(num_dict.values(), key=lambda n: n[0], reverse=True)
    combined_nums = []
    for arr in sorted_nums:
        if len(arr) == 1:
            combined_nums.append(arr[0])
            continue

        split = {}
        for num in arr:
            num_len = len(num)
            if num_len not in split:
                split[num_len] = []
            split[num_len].append(num)

        sorted_vals = sorted(split.values(), key=lambda n: n[0])
        for val_arr in sorted_vals:
            combined_nums.extend(sorted(val_arr, reverse=True))
    
    return int("".join(combined_nums))

print(largestPossibleInteger([10, 7, 76, 415]))