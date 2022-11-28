'''
Implement a stack API using only a heap. A stack implements the following methods:

    push(item), which adds an element to the stack
    pop(), which removes and returns the most recently added element (or throws an error if there is nothing on the stack)

Recall that a heap has the following operations:

    push(item), which adds a new key to the heap
    pop(), which removes and returns the max value of the heap
'''

# Python's heapq library prioritizes low-to-high order. So start from the system max value when pushing and work down.
# The idea is to associate a heap pushed item with its push order in the stack. Easily done via tuples.

from heapq import heappush, heappop
import sys

class Stack:
    def __init__(self, *values):
        self._counter = sys.maxsize
        self._stack = []
        for v in values:
            self.push(v)

    # For printed representation. White nerds in ΛΛΛ. (Seriously, this made sense in the 1980s)
    def __repr__(self):
        sorted_stack = sorted(self._stack, key=lambda item: item[0], reverse=True)
        out_list = list(map(lambda item: item[1], sorted_stack))
        return str(out_list)

    def push(self, value):
        heappush(self._stack, (self._counter, value))
        self._counter -= 1

    def pop(self):
        if not self._stack: # Empty Stack
            return None
        
        out_item = heappop(self._stack)
        self._counter += 1
        return out_item[1]

s = Stack(5, 1, 3, 2, 4)
print(s)
s.push(6)
print(s)
out = s.pop()
print(out)
print(s)