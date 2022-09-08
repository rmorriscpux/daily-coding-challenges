'''
You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns that can be removed to ensure that each row is ordered from top to bottom lexicographically. That is, the letter at each column is lexicographically later as you go down each row. It does not matter whether each row itself is ordered lexicographically.

For example, given the following table:

cba
daf
ghi

This is not ordered because of the a in the center. We can remove the second column to make it ordered:

ca
df
gi

So your function should return 1, since we only needed to remove 1 column.

As another example, given the following table:

abcdef

Your function should return 0, since the rows are already ordered (there's only one row).

As another example, given the following table:

zyx
wvu
tsr

Your function should return 3, since we would need to remove all the columns to order it.
'''

from typing import List

def numColumnsToRemove(char_matrix: List[List[str]]):
    # Assuming input matrix values are all single character strings.
    # Other languages like C++ and Java have primitive 'char' types that can ensure this.

    count = 0
    for column in range(0, len(char_matrix[0])):
        for row in range(1, len(char_matrix)):
            if char_matrix[row-1][column] > char_matrix[row][column]:
                count += 1
                break
    return count

# List of strings version.
# Assume all strings are of equal length.
def numLettersToRemove(str_list: List[str]):
    count = 0
    for letter in range(0, len(str_list[0])):
        for word in range(1, len(str_list)):
            if str_list[word-1][letter] > str_list[word][letter]:
                count += 1
                break
    return count

print(numColumnsToRemove([
    ['c', 'b', 'a'],
    ['d', 'a', 'f'],
    ['g', 'h', 'i']
]))

print(numColumnsToRemove([['a', 'b', 'c', 'd', 'e', 'f']]))

print(numColumnsToRemove([
    ['z', 'y', 'x'],
    ['w', 'v', 'u'],
    ['t', 's', 'r']
]))