'''
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
'''

# After the point where two single-linked lists intersect, all values will be the same. 
# The trick here is to write something that gets to the end of each list and then backtracks.

# Create node and single-linked list classes.
class SLLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def __len__(self):
        count = 0
        node_ptr = self.head
        while node_ptr != None:
            count += 1
            node_ptr = node_ptr.next
        return count

    def add_to_front(self, value):
        if self.head:
            new_node = SLLNode(value)
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = SLLNode(value)
        return self

    def add_to_back(self, value):
        if self.head:
            list_ptr = self.head
            while list_ptr.next != None:
                list_ptr = list_ptr.next
            list_ptr.next = SLLNode(value)
        else:
            self.head = SLLNode(value)
        return self

    def traverse(self):
        list_ptr = self.head
        while list_ptr != None:
            print(list_ptr.value)
            list_ptr = list_ptr.next

# Takes in two SLLs, M and N.
def list_intersection(M, N):
    m_ptr = M.head
    n_ptr = N.head
    # The way single linked lists work, if two lists point to the same memory block, we know that the tails are identical between the two lists.
    # Therefore the length between the tail and the intersection is equal between both, regardless of how long each list is.
    # So we just need to get pointers to an equidistant length from the tail.
    len_diff = len(M) - len(N)

    if len_diff > 0: # M is longer than N
        for i in range(0, len_diff):
            m_ptr = m_ptr.next
    else: # N is longer than M, or both are the same length.
        for i in range(len_diff, 0): # Because len_diff is negative.
            n_ptr = n_ptr.next

    # Now find the intersection if it exists.
    while m_ptr != None:
        if m_ptr.value == n_ptr.value:
            return m_ptr.value
        m_ptr = m_ptr.next
        n_ptr = n_ptr.next
    
    # No intersection, return None
    return None

M = SLL()
M.add_to_front(10).add_to_front(8).add_to_front(9).add_to_front(3)

N = SLL()
N.add_to_front(10).add_to_front(8).add_to_front(9).add_to_front(18).add_to_front(4).add_to_front(5)

print(list_intersection(M, N))