'''
Given a binary tree of integers, find the maximum path sum between two nodes.
The path must go through at least one node, and does not need to go through the root.
'''

class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

def largestTreePathSum(root: TreeNode):
    def rLargestTreePathSum(node, parent_sum):
        # Calculate the current sum. Do not include the parent sum if it is negative.
        current_sum = max(node.value, node.value + parent_sum)
        # Now recur into children and determine the maximum from that.
        max_sum = current_sum
        if type(node.left) == TreeNode:
            max_sum = max(max_sum, rLargestTreePathSum(node.left, current_sum))
        if type(node.right) == TreeNode:
            max_sum = max(max_sum, rLargestTreePathSum(node.right, current_sum))

        return max_sum

    # Start with the root value, use -∞ (or system minimum integer) as the initial "sum".
    return rLargestTreePathSum(root, -float("inf"))

'''
Expected return: 28
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
print(largestTreePathSum(root))

'''
Expected return: 23
     -5
     / \
    3   6
   / \   \
  1   4   8
 / \     / \
0   2   7   9
'''

root2 = TreeNode(-5)
root2.left = TreeNode(3)
root2.left.left = TreeNode(1)
root2.left.left.left = TreeNode(0)
root2.left.left.right = TreeNode(2)
root2.left.right = TreeNode(4)
root2.right = TreeNode(6)
root2.right.right = TreeNode(8)
root2.right.right.left = TreeNode(7)
root2.right.right.right = TreeNode(9)
print(largestTreePathSum(root2))

'''
Expected return: 12
      5
     / \
    3  -6
   / \   \
  1   4  -8
 / \     / \
0   2  -7  -9
'''

root3 = TreeNode(5)
root3.left = TreeNode(3)
root3.left.left = TreeNode(1)
root3.left.left.left = TreeNode(0)
root3.left.left.right = TreeNode(2)
root3.left.right = TreeNode(4)
root3.right = TreeNode(-6)
root3.right.right = TreeNode(-8)
root3.right.right.left = TreeNode(-7)
root3.right.right.right = TreeNode(-9)
print(largestTreePathSum(root3))

'''
Expected return: 5
      5
     / \
   -3  -6
   / \   \
 -1  -4  -8
 / \     / \
0  -2  -7  -9
'''

root4 = TreeNode(5)
root4.left = TreeNode(-3)
root4.left.left = TreeNode(-1)
root4.left.left.left = TreeNode(0)
root4.left.left.right = TreeNode(-2)
root4.left.right = TreeNode(-4)
root4.right = TreeNode(-6)
root4.right.right = TreeNode(-8)
root4.right.right.left = TreeNode(-7)
root4.right.right.right = TreeNode(-9)
print(largestTreePathSum(root4))

'''
Expected return: 0
     -5
     / \
   -3  -6
   / \   \
 -1  -4  -8
 / \     / \
0  -2  -7  -9
'''

root5 = TreeNode(-5)
root5.left = TreeNode(-3)
root5.left.left = TreeNode(-1)
root5.left.left.left = TreeNode(0)
root5.left.left.right = TreeNode(-2)
root5.left.right = TreeNode(-4)
root5.right = TreeNode(-6)
root5.right.right = TreeNode(-8)
root5.right.right.left = TreeNode(-7)
root5.right.right.right = TreeNode(-9)
print(largestTreePathSum(root5))