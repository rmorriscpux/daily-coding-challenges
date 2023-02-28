'''
A tree is symmetric if its data and shape remain unchanged when it is reflected about the root node. The following tree is an example:

        4
      / | \
    3   5   3
  /           \
9              9
Given a k-ary tree, determine whether it is symmetric.
'''

# Using NumPy for its support of fixed-length arrays with mutable items. NumPy is not in standard Python but is utilized widely. 
# Standard lists can be used for the TreeNode class as a substitute, but their length can be modified.
import numpy as np
from copy import deepcopy

# Number of children per node.
K = 3

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.children = np.empty(K, dtype=object) # K-length 1D array filled with None. Python list declaration equivalent: self.children = [None] * K

# Makes a deep copy of the K-ary tree reversed.
def reverseCopyTree(root: TreeNode):
    # Recursive subroutine.
    def rReverseTree(node: TreeNode):
        # Flip the positions of the node's children symmetrically.
        i = 0
        while i < K/2:
            temp = node.children[i]
            node.children[i] = node.children[~i]
            node.children[~i] = temp
            i += 1
        # Recur into each child.
        for child in node.children:
            if child:
                rReverseTree(child)

        return

    reverse_tree = deepcopy(root)
    rReverseTree(reverse_tree)

    return reverse_tree

def isSymmetrical(root: TreeNode):
    # Recursive routine.
    def rIsSymmetrical(node1: TreeNode, node2: TreeNode):
        # Compare node values, return False if they are not the same.
        if node1.val != node2.val:
            return False
        # Compare children.
        for i in range(0, K):
            # Move on if children don't exist at position i for either tree.
            if not (node1.children[i] or node2.children[i]):
                continue
            # Child only exists at position i for one node. Tree is asymmetrical.
            if (node1.children[i] and not node2.children[i]) or (not node1.children[i] and node2.children[i]):
                return False
            # Recur into the children at position i; return False if it ultimately returns False.
            if not rIsSymmetrical(node1.children[i], node2.children[i]):
                return False
        # No problems, so return True.
        return True

    rvrse_root = reverseCopyTree(root)

    return rIsSymmetrical(root, rvrse_root)

if __name__ == "__main__":
    root = TreeNode(4)
    root.children[0] = TreeNode(3)
    root.children[0].children[0] = TreeNode(9)
    root.children[1] = TreeNode(5)
    root.children[2] = TreeNode(3)
    root.children[2].children[2] = TreeNode(9)

    print(isSymmetrical(root))

    root.children[2].children[0] = TreeNode(1)

    print(isSymmetrical(root))