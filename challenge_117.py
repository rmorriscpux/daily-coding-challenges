'''
Given a binary tree, return the level of the tree with minimum sum.
'''

# Task: Sum all nodes on a level, finding the lowest sum, and return the level.

class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

def minSumLevel(root: TreeNode):
    # Recursive function takes in the current level and a list of nodes.
    def rMinSumLevel(level, nodes):
        current_sum = 0
        child_nodes = []

        for n in nodes:
            # Sum the value in each node.
            current_sum += n.value
            # Create a list of all the nodes' children that are on the next level.
            if n.left:
                child_nodes.append(n.left)
            if n.right:
                child_nodes.append(n.right)
        
        # If any child nodes were found, recur down and compare to the current level. Tracking the lowest sum and its level throughout.
        if child_nodes:
            lowest_sum, lowest_level = rMinSumLevel(level+1, child_nodes)
            if current_sum <= lowest_sum:
                lowest_sum = current_sum
                lowest_level = level
            return lowest_sum, lowest_level

        return current_sum, level

    lowest_sum, lowest_level = rMinSumLevel(0, [root])
    return lowest_level