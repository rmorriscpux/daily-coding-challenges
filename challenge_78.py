'''
Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.
'''

class SLLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def __len__(self):
        return self._length

    def __repr__(self):
        out_str = "["
        node_ptr = self.head
        while node_ptr:
            out_str += str(node_ptr.value)
            if node_ptr.next:
                out_str += ", "
            node_ptr = node_ptr.next
        out_str += "]"
        return out_str

    def addFront(self, value):
        new_node = SLLNode(value)
        new_node.next = self.head
        self.head = new_node
        if self._length == 0:
            self.tail = new_node
        self._length += 1
        return self

    def addBack(self, value):
        if self._length == 0:
            self.addFront(value)
        else:
            new_node = SLLNode(value)
            self.tail.next = new_node
            self.tail = new_node
            self._length += 1
        return self

    def remove(self):
        if self.head:
            pop_node = self.head
            self.head = self.head.next
            self._length -= 1
            if self._length == 0:
                self.tail = None
            return pop_node
        return None

def mergeSortedLists(*linked_lists: SLL):
    merged_list = SLL()
    if len(linked_lists) == 0:
        return merged_list

    while True:
        cur_min_index = None
        for i, cur_list in enumerate(linked_lists):
            # Ignore empty linked lists.
            if len(cur_list) == 0:
                continue

            if cur_min_index == None:
                cur_min_index = i
            elif cur_list.head.value < linked_lists[cur_min_index].head.value:
                cur_min_index = i

        # Exhausted all input linked lists when cur_min_index == None at the end of the for loop.
        if cur_min_index == None:
            break

        # Remove the minimum value among all input linked lists and add it to the back of the merged list.
        pop_node = linked_lists[cur_min_index].remove()
        merged_list.addBack(pop_node.value)

    return merged_list

list1 = SLL()
list1.addBack(1).addBack(5).addBack(9)
list2 = SLL()
list2.addBack(2).addBack(6).addBack(7)
list3 = SLL()
list3.addBack(3).addBack(4).addBack(8)

print(list1, list2, list3)

merged_list = mergeSortedLists(list1, list2, list3)

print(merged_list)