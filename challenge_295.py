'''
Pascal's triangle is a triangular array of integers constructed with the following formula:

The first row consists of the number 1. For each subsequent row, each element is the sum of the numbers directly above it, on either side.
For example, here are the first few rows:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

Given an input k, return the kth row of Pascal's triangle.

Bonus: Can you do this only using O(k) space?
'''

# Method using only O(k) space. Returns empty list when k < 1.
def getPascalsTriangleRow(k: int) -> list[int]:
    pascal_row = []
    for i in range(k):
        # On each position past the leftmost, the next row's value is equal to the sum of that position and the position before it.
        for j in range(i-1, 0, -1):
            pascal_row[j] += pascal_row[j-1]
        # Place a 1 at the end of the row on each iteration.
        pascal_row.append(1)
    return pascal_row

if __name__ == "__main__":
    for k in range(1, 11):
        print(getPascalsTriangleRow(k))