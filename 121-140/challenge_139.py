'''
Given an iterator with methods next() and hasNext(), create a wrapper iterator, PeekableInterface,
which also implements peek(). peek shows the next element that would be returned on next().

Here is the interface:

class PeekableInterface(object):
    def __init__(self, iterator):
        pass

    def peek(self):
        pass

    def next(self):
        pass

    def hasNext(self):
        pass
'''

from collections.abc import Iterator

# This is effectively creating an iterator that keeps the next value in a buffer.

class PeekableInterface:
    def __init__(self, iterator: Iterator):
        # Must instantiate the class with an Iterator object, created via iter(), for the class methods to work.
        if not isinstance(iterator, Iterator):
            raise TypeError("Must initialize PeekableInterface class with an Iterator object.")

        self._iterator = iterator
        self._next = next(self._iterator)
        self._has_next = True

    # peek() - Simply return the next element without iterating.
    def peek(self):
        return self._next

    def next(self):
        # Check if we've already completed the iteration.
        if not self._has_next:
            raise StopIteration

        # Set the return value, then check if we have a next value after that. If not, set up self._has_next
        out_val = self._next

        try:
            self._next = next(self._iterator)
        except StopIteration:
            self._has_next = False
            self._next = None

        return out_val

    def hasNext(self):
        return self._has_next

x = PeekableInterface(iter([1, 2, 3, 4, 5]))

print(x.peek())
print(x.peek())
print("Iterate to", x.next())
print("Iterate to", x.next())
print("Has Next:", x.hasNext())
print(x.peek())
print("Iterate to", x.next())
print("Iterate to", x.next())
print(x.peek())
print("Iterate to", x.next())
print("Has Next:", x.hasNext())
print(x.peek())
try:
    print("Iterate to", x.next())
except StopIteration:
    print("PeekableInterface.next() - StopIteration occurred.")
print("Has Next:", x.hasNext())
print(x.peek())