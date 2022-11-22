'''
You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:

    init(arr, size): initialize with the original large array and size.
    set(i, val): updates index at i with val.
    get(i): gets the value at index i.

'''

# Including support for negative i values. e.g. -1 will be the last element, -2 will be the second-to-last element, etc.

class SparseArray:
    # Size can be flexible on init. If left to default, size will be len(arr).
    def __init__(self, arr: list, size: int=-1):
        self.size = size if size >= 0 else len(arr)
        self.array = {}
        # All non-zero values will be included in the dictionary under the index it is in the array.
        for i in range(0, self.size):
            if i == len(arr):
                break
            if arr[i] != 0:
                self.array[i] = arr[i]

    def set(self, i: int, val):
        index = self._indexCheck(i)
        # Remove key index if it exists and val is 0. Otherwise set key index to non-zero value.
        if index in self.array and val == 0:
            self.array.pop(index)
        elif val != 0:
            self.array[index] = val
        return

    def get(self, i):
        index = self._indexCheck(i)
        return 0 if index not in self.array else self.array[index]

    # Check for input index in range, return positive i or flipped negative i.
    def _indexCheck(self, i):
        if i < -self.size or i >= self.size:
            raise IndexError("Sequence index out of range.")
        return self.size + i if i < 0 else i


sa = SparseArray([0, 4, 0, 0, 8, 0, 0, 0])

print("sa.array:", sa.array)
print(sa.get(1))
print(sa.get(2))
print("Setting index 3 to 5")
sa.set(3, 5)
print("sa.array:", sa.array)
print(sa.get(-5))
sa.set(1, 0)
print("sa.array:", sa.array)