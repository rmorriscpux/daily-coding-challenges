'''
Given the head to a singly linked list, where each node also has a “random” pointer that points to anywhere in the linked list, deep clone the list.
'''

from random import randint

class SLLNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.rand_next = None

class SLL:
    def __init__(self, *values):
        self.head = None
        self._length = 0
        self._rand_next_digest = []
        if values:
            self.head = SLLNode(values[0])
            self._length += 1
            node_ptr = self.head
            for v in values[1:]:
                node_ptr.next = SLLNode(v)
                self._length += 1
                node_ptr = node_ptr.next
            self.randomizePtrs()

    def __str__(self):
        value_list = []
        next_list = []
        rand_next_list = []
        node_ptr = self.head
        while node_ptr:
            value_list.append(node_ptr.value)
            if node_ptr.next:
                next_list.append(node_ptr.next.value)
            rand_next_list.append(node_ptr.rand_next.value)
            node_ptr = node_ptr.next
        return repr(value_list) + '\n' + repr(next_list) + '\n' + repr(rand_next_list)
    
    def addRear(self, value):
        if not self.head:
            self.head = SLLNode(value)
            self._length += 1
            return self

        node_ptr = self.head
        while node_ptr.next:
            node_ptr = node_ptr.next
        node_ptr.next = SLLNode(value)
        self._length += 1
        return self

    def randomizePtrs(self):
        if not self.head:
            return

        self._rand_next_digest = []
        node_ptr = self.head
        while node_ptr:
            rand_ptr = self.head
            jumps = randint(0, self._length-1)
            for i in range(0, jumps):
                rand_ptr = rand_ptr.next
            node_ptr.rand_next = rand_ptr
            self._rand_next_digest.append(jumps)
            node_ptr = node_ptr.next

        return

    def deepClone(self):
        new_sll = SLL()
        node_ptr = self.head
        while node_ptr:
            new_sll.addRear(node_ptr.value)
            node_ptr = node_ptr.next

        new_node_ptr = new_sll.head
        for i in range(0, self._length):
            rand_ptr = self.head
            for j in range(0, self._rand_next_digest[i]):
                rand_ptr = rand_ptr.next
            new_node_ptr.rand_next = rand_ptr
            new_sll._rand_next_digest.append(self._rand_next_digest[i])
            new_node_ptr = new_node_ptr.next

        return new_sll

sll1 = SLL(1, 2, 3, 4, 5, 6)
print(sll1)
sll2 = sll1.deepClone()
print(sll2)