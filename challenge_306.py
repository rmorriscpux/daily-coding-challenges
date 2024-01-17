'''
You are given a list of N numbers, in which each number is located at most k places away from its sorted position.
For example, if k = 1, a given element at index 4 might end up at indices 3, 4, or 5.

Come up with an algorithm that sorts this list in O(N log k) time.
'''

from math import ceil

def kSort(N: list[int], k: int) -> list[int]:
    def sortSubList(sub_list: list[int]):
        if len(sub_list) <= 1:
            return sub_list
        
        pivot = ceil(len(sub_list) / 2)
        l1 = sortSubList(sub_list[:pivot])
        l2 = sortSubList(sub_list[pivot:])

        out_list = []
        while l1 and l2:
            if l1[0] < l2[0]:
                out_list.append(l1.pop(0))
            else:
                out_list.append(l2.pop(0))
        if l1:
            out_list.extend(l1)
        if l2:
            out_list.extend(l2)
        return out_list
    
    sorted_n = N.copy()
    k = min(k, len(N))

    for start_i in range(0, len(N) - k + 1):
        sorted_n = sorted_n[:start_i] + sortSubList(sorted_n[start_i:start_i+k+1]) + sorted_n[start_i+k+1:]

    return sorted_n

if __name__ == "__main__":
    print(kSort([1, 2, 0, 5, 4, 3], 2))