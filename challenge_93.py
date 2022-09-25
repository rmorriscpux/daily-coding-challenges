'''
Given a tree, find the largest tree/subtree that is a BST.

Given a tree, return the size of the largest tree/subtree that is a BST.
'''

# A node is part of a binary search tree (BST) if:
# - Its left child, if it exists, has a value less than its own value.
# - Its right child, if it exists, has a value greater than its own value.
# - Its children, if any exist, also meet the above criteria.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Returns the root node and size of the largest binary search tree.
def getLargestBST(root: TreeNode):
    def rGetLargestBST(node):
        # Determine if the current node has BST properties. Additionally, recur into left and right nodes if they exist.
        # Assume BST until proven otherwise. Leaves with no children count as BSTs.
        is_bst = True
        left_root, left_size, left_is_bst = None, 0, True
        right_root, right_size, right_is_bst = None, 0, True
        if node.left:
            left_root, left_size, left_is_bst = rGetLargestBST(node.left)
            if node.left.value > node.value:
                is_bst = False
        if node.right:
            right_root, right_size, right_is_bst = rGetLargestBST(node.right)
            if node.right.value < node.value:
                is_bst = False

        # Both subtrees must be BSTs or empty for this node to be the root of a BST.
        is_bst = is_bst and left_is_bst and right_is_bst

        # Case where the node is the root of a BST.
        if is_bst:
            tree_root = node
            size = left_size + right_size + 1
        # When it is not a BST, compare the sizes returned from left and right, and return the largest.
        else:
            tree_root, size = left_root, left_size if left_size >= right_size else right_root, right_size

        return tree_root, size, is_bst

    bst_root, bst_size, _ = rGetLargestBST(root)
    return bst_root, bst_size