'''
Given an integer N, construct all possible binary search trees with N nodes.
'''

from copy import deepcopy
from typing import List

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        out_str = str(self.value)
        if self.left:
            out_str += f" | L: ({str(self.left)})"
        if self.right:
            out_str += f" | R: ({str(self.right)})"
        return out_str

    def __repr__(self):
        return f"Tree({str(self)})"
    
def constructTrees(N: int):
    def rConstructTrees(node_values: List[int]):
        if not node_values:
            # Node values are empty. Return list with None as an item to represent an empty branch.
            return [None]

        trees = []
        for index, root_val in enumerate(node_values):
            root = TreeNode(root_val)
            # Construct list of left branches and list of right branches.
            # Since list is pre-ordered, all node values on the left branch will be less than root value
            # and all node values on the right branch will be greater than root value. This fits the rules for binary search tree architecture.
            left_branches = rConstructTrees(node_values[:index])
            right_branches = rConstructTrees(node_values[index+1:])
            for lb in left_branches:
                for rb in right_branches:
                    # Attach each combination of left and right branches to the root node, then append a deep copy to the output list.
                    root.left = lb
                    root.right = rb
                    trees.append(deepcopy(root))

        return trees
    
    if N <= 0:
        return []
    # Ordered list of values.
    all_nodes = [TreeNode(value) for value in range(0, N)]
    # Build list to return recursively.
    return rConstructTrees(all_nodes)

all_trees = constructTrees(5)
print(all_trees)
print(f"Total Trees: {len(all_trees)}")