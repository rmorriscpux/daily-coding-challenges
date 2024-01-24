'''
Given an unsorted array, in which all elements are distinct, find a “peak” element in O(log N) time.

An element is considered a peak if it is greater than both its left and right neighbors.
It is guaranteed that the first and last elements are lower than all others.
'''

def findPeak(arr: list[int], begin: int=-1, end: int=-1) -> int:
    if begin == -1 or end == -1:
        begin = 0
        end = len(arr)

    pivot = (end - begin) // 2

    if pivot in {begin, end-1}:
        return None
    
    if arr[pivot] > arr[pivot-1] and arr[pivot] > arr[pivot+1]:
        return arr[pivot]
    
    left_peak = findPeak(arr, begin, pivot)
    if left_peak != None:
        return left_peak
    
    return findPeak(arr, pivot+1, end)

if __name__ == "__main__":
    print(findPeak([0, 5, 4, 3, 2, 1]))
    print(findPeak([0, 2, 3, 4, 5, 1]))