'''
Given a pivot x, and a list lst, partition the list into three parts.

    The first part contains all elements in lst that are less than x
    The second part contains all elements in lst that are equal to x
    The third part contains all elements in lst that are larger than x

Ordering within a part can be arbitrary.

For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14].
'''

from typing import List

# Creates new pivoted list.
def pivotList(x: int, lst: List[int]):
    partitioned_list = [[], [], []]
    for k in lst:
        if k < x:
            partitioned_list[0].append(k)
        elif k == x:
            partitioned_list[1].append(k)
        else: # k > x
            partitioned_list[2].append(k)

    return partitioned_list[0] + partitioned_list[1] + partitioned_list[2]

# Pivots the input list in-place.
def pivotListInPlace(x: int, lst: List[int]):
    cur_index = 0

    for i in range(0, len(lst)):
        if lst[cur_index] < x:
            lst.insert(0, lst.pop(cur_index))
            cur_index += 1
        elif lst[cur_index] == x:
            cur_index += 1
        else: # lst[cur_index] > x
            lst.append(lst.pop(cur_index))

    return

lst1 = [9, 12, 3, 5, 14, 10, 10]
print(lst1)
print(pivotList(10, lst1))

print("---")

lst2 = [9, 12, 3, 5, 14, 10, 10]
print(lst2)
pivotListInPlace(10, lst2)
print(lst2)