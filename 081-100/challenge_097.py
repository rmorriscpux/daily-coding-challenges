'''
Write a map implementation with a get function that lets you retrieve the value of a key at a particular time.

It should contain the following methods:

    set(key, value, time): # sets key to value for t = time.
    get(key, time): # gets the key at t = time.

The map should work like this. If we set a key at a particular time, it will maintain that value forever or until it gets set at a later time.
In other words, when we get a key at a time, it should return the value that was set for that key set at the most recent time.

Consider the following examples:

d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 2) # set key 1 to value 2 at time 2
d.get(1, 1) # get key 1 at time 1 should be 1
d.get(1, 3) # get key 1 at time 3 should be 2

d.set(1, 1, 5) # set key 1 to value 1 at time 5
d.get(1, 0) # get key 1 at time 0 should be null
d.get(1, 10) # get key 1 at time 10 should be 1

d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 0) # set key 1 to value 2 at time 0
d.get(1, 0) # get key 1 at time 0 should be 2
'''

class TimeMap:
    def __init__(self):
        self._map = {}

    class SLLNode:
        def __init__(self, value, timestamp):
            self.value = value
            self.timestamp = timestamp
            self.next = None

    class SLL:
        def __init__(self):
            self.head = None

        def add(self, value, timestamp):
            new_node = TimeMap.SLLNode(value, timestamp)

            if not self.head:
                self.head = new_node
                return

            if new_node.timestamp < self.head.timestamp:
                new_node.next = self.head
                self.head = new_node
                return

            node_ptr = self.head
            while node_ptr:
                if new_node.timestamp == node_ptr.timestamp:
                    node_ptr.value = new_node.value
                    return

                if ((new_node.timestamp > node_ptr.timestamp) and
                    (not node_ptr.next or node_ptr.next.timestamp > new_node.timestamp)):
                    new_node.next = node_ptr.next
                    node_ptr.next = new_node
                    return

                node_ptr = node_ptr.next

    def set(self, key: int, value: int, time: int):
        if key not in self._map:
            self._map[key] = TimeMap.SLL()

        self._map[key].add(value, time)

        return

    def get(self, key: int, time: int):
        if key not in self._map:
            return None

        node_ptr = self._map[key].head

        if time < node_ptr.timestamp:
            return None

        while node_ptr.next:
            if time < node_ptr.next.timestamp:
                return node_ptr.value
            node_ptr = node_ptr.next
        return node_ptr.value

d = TimeMap()
d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 2) # set key 1 to value 2 at time 2
print(d.get(1, 1)) # get key 1 at time 1 should be 1
print(d.get(1, 3)) # get key 1 at time 3 should be 2
del d
d = TimeMap()
d.set(1, 1, 5) # set key 1 to value 1 at time 5
print(d.get(1, 0)) # get key 1 at time 0 should be null
print(d.get(1, 10)) # get key 1 at time 10 should be 1
del d
d = TimeMap()
d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 0) # set key 1 to value 2 at time 0
print(d.get(1, 0)) # get key 1 at time 0 should be 2