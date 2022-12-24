'''
Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
'''

from typing import List

# Works in O(N^3) time and O(1) space.
def largestMultOfThree(int_list: List[int]):
    # NOTE: This function returns None when a list has less than 3 integers. One could also do a check and raise an exception for that case.
    max_product = None
    
    for i in range(0, len(int_list)-2):
        for j in range(i+1, len(int_list)-1):
            for k in range(j+1, len(int_list)):
                product = int_list[i] * int_list[j] * int_list[k]
                max_product = product if max_product == None else max(product, max_product)

    return max_product

print(largestMultOfThree([-10, -10, 5, 2]))
print(largestMultOfThree([10, -10, 5, 2]))

# Quicker solution.
def largestMultOfThreeQuick(int_list: List[int]):
    if len(int_list) < 3:
        raise IndexError("Not enough elements in list.")
    # Assuming O(n*log(n)) sort time.
    sorted_list = sorted(int_list)

    # Case: All negative.
    if sorted_list[-1] < 0:
        return sorted_list[-1] * sorted_list[-2] * sorted_list[-3]

    # Case: Highest value is 0.
    elif sorted_list[-1] == 0:
        return 0

    # Case: Positive integers exist.
    else:
        return max(sorted_list[-1] * sorted_list[-2] * sorted_list[-3], sorted_list[-1] * sorted_list[0] * sorted_list[1])

print(largestMultOfThreeQuick([-10, -10, 5, 2]))
print(largestMultOfThreeQuick([10, -10, 5, 2]))