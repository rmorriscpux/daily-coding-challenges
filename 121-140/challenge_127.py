'''
Let's represent an integer in a linked list format by having each node represent a digit in the number. The nodes make up the number in reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5

is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

9 -> 9

5 -> 2

return 124 (99 + 25) as:

4 -> 2 -> 1
'''

class SLLNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def __str__(self):
        out_str = ""
        if not self.head:
            out_str += ""
            return out_str

        node_ptr = self.head
        while node_ptr:
            out_str += str(node_ptr.value)
            node_ptr = node_ptr.next
            if node_ptr:
                out_str += "->"

        return out_str

    def add(self, value):
        if not self.head:
            self.head = SLLNode(value)
            return self

        node_ptr = self.head
        while node_ptr.next:
            node_ptr = node_ptr.next
        node_ptr.next = SLLNode(value)
        return self

    def buildIntList(self, num: int):
        self.head = None

        while num > 0:
            self.add(num % 10)
            num //= 10

def addNumLists(sll1: SLL, sll2: SLL):
    sum_sll = SLL()

    sll1_ptr = sll1.head
    sll2_ptr = sll2.head

    cur_sum = 0

    while sll1_ptr or sll2_ptr:
        # Carry from the previous sum.
        cur_sum //= 10
        
        # Add digits in sll1_ptr and sll2_ptr
        if sll1_ptr:
            cur_sum += sll1_ptr.value
            sll1_ptr = sll1_ptr.next
        
        if sll2_ptr:
            cur_sum += sll2_ptr.value
            sll2_ptr = sll2_ptr.next

        # Sum digit is the cur_sum % 10.
        sum_sll.add(cur_sum % 10)

    # Add final digit if we have a carry.
    cur_sum //= 10
    if cur_sum:
        sum_sll.add(cur_sum)

    return sum_sll

sll1 = SLL()
sll2 = SLL()
sll1.buildIntList(99)
sll2.buildIntList(25)
print(sll1)
print(sll2)
print(addNumLists(sll1, sll2))