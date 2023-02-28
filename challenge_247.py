'''
Given a binary tree, determine whether or not it is height-balanced.
A height-balanced binary tree can be defined as one in which the heights of the two subtrees of any node never differ by more than one.
'''

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.data})"
    
def isHeightBalanced(root: TreeNode) -> bool:
    def rIsHeightBalanced(node):
        # Branch bottom. No node, return default values.
        if not node:
            return (0, True)
        
        left_bal = rIsHeightBalanced(node.left)
        right_bal = rIsHeightBalanced(node.right)

        # Total height is the max of left and right branches plus one.
        height = max(left_bal[0], right_bal[0]) + 1
        # Balanced if the branches are balanced and the heights do not differ by more than 1.
        balanced = abs(left_bal[0] - right_bal[0]) <= 1 and left_bal[1] and right_bal[1]

        return (height, balanced)
    
    return rIsHeightBalanced(root)[1]

root = TreeNode(0)
root.left = TreeNode(1)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(5)
root.left.right.right = TreeNode(6)
root.right = TreeNode(7)
root.right.left = TreeNode(8)
root.right.left.left = TreeNode(9)
root.right.left.right = TreeNode(10)
root.right.right = TreeNode(11)
root.right.right.left = TreeNode(12)

print(isHeightBalanced(root))