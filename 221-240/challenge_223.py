'''
Typically, an implementation of in-order traversal of a binary tree has O(h) space complexity, where h is the height of the tree.
Write a program to compute the in-order traversal of a binary tree using O(1) space.
'''

# While not typically thought about, every function call in Python uses space in memory much like every instance of an object, including recursive calls.
# Thus a recursive function going from the root to the bottom of a binary tree has O(h) space complexity.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def compactTreeTraversal(root: TreeNode):
    curr_node = root

    while curr_node:
        # Print curr_node.data if no left child.
        if not curr_node.left:
            print(curr_node.data)
            curr_node = curr_node.right
        else:
            # Get to the rightmost node on curr_node's left branch, stopping at a circular reference.
            rightmost_on_left = curr_node.left
            while rightmost_on_left.right and (rightmost_on_left.right != curr_node):
                rightmost_on_left = rightmost_on_left.right
            # Add reference back to curr_node if it doesn't exist. Otherwise, remove the reference, print curr_node.data, and go right from there.
            if not rightmost_on_left.right:
                rightmost_on_left.right = curr_node
                curr_node = curr_node.left
            else:
                rightmost_on_left.right = None
                print(curr_node.data)
                curr_node = curr_node.right

root = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right = TreeNode(7)
root.right.right = TreeNode(9)
root.right.right.left = TreeNode(8)

compactTreeTraversal(root)