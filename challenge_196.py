'''
Given the root of a binary tree, find the most frequent subtree sum. The subtree sum of a node is the sum of all values under a node, including the node itself.

For example, given the following tree:

  5
 / \
2  -5
Return 2 as it occurs twice: once as the left leaf, and once as the sum of 2 + 5 - 5.
'''

class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"TreeNode({self.value})"

def mostFrequentSum(root: TreeNode):
    def rMostFrequentSum(node: TreeNode, sum_dict: dict):
        left_sum, right_sum = 0, 0

        # Recur into left and right children if they exist.
        if node.left:
            left_sum = rMostFrequentSum(node.left, sum_dict)
        if node.right:
            right_sum = rMostFrequentSum(node.right, sum_dict)

        node_sum = node.value + left_sum + right_sum

        # Add this node's tree sum to the dictionary. Dictionaries are passed by reference so it will be full when the routine completes.
        if node_sum not in sum_dict:
            sum_dict[node_sum] = 0
        sum_dict[node_sum] += 1

        return node_sum

    sum_dict = {}
    rMostFrequentSum(root, sum_dict)

    return max(sum_dict) # max() with a dictionary parameter returns the key containing the highest value.

root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(-5)
root.right.left = TreeNode(-2)
root.right.right = TreeNode(2)

print(mostFrequentSum(root))