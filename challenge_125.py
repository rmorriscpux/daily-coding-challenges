'''
Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.

For example, given the following tree and K of 20

    10
   /   \
 5      15
       /  \
     11    15

Return the nodes 5 and 15.
'''

class BSTNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self, *values: int):
        self.root = None

        for v in values:
            self.add(v)

    def add(self, value: int):
        if not self.root:
            self.root = BSTNode(value)
            return self

        def rAdd(node, value):
            if value < node.value:
                if node.left:
                    rAdd(node.left, value)
                else:
                    node.left = BSTNode(value)
            else:
                if node.right:
                    rAdd(node.right, value)
                else:
                    node.right = BSTNode(value)
            return

        rAdd(self.root, value)
        return self

    def sumToK(self, K: int):
        def buildList(node, t_list):
            if node.left:
                buildList(node.left, t_list)
            t_list.append(node.value)
            if node.right:
                buildList(node.right, t_list)
            return

        t_list = []
        buildList(self.root, t_list)

        for i in range(0, len(t_list)-1):
            if t_list[i] > K:
                return None

            for j in range(len(t_list)-1, i, -1):
                if t_list[i] + t_list[j] == K:
                    return t_list[i], t_list[j]
                elif t_list[i] + t_list[j] < K:
                    break

        return None

