'''
Given an array of integers, determine whether it contains a Pythagorean triplet.
Recall that a Pythogorean triplet (a, b, c) is defined by the equation a^2 + b^2 = c^2.
'''

from typing import List

def hasPythTriplet(int_arr: List[int]):
    # Pre-multiply all integers in the list.
    square_arr = list(map(lambda n: n * n, int_arr))
    # Look for the sum of two squared list elements in the squared list.
    for i in range(0, len(square_arr)-1):
        for j in range(i+1, len(square_arr)):
            if square_arr[i] + square_arr[j] in square_arr:
                return True
    # Squared hypotenuse not found.
    return False

print(hasPythTriplet([5, 6, 7, 4, 3])) # 3^2 + 4^2 = 5^2
print(hasPythTriplet([6, 7, 4, 3, 10])) # No Pythagorean triplet.
print(hasPythTriplet([5, 6, 7, 4, -3])) # -3^2 + 4^2 = 5^2

# If wanted, it can be made so c is a different element than a or b.
# This only becomes important if an element in the input list is 0.

def hasPythTriplet2(int_arr: List[int]):
    # Pre-multiply all integers in the list.
    square_arr = list(map(lambda n: n * n, int_arr))
    # Look for the sum of two squared list elements in the squared list.
    for i in range(0, len(square_arr)-1):
        for j in range(i+1, len(square_arr)):
            if square_arr[i] + square_arr[j] in square_arr[:i] + square_arr[i+1:j] + square_arr[j+1:]: # This line modified.
                return True
    # Squared hypotenuse not found.
    return False

# print(hasPythTriplet2([5, 6, 7, 4, 3])) # 3^2 + 4^2 = 5^2
# print(hasPythTriplet2([6, 7, 4, 3, 10])) # No Pythagorean triplet.
# print(hasPythTriplet2([5, 6, 7, 4, -3])) # -3^2 + 4^2 = 5^2