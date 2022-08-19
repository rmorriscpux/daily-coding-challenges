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

    # Quicker implementation.
    def getSecondLargestNode2(self):
        def rGetSecondLargestNode2(node_ptr):
            # Case 1: Node has no children. Return single value tuple.
            if not node_ptr.left and not node_ptr.right:
                return (node_ptr.data,)
            # Case 2: Node has right child.
            elif node_ptr.right:
                # If right child has no children, return tuple containing node_ptr.data and node_ptr.right.data
                if not node_ptr.right.left and not node_ptr.right.right:
                    return (node_ptr.right.data, node_ptr.data)
                # Else, return the two largest between the right child and the return value of its children.
                else:
                    t = rGetSecondLargestNode2(node_ptr.right)
                    if len(t) == 1:
                        return (t[0], node_ptr.data) if t[0] > node_ptr.data else (node_ptr.data, t[0])
                    else: # len(t) == 2
                        if node_ptr.right.data > t[0]: # Coming from the left side of the right node.
                            return (node_ptr.right.data, t[0])
                        else:
                            return t # Coming from the left child of the right node.
            # Case 3: Node has left child and no right child. Second largest is the max of what's descended from the left child.
            else:
                return (node_ptr.data, max(rGetSecondLargestNode2(node_ptr.left)))

        # Check if 0 or 1 node in tree. In this case, there is no second largest node.
        if not self.root:
            return None
        if not self.root.left and self.root.right:
            return None

        result = rGetSecondLargestNode2(self.root)
        return result[1]

x = BST(5)
x.insert(3).insert(7).insert(4).insert(6)
print(x.getDataList())
print(x.getSecondLargestNode())
print(x.getSecondLargestNode2())