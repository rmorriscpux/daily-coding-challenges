'''
Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the following methods:

    next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
    has_next(): returns whether or not the iterator still has elements left.

For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.
'''

from typing import List

class TwoDimensionalIterator:
    def __init__(self, two_d_iterable: List[list]):
        self._iterable = two_d_iterable
        self._group, self._pos = 0, 0
        # Check for empty group lists at the start.
        self._checkEmptyGroup()

    # "Private" method to skip empty self._group lists.
    def _checkEmptyGroup(self):
        iterable_length = len(self._iterable) # Optimization

        while self._group < iterable_length and not self._iterable[self._group]:
            self._group += 1
        return

    def next(self):
        # When the iterable is completed, raise exception.
        if self._group >= len(self._iterable):
            raise StopIteration()

        next_element = self._iterable[self._group][self._pos]
        self._pos += 1
        if self._pos == len(self._iterable[self._group]):
            self._group += 1
            self._pos = 0
            self._checkEmptyGroup()

        return next_element

    def hasNext(self):
        return self._group < len(self._iterable)

if __name__ == "__main__":
    two_d_iter = TwoDimensionalIterator([[1, 2], [3], [], [4, 5, 6]])
    print(two_d_iter.hasNext())
    print(two_d_iter.next())
    print(two_d_iter.next())
    print(two_d_iter.next())
    print(two_d_iter.hasNext())
    print(two_d_iter.next())
    print(two_d_iter.next())
    print(two_d_iter.hasNext())
    print(two_d_iter.next())
    print(two_d_iter.hasNext())
    print(two_d_iter.next()) # Will raise StopIteration exception.
