'''
Given a tree, find the largest tree/subtree that is a BST.

Given a tree, return the size of the largest tree/subtree that is a BST.
'''

# A node is part of a binary search tree (BST) if:
# - Its left descendants, if they exist, have values less than its own value.
# - Its right descendants, if they exist, have values greater than its own value.
# - Its children, if any exist, also meet the above criteria.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.value})"

# Returns the root node and size of the largest binary search tree.
# If multiple BST sizes are equal, the leftmost BST root node will be returned.
def getLargestBST(root: TreeNode):
    def rGetLargestBST(node, left_bound, right_bound):
        # Determine if the current node has BST properties. Additionally, recur into left and right nodes if they exist.
        # Assume BST until proven otherwise. Leaves with no children within bounds count as BSTs.
        is_bst = (node.value > left_bound) and (node.value < right_bound)
        left_root, left_size, left_is_bst = None, 0, True
        right_root, right_size, right_is_bst = None, 0, True
        new_left_bound, new_right_bound = node.value, node.value
        if node.left:
            if node.left.value > node.value:
                is_bst = False
                new_right_bound = float("inf")
            left_root, left_size, left_is_bst = rGetLargestBST(node.left, left_bound, new_right_bound)
        if node.right:
            if node.right.value < node.value:
                is_bst = False
                new_left_bound = -float("inf")
            right_root, right_size, right_is_bst = rGetLargestBST(node.right, new_left_bound, right_bound)

        # Both subtrees must be BSTs or empty for this node to be the root of a BST.
        is_bst = is_bst and left_is_bst and right_is_bst

        # Case where the node is the root of a BST.
        if is_bst:
            tree_root = node
            size = left_size + right_size + 1
        # When it is not a BST, compare the sizes returned from left and right, and return the largest.
        else:
            tree_root, size = (left_root, left_size) if left_size >= right_size else (right_root, right_size)

        return tree_root, size, is_bst

    # Only need to retrieve the first two variables from the top level recursion.
    bst_root, bst_size, _ = rGetLargestBST(root, -float("inf"), float("inf"))
    return bst_root, bst_size

'''
Full tree is a binary search tree.
      5
     / \
    3   6
   / \   \
  1   4   8
 / \     / \
0   2   7   9
'''

root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.left.left.left = TreeNode(0)
root.left.left.right = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(7)
root.right.right.right = TreeNode(9)

print(getLargestBST(root))

'''
Root is not a binary search tree, but its children are.
      1
     / \
    4   6
   / \   \
  2   5   8
 / \     / \
0   3   7   9
'''

root2 = TreeNode(1)
root2.left = TreeNode(4)
root2.left.left = TreeNode(2)
root2.left.left.left = TreeNode(0)
root2.left.left.right = TreeNode(3)
root2.left.right = TreeNode(5)
root2.right = TreeNode(6)
root2.right.right = TreeNode(8)
root2.right.right.left = TreeNode(7)
root2.right.right.right = TreeNode(9)

print(getLargestBST(root2))

'''
Left branch has a leaf greater than its grandparent node (invalid BST setup on left side).
      5
     / \
    2   6
   / \   \
  1   4   8
 / \     / \
0   3   7   9
'''

root3 = TreeNode(5)
root3.left = TreeNode(2)
root3.left.left = TreeNode(1)
root3.left.left.left = TreeNode(0)
root3.left.left.right = TreeNode(3)
root3.left.right = TreeNode(4)
root3.right = TreeNode(6)
root3.right.right = TreeNode(8)
root3.right.right.left = TreeNode(7)
root3.right.right.right = TreeNode(9)

print(getLargestBST(root3))