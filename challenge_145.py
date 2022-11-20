'''
Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
'''

class SLLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"SLLNode({self.value})"

    def printSLL(self):
        node_ptr = self
        out_str = ""
        while node_ptr:
            out_str += str(node_ptr)
            if node_ptr.next:
                out_str += "->"
            node_ptr = node_ptr.next
        print(out_str)
        return

def swapEveryTwoNodes(head: SLLNode):
    # Case: Empty list.
    if not head:
        return

    # Case: Single node in list.
    if not head.next:
        return head

    next1 = head.next
    next2 = next1.next

    # Case: Last two nodes in the list. Make the first next node's next the head, then make head the end.
    if not next2:
        next1.next = head
        head.next = None
    # Case: Single node in list after the current two: Make the first next node's next the head, then name head's next the second next node.
    elif not next2.next:
        next1.next = head
        head.next = next2
    # Case: More than one node in list after the current two: Make the first next node's next the head, name head's next the third next node, then recur into the second next node.
    else:
        next1.next = head
        head.next = next2.next
        swapEveryTwoNodes(next2)

    # next1 is the new head.
    return next1

# Start with linked list from 1 to 8.
head1 = SLLNode(1)
h1_ptr = head1
for i in range(2, 9):
    h1_ptr.next = SLLNode(i)
    h1_ptr = h1_ptr.next
head1.printSLL()
head1_swapped = swapEveryTwoNodes(head1)
head1_swapped.printSLL()

print("========")

# Start with linked list from 1 to 9.
head2 = SLLNode(1)
h2_ptr = head2
for i in range(2, 10):
    h2_ptr.next = SLLNode(i)
    h2_ptr = h2_ptr.next
head2.printSLL()
head2_swapped = swapEveryTwoNodes(head2)
head2_swapped.printSLL()