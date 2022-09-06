'''
Given the head of a singly linked list, reverse it in-place.
'''

class SLLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self._length = 0

    def __len__(self):
        return self._length

    def __repr__(self):
        out_str = "["
        node_ptr = self.head
        for i in range(0, self._length):
            out_str += str(node_ptr.value)
            if i < self._length - 1:
                out_str += "->"
            node_ptr = node_ptr.next
        out_str += "]"
        return out_str

    def addFront(self, value):
        new_node = SLLNode(value)

        if self.head:
            new_node.next = self.head
        self.head = new_node
        self._length += 1
        return self

    def addBack(self, value):
        new_node = SLLNode(value)
        self._length += 1

        if not self.head:
            self.head = new_node
            return self

        node_ptr = self.head
        while node_ptr.next:
            node_ptr = node_ptr.next
        node_ptr.next = new_node
        return self

    # Reverse Linked List In Place Function
    def reverse(self):
        if not self.head:
            return self
        if not self.head.next:
            return self

        left = self.head
        center = self.head.next
        left.next = None
        while center:
            right = center.next
            center.next = left
            left = center
            center = right
        self.head = left
        return self

sll = SLL()
sll.addFront(5).addFront(4).addFront(3).addFront(2).addFront(1)
print(sll)
sll.reverse()
print(sll)