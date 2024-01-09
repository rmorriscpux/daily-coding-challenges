'''
Implement a data structure which carries out the following operations without resizing the underlying array:

add(value): Add a value to the set of values.
check(value): Check whether a value is in the set.

The check method may return occasional false positives (in other words, incorrectly identifying an element as part of the set),
but should always correctly identify a true element.
'''

# The structure described in the problem is a Bloom filter, a highly space-efficient data structure.
# https://en.wikipedia.org/wiki/Bloom_filter

from hashlib import sha256 # Any hash algorithm can be used here. Note larger hash sizes produce less false positives.

class BloomFilter:
    def __init__(self):
        self.hash_sum = 0
        self._hashval = lambda h: int.from_bytes(bytes.fromhex(sha256(h.encode()).hexdigest()))

    def add(self, value):
        self.hash_sum |= self._hashval(value)
        return self

    def check(self, value) -> bool:
        val_hash = self._hashval(value)
        return val_hash & self.hash_sum == val_hash
    
if __name__ == "__main__":
    bf = BloomFilter()

    bf.add('abcd')
    bf.add('efgh')
    print(bf.check('abcd')) # True
    print(bf.check('efghi')) # False