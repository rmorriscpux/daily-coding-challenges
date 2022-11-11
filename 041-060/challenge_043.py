'''
Implement a stack that has the following methods:

    push(val), which pushes an element onto the stack
    pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
    max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.
'''

# Class maintains a second list that contains indices where a value greater than the last max value was pushed.
class Stack:
    def __init__(self, *values):
        self.stack = []
        self.max_stack = []
        for v in values:
            self.push(v)

    # When a value is pushed, check if it's greater than the value at the position where the current max is.
    def push(self, value):
        self.stack.append(value)
        if len(self.max_stack) == 0 or value > self.stack[len(self.max_stack)-1]:
            self.max_stack.append(len(self.stack)-1)

    # When a value is popped, check if the index popped was the last value in max_stack. If so, remove that as well.
    def pop(self):
        if len(self.stack) == 0:
            return None

        if len(self.stack) - 1 == self.max_stack[-1]:
            self.max_stack.pop()

        return self.stack.pop()

    def max(self):
        return self.stack[len(self.max_stack)-1] if len(self.stack) > 0 else None

s = Stack()
s.push(1)
s.push(3)
s.push(2)
s.push(5)
s.max()