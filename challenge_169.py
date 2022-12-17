'''
Given a linked list, sort it in O(n log n) time and constant space.

For example, the linked list 4 -> 1 -> -3 -> 99 should become -3 -> 1 -> 4 -> 99.
'''

class SLLNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class SLL:
    def __init__(self, *values: int):
        self.head = None
        for val in values[::-1]:
            self.addToFront(val)
        return

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
        return

    def sortNodes(self):
        def rSortNodes(node, count):
            if count == 1:
                return node

            # Split the list and sort recursively.
            middle = count // 2
            right_start = node
            left_end = None
            for i in range(0, middle):
                left_end = right_start
                right_start = right_start.next

            left_end.next = None
            
            sorted_left = rSortNodes(node, middle)
            sorted_right = rSortNodes(right_start, count - middle)

            # Dummy node to start. Trim at the end.
            head = SLLNode(float("-inf"))
            node_ptr = head
            
            # Merge the recursively sorted lists by joining them in numerical order.
            while sorted_left and sorted_right:
                if sorted_left.value < sorted_right.value:
                    temp = sorted_left
                    sorted_left = sorted_left.next
                else:
                    temp = sorted_right
                    sorted_right = sorted_right.next
                temp.next = None
                node_ptr.next = temp
                node_ptr = node_ptr.next

            if sorted_left:
                node_ptr.next = sorted_left
            if sorted_right:
                node_ptr.next = sorted_right

            return head.next

        if not self.head:
            return

        # Get the length of the SLL.
        count = 0
        node_ptr = self.head
        while node_ptr:
            count += 1
            node_ptr = node_ptr.next

        # Start with the length and the head of the SLL.
        self.head = rSortNodes(self.head, count)

        return

s = SLL(4, 1, -3, 99)
print(s)
s.sortNodes()
print(s)