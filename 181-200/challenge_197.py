'''
Given an array and a number k that's smaller than the length of the array, rotate the array to the right k elements in-place.
'''

def rotateArrayRight(arr: list, k: int):
    if not arr: # Empty array.
        return

    # Lists in Python are a mapping type. Use built-in list methods (no re-assignment) to modify the array in-place.
    for i in range(0, k % len(arr)):
        arr.insert(0, arr.pop())

arr = [1, 2, 3, 4, 5, 6]
rotateArrayRight(arr, 2)
print(arr)