'''
Generate a finite, but an arbitrarily large binary tree quickly in O(1).

That is, generate() should return a tree whose size is unbounded but finite.
'''

from random import random

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def count(self):
        total = 1
        if self.left:
            total += self.left.count()
        if self.right:
            total += self.right.count()
        return total

# Effectively, this is a linked list. Each node will only have one branch.
def generate(size: int):
    if size <= 0:
        raise ValueError("size must be positive.")
    start = TreeNode(0)
    current = start

    for i in range(1, size):
        if random() < 0.5:
            current.left = TreeNode(i)
            current = current.left
        else:
            current.right = TreeNode(i)
            current = current.right

    return start

tree = generate(100)
print(tree.count())
tree2 = generate(200)
print(tree2.count())