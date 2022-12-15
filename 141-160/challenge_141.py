'''
Implement 3 stacks using a single list:

class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        pass

    def push(self, item, stack_number):
        pass
'''

class TripleStack:
    def __init__(self):
        self.triple_stack = []
        self._stack_starts = [0, 0, 0]

    def __repr__(self):
        return str([
            self.triple_stack[self._stack_starts[0]:self._stack_starts[1]],
            self.triple_stack[self._stack_starts[1]:self._stack_starts[2]],
            self.triple_stack[self._stack_starts[2]:]
        ])

    def __str__(self):
        return repr(self)

    def pop(self, stack_number: int):
        if stack_number < 0 or stack_number > 2:
            raise ValueError("Stack number must be between 0 and 2.")

        if stack_number == 2 and self._stack_starts[2] == len(self.triple_stack)-1:
            return None
        elif stack_number < 2 and self._stack_starts[stack_number] == self._stack_starts[stack_number+1]:
            return None

        out_val = self.triple_stack.pop(self._stack_starts[stack_number])
        for i in range(stack_number+1, 3):
            self._stack_starts[i] -= 1

        return out_val
    
    def push(self, item, stack_number: int):
        if stack_number < 0 or stack_number > 2:
            raise ValueError("Stack number must be between 0 and 2.")

        self.triple_stack.insert(self._stack_starts[stack_number], item)
        for i in range(stack_number+1, 3):
            self._stack_starts[i] += 1

        return

ts = TripleStack()
ts.push(1, 0)
ts.push(10, 1)
ts.push(100, 2)
ts.push(2, 0)
ts.push(20, 1)
ts.push(200, 2)
ts.push(3, 0)
ts.push(30, 1)
ts.push(300, 2)

print(ts)
ts.pop(1)
print(ts)
ts.pop(2)
print(ts)
ts.pop(0)
print(ts)