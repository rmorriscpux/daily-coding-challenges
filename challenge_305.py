'''
Given a linked list, remove all consecutive nodes that sum to zero. Print out the remaining nodes.

For example, suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6 -> 6.
In this case, you should first remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5.
'''

class SLLNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return f"SLLNode({self.value})"
    
class SLL:
    def __init__(self, *values):
        # Declare self.head and add values if passed.
        self.head = None
        self.add(*values)

    def __len__(self):
        length = 0
        node_ptr = self.head
        while node_ptr:
            node_ptr = node_ptr.next
            length += 1
        return length
    
    def __str__(self):
        out_str = "SLL("
        node_ptr = self.head
        while node_ptr:
            out_str += str(node_ptr)
            if node_ptr.next:
                out_str += " -> "
            node_ptr = node_ptr.next
        out_str += ")"
        return out_str

    def add(self, *values):
        if not values:
            # values tuple is empty.
            return self
        start = 0
        if not self.head:
            # When SLL is empty, set self.head to the first value, then increment start.
            self.head = SLLNode(values[0])
            start = 1
        # Traverse to the end of the SLL.
        tail = self.head
        while tail.next:
            tail = tail.next
        # Add new values.
        for val in values[start:]:
            tail.next = SLLNode(val)
            tail = tail.next
        return self
    
    # Sum values in nodes inclusive of start, exclusive from end. [start -> ... -> end)
    def sumNodes(self, start: SLLNode, end: SLLNode=None) -> int:
        node_sum = 0
        node_ptr = start
        while node_ptr != end and node_ptr != None:
            node_sum += node_ptr.value
            node_ptr = node_ptr.next
        return node_sum
    
    def removeZeroSums(self):
        # At the head.
        start = self.head
        end = start
        while end:
            end = end.next
            node_sum = self.sumNodes(start, end)
            if node_sum == 0:
                start = end
                self.head = end
        # Past the head.
        while start and start.next:
            end = start.next
            while end:
                end = end.next
                node_sum = self.sumNodes(start.next, end)
                if node_sum == 0:
                    start.next = end
            start = start.next
        return self
    
    def efftRemoveZeroSums(self):
        # At the head
        end = self.head
        total_sum = 0
        while end:
            total_sum += end.value
            end = end.next
            if total_sum == 0:
                self.head = end
        # Past the head
        prev = self.head
        while prev and prev.next:
            total_sum = 0
            end = prev.next
            while end:
                total_sum += end.value
                end = end.next
                if total_sum == 0:
                    prev.next = end
            prev = prev.next
    
if __name__ == "__main__":
    sll = SLL(3, 4, -7, 5, 6, -6)
    print(sll)
    sll.removeZeroSums()
    print(sll)
    print("----------")
    sll2 = SLL(0, 3, 4, -7, 5, 6, -6, 0)
    print(sll2)
    sll2.efftRemoveZeroSums()
    print(sll2)