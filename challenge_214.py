'''
Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.
'''

def longestConsecutiveOnes(n: int):
    n = abs(n)

    count, max_count = 0, 0
    while n > 0:
        if n % 2 == 1:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
        n >>= 1

    return max(count, max_count)

print(longestConsecutiveOnes(156))