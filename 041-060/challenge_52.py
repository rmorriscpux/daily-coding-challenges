'''
Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

    set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item,
    then it should also remove the least recently used item.

    get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.
'''

# Implemented as a dictionary with keys set to nodes in a doubly-linked list to track the last used.
# Hybridizing in this way allows for tracking the order used in O(1) time.

class LRUNode:
    def __init__(self, key, value):
        # key is needed in the node class in order to accurately remove nodes.
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, cache_size: int):
        if cache_size <= 0:
            raise ValueError("cache_size must be positive.")
        self.cache_size = cache_size
        self.cache = {}
        self.head = LRUNode(None, None)
        self.tail = LRUNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _insertNode(self, node: LRUNode):
        # Get the next node after the head.
        next_node = self.head.next
        # Set the node after the head.
        node.next = next_node
        node.prev = self.head
        # Point back to the new node.
        next_node.prev = node
        self.head.next = node

    def _removeNode(self, node: LRUNode):
        next_node = node.next
        prev_node = node.prev
        prev_node.next = next_node
        next_node.prev = prev_node

    def set(self, key, value):
        # Case for where key already exists: Remove so we can update.
        if key in self.cache:
            self._removeNode(self.cache[key])
        # Add new node to cache.
        new_node = LRUNode(key, value)
        self._insertNode(new_node)
        self.cache[key] = new_node
        # Now remove the least-used node if the cache size is too big.
        if len(self.cache) > self.cache_size:
            last_node = self.tail.prev
            self._removeNode(last_node)
            del self.cache[last_node.key]
        return

    def get(self, key):
        if key not in self.cache:
            return None

        # Grab the node.
        get_node = self.cache[key]
        # Move the node to the front of the cache.
        self._removeNode(get_node)
        self._insertNode(get_node)

        return get_node.value

if __name__ == "__main__":
    c = LRUCache(3)

    c.set('one', 1)
    assert 'one' in c.cache
    c.set('two', 2)
    c.set('three', 3)
    print(c.get('one'), "was the first entered.")
    c.set('four', 4)
    assert 'one' in c.cache
    assert 'two' not in c.cache
    print(c.cache)