'''
Given a linked list of numbers and a pivot k, partition the linked list so that all nodes less than k come before nodes greater than or equal to k.

For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3, the solution could be 1 -> 0 -> 5 -> 8 -> 3.
'''

class SLLNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"SLLNode({self.value})"

    def __str__(self):
        return str(self.value)

class SLL:
    def __init__(self, *values):
        self.head = None
        for v in values[::-1]:
            self.addToFront(v)
        
    def __repr__(self):
        sll_head = self.head.value if self.head else None
        return f"SLL(head: '{sll_head}')"

    def __str__(self):
        out_str = "SLL["
        node_ptr = self.head
        while node_ptr:
            out_str += str(node_ptr.value)
            if node_ptr.next:
                out_str += " -> "
            node_ptr = node_ptr.next
        out_str += "]"
        return out_str

    def addToFront(self, value: int):
        new_node = SLLNode(value)
        new_node.next = self.head
        self.head = new_node
        return self

    def partition(self, k: int):
        if not self.head:
            return self

        prev_node = self.head
        cur_node = self.head.next
        while cur_node:
            if cur_node.value < k:
                prev_node.next = cur_node.next
                cur_node.next = self.head
                self.head = cur_node
                cur_node = prev_node.next
            else:
                prev_node = cur_node
                cur_node = cur_node.next

        return self

s = SLL(5, 1, 8, 0, 3)
print(s)
s.partition(3)
print(s)