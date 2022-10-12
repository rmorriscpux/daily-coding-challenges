'''
Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
'''

class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self._length = 0
        self.head = None

    def __len__(self):
        return self._length

    def addFront(self, data):
        new_node = SLLNode(data)
        new_node.next = self.head
        self.head = new_node
        self._length += 1
        return self

    def addBack(self, data):
        if self.head == None:
            self.addFront(data) # self._length is updated in this method.
        else:
            list_ptr = self.head
            while list_ptr.next != None:
                list_ptr = list_ptr.next
            list_ptr.next = SLLNode(data)
            self._length += 1
        return self

    def removeKthLastElement(self, k):
        # Sanity Check
        if self.head == None:
            return None
        if k <= 0 or k > len(self):
            return None
        
        popped_data = None
        if k == len(self):
            # Remove the head, make the next element the head.
            popped_data = self.head.data
            self.head = self.head.next
        else:
            # Calculate steps up to before the kth last element, then go there.
            steps = len(self) - k - 1
            list_ptr = self.head
            for i in range(0, steps):
                list_ptr = list_ptr.next
            # Set the return value to the data we're removing.
            popped_data = list_ptr.next.data
            list_ptr.next = list_ptr.next.next

        self._length -= 1
        return popped_data

    def printAsList(self):
        out_list = []
        list_ptr = self.head
        while list_ptr != None:
            out_list.append(list_ptr.data)
            list_ptr = list_ptr.next
        print(out_list)
        return self

# Singly linked list of integers in descending order. 10->9->8->7->6->5->4->3->2->1
my_list = SLL()
my_list.addFront(1).addFront(2).addFront(3).addFront(4).addFront(5).addFront(6).addFront(7).addFront(8).addFront(9).addFront(10)
my_list.printAsList()
print("Removed " + str(my_list.removeKthLastElement(5)))
my_list.printAsList()
print("Removed " + str(my_list.removeKthLastElement(9)))
my_list.printAsList()