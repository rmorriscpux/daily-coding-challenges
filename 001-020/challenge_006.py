'''
An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node.
Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.
'''

# This doesn't work. I believe it's due to the way Python does garbage collection. This is better suited for C++.

import ctypes # Necessary to get the 

class Node:
    def __init__(self, val):
        self.val = val
        self.both = 0

class XORLL:
    def __init__(self):
        self.head = None
        self.tail = None

    # Add a new node to the end of the list.
    def add(self, val):
        new_node = Node(val)
        print("New Node ", id(new_node))

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.both = id(new_node) ^ self.tail.both
            new_node.both = id(self.tail)
            self.tail = new_node
        return

    # Get the value stored at a given index in the list.
    def get(self, index):
        # Sanity check for empty list.
        if self.head == None:
            return "Index not found."

        # Initialize
        prev = 0
        cur_node = self.head

        for i in range(0, index):
            next = prev ^ cur_node.both

            if next != 0:
                prev = id(cur_node)
                cur_node = ctypes.cast(next, ctypes.py_object).value
            else:
                return "Index not found."

        return cur_node.val

if __name__ == "__main__":
    test_ll = XORLL()
    test_ll.add(5)
    test_ll.add(4)
    test_ll.add(3)
    test_ll.add(2)
    test_ll.add(1)
    test_ll.add("Takeoff!")

    print(test_ll.get(1))
    print(test_ll.get(2))
    print(test_ll.get(3))
    print(test_ll.get(4))
    print(test_ll.get(5))
    print(test_ll.get(6))
    print(test_ll.get(7))