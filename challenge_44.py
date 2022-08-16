'''
We can determine how "out of order" an array A is by counting the number of inversions it has.
Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions.
The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3).
The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.
'''

from typing import List, Tuple

def countInversions(arr: List) -> Tuple[List, int]:
    def mergeSortInv(arr1_info, arr2_info):
        arr1 = arr1_info[0]
        arr2 = arr2_info[0]
        inversions = arr1_info[1] + arr2_info[1]

        merged_arr = []
        i1 = i2 = 0

        while i1 < len(arr1) and i2 < len(arr2):
            if arr1[i1] < arr2[i2]:
                merged_arr.append(arr1[i1])
                i1 += 1
            else:
                merged_arr.append(arr2[i2])
                i2 += 1
                inversions += len(arr1[i1:])

        while i1 < len(arr1):
            merged_arr.append(arr1[i1])
            i1 += 1
        while i2 < len(arr2):
            merged_arr.append(arr2[i2])
            i2 += 1

        return merged_arr, inversions

    if len(arr) <= 1:
        return arr, 0

    middle = len(arr) // 2

    return mergeSortInv(countInversions(arr[:middle]), countInversions(arr[middle:]))


print(countInversions([2, 4, 1, 3, 5])[1])
print(countInversions([5, 4, 3, 2, 1])[1])