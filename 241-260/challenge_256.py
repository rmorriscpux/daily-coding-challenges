'''
Given a linked list, rearrange the node values such that they appear in alternating low -> high -> low -> high ... form.
For example, given 1 -> 2 -> 3 -> 4 -> 5, you should return 1 -> 3 -> 2 -> 5 -> 4.
'''

class SLLNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class SLL:
    def __init__(self, *values: int):
        self.head = None
        for v in values[::-1]:
            self.addFront(v)

    def __str__(self):
        node_ptr = self.head
        out_str = "SLL("
        while node_ptr:
            out_str += str(node_ptr.value)
            if node_ptr.next:
                out_str += " -> "
            node_ptr = node_ptr.next
        out_str += ")"
        return out_str
    
    def __repr__(self):
        return str(self)

    def addFront(self, value: int):
        new_node = SLLNode(value)
        new_node.next = self.head
        self.head = new_node
        return self

    def removeValue(self, target_value: int):
        if not self.head:
            raise ValueError("List is empty.")

        if self.head.value == target_value:
            self.head = self.head.next
            return target_value
        
        node_ptr = self.head
        while node_ptr.next:
            if node_ptr.next.value == target_value:
                node_ptr.next = node_ptr.next.next
                return target_value
            node_ptr = node_ptr.next

        raise ValueError("Target Value Not Found.")
    
        return
    
    def arrangeLowHigh(self):
        if not (self.head and self.head.next):
            return self
        
        val_arr = []
        while self.head:
            val_arr.append(self.head.value)
            self.head = self.head.next

        val_arr.sort()

        self.head = SLLNode(val_arr.pop(0))
        next_val = -1
        node_ptr = self.head
        while val_arr:
            node_ptr.next = SLLNode(val_arr.pop(next_val))
            next_val = ~next_val
            node_ptr = node_ptr.next

        return self
    
    # Slightly more complex; replicates example.
    def arrangeLowHigh2(self):
        if not (self.head and self.head.next):
            return self
        
        val_arr = []
        while self.head:
            val_arr.append(self.head.value)
            self.head = self.head.next

        val_arr.sort()

        self.head = SLLNode(val_arr.pop(0))
        next_val = True
        node_ptr = self.head
        while len(val_arr) > 1:
            node_ptr.next = SLLNode(val_arr.pop(int(next_val)))
            next_val = not next_val
            node_ptr = node_ptr.next
        node_ptr.next = SLLNode(val_arr.pop(0))

        return self    
s = SLL(1, 2, 3, 4, 5, 6, 7)
print(s)
s.arrangeLowHigh()
print(s)
s.arrangeLowHigh2()
print(s)