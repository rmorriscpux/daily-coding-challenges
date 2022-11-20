'''
Given a binary tree where all nodes are either 0 or 1, prune the tree so that subtrees containing all 0s are removed.

For example, given the following tree:

   0
  / \
 1   0
    / \
   1   0
  / \
 0   0

should be pruned to:

   0
  / \
 1   0
    /
   1

We do not remove the tree at the root or its left child because it still has a 1 as a descendant.
'''

class TreeNode:
    def __init__(self, value: int):
        self.value = int(bool(value))
        self.left = None
        self.right = None

    # Printable representation of tree starting at the node object.
    def __repr__(self):
        out_str = f"TreeNode({self.value})"
        if self.left or self.right:
            out_str += "->"
            if self.left:
                out_str += f"left:[{repr(self.left)}]"
            if self.left and self.right:
                out_str += ", "
            if self.right:
                out_str += f"right:[{repr(self.right)}]"
        return out_str

    def pruneTree(self):
        # Check left side.
        if self.left:
            self.left = self.left.pruneTree()
        # Check right side.
        if self.right:
            self.right = self.right.pruneTree()
        # Return
        return self if self.value == 1 or self.left or self.right else None

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(0)
root.right.left = TreeNode(1)
root.right.left.left = TreeNode(0)
root.right.left.right = TreeNode(0)
root.right.right = TreeNode(0)

print(root)

root.pruneTree()

print(root)

# Limitation: Pruning a tree of all 0's will result in the original root node by itself with no children.
# If we want None, assign the root node to the result of its pruneTree() method {root = root.pruneTree()}
root2 = TreeNode(0)
root2.left = TreeNode(0)
root2.right = TreeNode(0)

print(root2)

root2.pruneTree()

print(root2)