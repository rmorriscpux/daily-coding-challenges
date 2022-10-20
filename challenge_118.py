'''
Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
'''

from typing import List

def sortedSquares(int_list: List[int]):
    square_list = []
    left_ptr = 0
    right_ptr = len(int_list) - 1

    while left_ptr <= right_ptr:
        if abs(int_list[left_ptr]) > abs(int_list[right_ptr]):
            square_list.insert(0, int_list[left_ptr] ** 2)
            left_ptr += 1
        else:
            square_list.insert(0, int_list[right_ptr] ** 2)
            right_ptr -= 1

    return square_list

print(sortedSquares([-9, -2, 0, 2, 3]))
print(sortedSquares([1, 2, 3, 4, 5]))
print(sortedSquares([-10, -8, -6, -4, -2]))
print(sortedSquares([]))