'''
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.
'''

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function for counting Unival Subtrees.
def count_unival_trees(root):
    total = 0
    left_flag = False
    right_flag = False

    # Check whether left and right nodes exist.
    left_flag = True if root.left == None else False
    right_flag = True if root.right == None else False

    # Check whether left and right node values match the root if they exist
    if not left_flag:
        left_flag = True if root.left.val == root.val else False
    if not right_flag:
        right_flag = True if root.right.val == root.val else False

    # Get the total.
    if left_flag and right_flag:
        total += 1
    if root.left != None:
        total += count_unival_trees(root.left)
    if root.right != None:
        total += count_unival_trees(root.right)

    return total

tree = TreeNode(0, TreeNode(1), TreeNode(0, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(0)))

print(count_unival_trees(tree))