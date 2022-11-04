'''
Given a binary tree, return all paths from the root to leaves.

For example, given the tree

   1
  / \
 2   3
    / \
   4   5

it should return [[1, 2], [1, 3, 4], [1, 3, 5]].
'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def allPaths(self):
        # Use recursive function that builds a separate path up to each leaf, then place the path in a list when the leaf is reached.
        def rAllPaths(node_ptr: TreeNode, all_paths: list, current_path: list=[]):
            if not (node_ptr.left or node_ptr.right):
                # Current node is a leaf. Append final path to all_paths.
                all_paths.append(current_path + [node_ptr.value])
            else:
                # Otherwise, current node is a branch. Traverse down further, adding node_ptr's value to the current_path list.
                if node_ptr.left:
                    rAllPaths(node_ptr.left, all_paths, current_path + [node_ptr.value])
                if node_ptr.right:
                    rAllPaths(node_ptr.right, all_paths, current_path + [node_ptr.value])
            return

        all_paths = []
        rAllPaths(self, all_paths)
        return all_paths

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.right.left = TreeNode(4)
root1.right.right = TreeNode(5)

root2 = TreeNode(10)

print(root1.allPaths())
print(root2.allPaths())