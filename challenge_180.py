'''
Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other queue. This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

Hint: Try working backwards from the end state.
'''

# Custom Stack and Queue classes where only minimal manipulation is possible.

class Stack:
    def __init__(self, *values):
        self._stack = list(values)

    def __len__(self):
        return len(self._stack)

    def __str__(self):
        return repr(self._stack)

    def push(self, value):
        self._stack.append(value)
        return self

    def pop(self):
        if not self._stack:
            return None
        return self._stack.pop()

class Queue:
    def __init__(self, *values):
        self._queue = list(values)

    def __len__(self):
        return len(self._queue)

    def __str__(self):
        return repr(self._queue)

    def enqueue(self, value):
        self._queue.append(value)
        return self

    def dequeue(self):
        if not self._queue:
            return None
        return self._queue.pop(0)

def interleaveStack(stack: Stack):
    def rInterleaveStack(stack, queue, moves):
        # Function removes the number of items from the stack, placing them in the queue, then dequeues all the queue's items and places them back on the stack.
        # This effectively reverses those items. This then continues with the number of moves reduced by 1, until moves = 1.
        if moves <= 1:
            return

        for i in range(0, moves):
            queue.enqueue(stack.pop())

        while len(queue) > 0:
            stack.push(queue.dequeue())

        rInterleaveStack(stack, queue, moves-1)

    queue = Queue()
    rInterleaveStack(stack, queue, len(stack)-1)

stack = Stack(1, 2, 3, 4, 5)
print(stack)
interleaveStack(stack)
print(stack)