'''
Write a function that rotates a list by k elements. For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2].
Try solving this without creating a copy of the list. How many swap or move operations do you need?
'''

def rotateList(in_list: list, k: int):
    # Non-rotatable list check.
    if len(in_list) <= 1:
        return in_list

    mod_k = k % len(in_list)

    return in_list[mod_k:] + in_list[:mod_k]

l = [1, 2, 3, 4, 5, 6]
print(l)
l = rotateList(l, 2)
print(l)