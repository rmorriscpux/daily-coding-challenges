'''
Two nodes in a binary tree can be called cousins if they are on the same level of the tree but have different parents.
For example, in the following diagram 4 and 6 are cousins.

    1
   / \
  2   3
 / \   \
4   5   6
Given a binary tree and a particular node, find all cousins of that node.
'''

from typing import List

class TreeNode:
    def __init__(self, data=None, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent

    def __str__(self) -> str:
        return f"{self.data}"
    
    def __repr__(self) -> str:
        out_str = "TreeNode(" + str(self)
        if self.left:
            out_str += " | L:" + repr(self.left)
        if self.right:
            out_str += " | R:" + repr(self.right)
        out_str += ")"
        return out_str
    
def getNodeCousins(target_node: TreeNode):
    # Recursive subroutine to descend down to every node on the same level as the original node.
    def rGetNodeCousins(to_descend: int, cur_node: TreeNode, orig_node: TreeNode, cousin_list: List[TreeNode]) -> None:
        if to_descend == 0:
            # When at the level as orig_node, add the node unless it's orig_node.
            if cur_node != orig_node:
                cousin_list.append(cur_node)
        else:
            # Descend to each child if they exist.
            if cur_node.left:
                rGetNodeCousins(to_descend-1, cur_node.left, orig_node, cousin_list)
            if cur_node.right:
                rGetNodeCousins(to_descend-1, cur_node.right, orig_node, cousin_list)
        return
    
    node_ptr = target_node
    levels = 0
    # Go to the parent until the root node is reached, counting levels along the way.
    while type(node_ptr.parent) == TreeNode:
        node_ptr = node_ptr.parent
        levels += 1
    # Populate cousin_list and return.
    cousin_list = []
    rGetNodeCousins(levels, node_ptr, target_node, cousin_list)
    return cousin_list

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2, root)
    root.right = TreeNode(3, root)
    root.left.left = TreeNode(4, root.left)
    root.left.right = TreeNode(5, root.left)
    root.right.right = TreeNode(6, root.right)

    target_node = root.right.right

    print(getNodeCousins(target_node))