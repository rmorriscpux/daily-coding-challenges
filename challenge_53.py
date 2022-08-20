'''
Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods:
enqueue, which inserts an element into the queue, and dequeue, which removes it.
'''

class Stack:
    class StackNode:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = self.StackNode(data)
        new_node.next = self.top
        self.top = new_node
        return self

    def pop(self):
        if self.top == None:
            return None
        
        pop_node = self.top
        self.top = self.top.next
        return pop_node.data

class Queue:
    # hold_stack is the stack that contains the queue. flip_stack is empty except when dequeue is called.
    def __init__(self):
        self.hold_stack = Stack()
        self.flip_stack = Stack()
        self._size = 0

    def __len__(self):
        return self._size

    def enqueue(self, data):
        self.hold_stack.push(data)
        self._size += 1
        return self

    def dequeue(self):
        if self._size <= 0:
            return None
        # Move everything to the flip_stack, remove the bottom from hold_stack, and flip back.
        for i in range(0, self._size-1):
            self.flip_stack.push(self.hold_stack.pop())
        dequeue_data = self.hold_stack.pop()
        for i in range(0, self._size-1):
            self.hold_stack.push(self.flip_stack.pop())
        self._size -= 1
        return dequeue_data

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1).enqueue(2).enqueue(3).enqueue(4)
    print(len(q))
    print(q.dequeue())
    print(len(q))