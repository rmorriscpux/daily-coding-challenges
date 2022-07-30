'''
Given the root to a binary search tree, find the second largest node in the tree.
'''

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self, data=None):
        self.root = BSTNode(data) if data != None else None

    def insert(self, data):
        def rInsert(node_ptr, data):
            if data < node_ptr.data:
                if node_ptr.left:
                    rInsert(node_ptr.left, data)
                else:
                    node_ptr.left = BSTNode(data)
            else:
                if node_ptr.right:
                    rInsert(node_ptr.right, data)
                else:
                    node_ptr.right = BSTNode(data)
            return
        
        if not self.root:
            self.root = BSTNode(data)
        else:
            rInsert(self.root, data)
        
        return self

    def getDataList(self):
        if not self.root:
            return []

        def rDataList(node_ptr):
            item_list = []
            if node_ptr.left:
                item_list.extend(rDataList(node_ptr.left))
            item_list.append(node_ptr.data)
            if node_ptr.right:
                item_list.extend(rDataList(node_ptr.right))
            return item_list

        return rDataList(self.root)

    # Slow, lazy implementation
    def getSecondLargestNode(self):
        l = self.getDataList()
        if len(l) >= 2:
            return l[-2]
        return

x = BST(5)
x.insert(3).insert(7).insert(4).insert(6)
print(x.getDataList())
print(x.getSecondLargestNode())