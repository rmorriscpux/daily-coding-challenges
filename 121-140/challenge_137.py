'''
Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

    init(size): initialize the array with size
    set(i, val): updates index at i with val where val is either 1 or 0.
    get(i): gets the value at index i.
'''

class BitArray:
    def __init__(self, size: int):
        self.assert_set = set()
        self.size = size

    def set(self, i: int, val: int):
        if i < -self.size or i >= self.size:
            raise IndexError("Sequence index out of range.")
        if not(val == 0 or val == 1):
            raise ValueError("val must be 1 or 0.")

        index = i if i >= 0 else self.size + i

        if val:
            self.assert_set.add(index)
        elif index in self.assert_set:
            self.assert_set.remove(index)

        return

    def get(self, i: int):
        if i < -self.size or i >= self.size:
            raise IndexError("Sequence index out of range.")

        index = i if i >= 0 else self.size + i

        return int(index in self.assert_set)

ba =  BitArray(10)

ba.set(3, 1)
ba.set(5, 1)
ba.set(-1, 1)
print(ba.get(0))
print(ba.get(3))
print(ba.get(9))
ba.set(3, 0)
print(ba.get(3))