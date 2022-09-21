'''
Implement an LFU (Least Frequently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

    set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item,
    then it should also remove the least frequently used item. If there is a tie, then the least recently used key should be removed.

    get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.
'''

class LFUNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.times_used = 0
        self.next = None
        self.prev = None

class LFUCache:
    def __init__(self, n: int):
        if n <= 0:
            raise ValueError("n must be positive.")

        self.MAX_CACHE_SIZE = n
        self.head = None
        self.cache = dict()

    def _sort(self, node: LFUNode):
        while True:
            if not node.next:
                return

            after = node.next
            before = node.prev
            if after.times_used > node.times_used:
                return
            node.next = after.next
            node.prev = after
            if node.next:
                node.next.prev = node
            after.next = node
            after.prev = before
            if before:
                before.next = after
            else:
                self.head = after

    def set(self, key, value):
        if key in self.cache:
            self.cache[key].value = value
            self.cache[key].times_used += 1
            self._sort(self.cache[key])
        else:
            if len(self.cache) == self.MAX_CACHE_SIZE:
                pop_node = self.head
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
                self.cache.pop(pop_node.key)
            new_node = LFUNode(key, value)
            self.cache[key] = new_node
            if self.head:
                new_node.next = self.head
                self.head.prev = new_node
            self.head = new_node
            self._sort(self.head)
        return

    def get(self, key):
        if key not in self.cache:
            return None

        self.cache[key].times_used += 1
        self._sort(self.cache[key])
        return self.cache[key].value

c = LFUCache(3)

c.set('one', 1)
c.set('two', 2)
c.set('three', 3)
c.get('one')
c.set('four', 4)
c_ptr = c.head
while c_ptr:
    print(c_ptr.value)
    c_ptr = c_ptr.next