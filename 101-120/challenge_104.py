'''
Determine whether a doubly linked list is a palindrome. What if it's singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns true while 1 -> 4 returns false.
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

    def addFront(self, value):
        new_node = SLLNode(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self._length += 1

        return self

    def isPalindrome(self):
        if self._length == 0:
            return False

        # Put together the first half of the list.
        value_list = []
        node_ptr = self.head
        for i in range(0, self._length // 2):
            value_list.append(node_ptr.value)
            node_ptr = node_ptr.next

        # Go through the center node if the list length is odd.
        if self._length % 2 == 1:
            node_ptr = node_ptr.next

        # Now compare.
        while len(value_list) > 0:
            if node_ptr.value != value_list[len(value_list)-1]:
                return False
            node_ptr = node_ptr.next
            value_list.pop()

        return True

class DLLNode(SLLNode):
    def __init__(self, value):
        super().__init__(value)
        self.prev = None

class DLL(SLL):
    def __init__(self):
        super().__init__()
        self.tail = None

    def addFront(self, value):
        new_node = DLLNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._length += 1

        return self

    def addBack(self, value):
        new_node = DLLNode(value)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._length += 1

        return self

    def isPalindrome(self):
        if self._length == 0:
            return False

        # Make 2 pointers starting at the head and tail, then head toward the center comparing along the way.
        front_ptr = self.head
        rear_ptr = self.tail

        for i in range(0, self._length // 2):
            if front_ptr.value != rear_ptr.value:
                return False
            front_ptr = front_ptr.next
            rear_ptr = rear_ptr.prev

        return True

sll1 = SLL()
sll1.addFront(1).addFront(4).addFront(3).addFront(4).addFront(1)

sll2 = SLL()
sll2.addFront(1).addFront(4)

print(sll1.isPalindrome())
print(sll2.isPalindrome())

dll1 = DLL()
dll1.addFront(1).addFront(4).addFront(3).addFront(4).addFront(1)

dll2 = DLL()
dll2.addFront(1).addFront(4)

print(dll1.isPalindrome())
print(dll2.isPalindrome())