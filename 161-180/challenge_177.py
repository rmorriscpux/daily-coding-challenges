'''
Given a linked list and a positive integer k, rotate the list to the right by k places.

For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.

Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2.
'''

class SLLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLL:
    def __init__(self, *values):
        self.head = None
        self._length = 0
        for v in values[::-1]:
            self.addToFront(v)

    def __str__(self):
        node_ptr = self.head
        out_str = ""
        while node_ptr:
            out_str += str(node_ptr.value)
            if node_ptr.next:
                out_str += "->"
            node_ptr = node_ptr.next

        return out_str

    def addToFront(self, value):
        new_node = SLLNode(value)
        new_node.next = self.head
        self.head = new_node
        self._length += 1
        return self

    def rotateRight(self, k: int):
        assert(k >= 0)
        if self._length == 0:
            return
        k %= self._length

        if k == 0:
            return

        new_head = None
        new_tail = None

        node_ptr = self.head
        for i in range(0, self._length-1):
            if i == self._length - k - 1:
                new_tail = node_ptr
            elif i == self._length - k:
                new_head = node_ptr
            node_ptr = node_ptr.next

        node_ptr.next = self.head
        new_tail.next = None
        self.head = new_head

        return self

s = SLL(1, 2, 3, 4, 5)
print(s)
s.rotateRight(3)
print(s)