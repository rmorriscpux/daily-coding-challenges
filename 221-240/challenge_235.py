'''
Given an array of numbers of length N, find both the minimum and maximum using less than 2 * (N - 2) comparisons.
'''

# A comparison in this case is one between two numbers. So, max(a, b, c) would require three comparisons, total (a to b, a to c, and b to c)

from typing import List

def getMinMax(num_arr: List[int]):
    # Quick helper function for doing the compare and ordering the numbers accordingly.
    num_compare = lambda n1, n2: (n1, n2) if n1 < n2 else (n2, n1)

    if len(num_arr) == 0:
        raise IndexError("List num_arr cannot be empty.")
    elif len(num_arr) == 1:
        return num_arr[0], num_arr[0]

    # First, split into two lists with the compare function. In the end min_list will contain the absolute min and max_list will contain the absolute max.
    min_list, max_list = [], []

    for i in range(0, len(num_arr), 2):
        if i == len(num_arr) - 1:
            # The list length is odd, so add the last number to both lists and sort it out later.
            min_list.append(num_arr[i])
            max_list.append(num_arr[i])
            break
        cur_numbers = num_compare(num_arr[i], num_arr[i+1])
        min_list.append(cur_numbers[0])
        max_list.append(cur_numbers[1])

    # To get the min and max, pare each list down using compares in the same way until there is only one item in each list.
    while len(min_list) > 1:
        new_min_list = []
        for i in range(0, len(min_list), 2):
            if i == len(min_list) - 1:
                # Odd list length, add last number to the new list.
                new_min_list.append(min_list[i])
                break
            cur_numbers = num_compare(min_list[i], min_list[i+1])
            new_min_list.append(cur_numbers[0])
        min_list = new_min_list

    while len(max_list) > 1:
        new_max_list = []
        for i in range(0, len(max_list), 2):
            if i == len(max_list) - 1:
                # Odd list length, add last number to the new list.
                new_max_list.append(max_list[i])
                break
            cur_numbers = num_compare(max_list[i], max_list[i+1])
            new_max_list.append(cur_numbers[1])
        max_list = new_max_list

    return min_list[0], max_list[0]

print(getMinMax([3, 0, 8, 6, 5, 2, 7, 9, 1, 4]))