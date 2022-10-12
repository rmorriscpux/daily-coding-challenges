'''
Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, and satisfies the constraint
that the key in the left child must be less than or equal to the root and the key in the right child must be greater than or equal to the root.
'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def isBST(root: TreeNode):
    valid_bst = type(root) == TreeNode

    # Check that the left side is a valid BST if it exists.
    if root.left:
        if root.left.value > root.value:
            return False
        valid_bst = valid_bst and isBST(root.left)

    # Check that the right side is a valid BST if it exists.
    if root.right:
        if root.right.value < root.value:
            return False
        valid_bst = valid_bst and isBST(root.right)

    return valid_bst

bst = TreeNode(5)
bst.left = TreeNode(3)
bst.left.left = TreeNode(2)
bst.left.left.left = TreeNode(1)
bst.left.right = TreeNode(4)
bst.right = TreeNode(7)
bst.right.left = TreeNode(6)
bst.right.right = TreeNode(8)
bst.right.right.right = TreeNode(9)

not_bst = TreeNode(5)
not_bst.right = TreeNode(3)
not_bst.right.right = TreeNode(2)
not_bst.right.right.right = TreeNode(1)
not_bst.right.left = TreeNode(4)
not_bst.left = TreeNode(7)
not_bst.left.right = TreeNode(6)
not_bst.left.left = TreeNode(8)
not_bst.left.left.left = TreeNode(9)

print(isBST(bst))
print(isBST(not_bst))