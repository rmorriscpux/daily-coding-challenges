'''
Implement a stack that has the following methods:

    push(val), which pushes an element onto the stack
    pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
    max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.
'''

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, data=None):
        self.top = StackNode(data) if data else None
        self._max = data

    def push(self, data):
        new_top = StackNode(data)
        new_top.next = self.top
        self.top = new_top
        if self._max == None or data > self._max:
            self._max = data
        return self

    def pop(self):
        # Return None if stack is empty.
        if not self.top:
            return None

        pop_data = self.top.data
        self.top = self.top.next
        # Recalculate self._max if the max value was popped.
        if pop_data == self._max:
            if self.top == None:
                self._max = None
            else:
                self._max = self.top.data
                stack_ptr = self.top.next
                while stack_ptr != None:
                    if stack_ptr.data > self._max:
                        self._max = stack_ptr.data
                    stack_ptr = stack_ptr.next
        return pop_data

    @property
    def max(self):
        return self._max

my_stack = Stack()
print("Max in stack:", my_stack.max)
my_stack.push(3).push(1).push(5).push(2)
print("Max in stack:", my_stack.max)
print("Popped", my_stack.pop())
print("Popped", my_stack.pop())
print("Max in stack:", my_stack.max)
