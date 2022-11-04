'''
Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

  1
 / \
2   3
   / \
  4   5
'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

    def printLevelWise(self):
        def rPrint(node_ptr, depth, priority_queue):
            # Build a list of lists as we go. At the end we'll have lists ordered by level.
            if len(priority_queue) <= depth:
                priority_queue.append([])
            # Append the value to the current index's list.
            priority_queue[depth].append(node_ptr.value)
            # Recur into the node's children if they exist.
            if node_ptr.left:
                rPrint(node_ptr.left, depth+1, priority_queue)
            if node_ptr.right:
                rPrint(node_ptr.right, depth+1, priority_queue)

            return priority_queue

        priority_queue = rPrint(self, 0, [])

        # Concatenate the priority queue and print in order.
        out_list = []
        for depth_list in priority_queue:
            out_list.extend(depth_list)
        print(out_list)
        return

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

root.printLevelWise()