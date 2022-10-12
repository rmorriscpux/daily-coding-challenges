'''
Given a number represented by a list of digits, find the next greater permutation of a number,in terms of lexicographic ordering.
If there is not greater permutation possible, return the permutation with the lowest value/ordering.

For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should return [2,1,3]. The list [3,2,1] should return [1,2,3].

Can you perform the operation without allocating extra memory (disregarding the input memory)?
'''

from typing import List

# This function modifies the list in-place.
def getNextPermutation(num_arr: List[int]):
    # End paramter needs to be the last index PLUS 1.
    def reverseSection(num_arr, start, end):
        for i in range(0, (end-start) // 2):
            temp = num_arr[start+i]
            num_arr[start+i] = num_arr[end-1-i]
            num_arr[end-1-i] = temp
    
    # Find where it stops increasing from back to front.
    start_index = len(num_arr) - 1
    for start_index in range(len(num_arr) - 1, 0, -1):
        if num_arr[start_index] >= num_arr[start_index-1]:
            break
    else:
        # If the loop completes, this means that the array is the highest ordering. Reverse the entire array and end.
        reverseSection(num_arr, 0, len(num_arr))
        return

    for i in range(len(num_arr) - 1, start_index - 1, -1):
        if num_arr[i] > num_arr[start_index-1]:
            temp = num_arr[i]
            num_arr[i] = num_arr[start_index-1]
            num_arr[start_index-1] = temp
            break

    reverseSection(num_arr, start_index, len(num_arr))
    
    return

a = [1, 2, 3, 4]
print(a)
for i in range(0, 24):
    getNextPermutation(a)
    print(a)