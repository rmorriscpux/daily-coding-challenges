'''
Implement a PrefixMapSum class with the following methods:

insert(key: str, value: int): Set a given key's value in the map. If the key already exists, overwrite the value.
sum(prefix: str): Return the sum of all values of keys that begin with a given prefix.

For example, you should be able to run the following code:

    mapsum.insert("columnar", 3)
    assert mapsum.sum("col") == 3
    mapsum.insert("column", 2)
    assert mapsum.sum("col") == 5
'''

class PrefixMapSum:
    def __init__(self):
        self.num_dict = dict()

    def insert(self, key: str, value: int):
        self.num_dict[key] = value # Key is created if it doesn't exist.
        return self

    def sum(self, prefix: str) -> int:
        prefix_length = len(prefix) # Optimization
        prefix_sum = 0
        # Go through every key and check that the first characters match the input prefix.
        for key, value in self.num_dict.items():
            if prefix == key[:prefix_length]:
                prefix_sum += value
        return prefix_sum

if __name__ == "__main__":
    mapsum = PrefixMapSum()
    mapsum.insert("columnar", 3)
    assert mapsum.sum("col") == 3
    mapsum.insert("column", 2)
    assert mapsum.sum("col") == 5
    mapsum.insert("notcol", 4)
    assert mapsum.sum("col") == 5
    mapsum.insert("columnar", 7)
    assert mapsum.sum("col") == 9