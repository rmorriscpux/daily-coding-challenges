'''
Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

    is_locked, which returns whether the node is locked
    lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
    unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you would like.
You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes.
Each method should run in O(h), where h is the height of the tree.
'''

class TreeNode:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self._lock = False

    def add_left(self, data):
        if self.left != None:
            return False
        
        self.left = TreeNode(data, self)
        return True

    def add_right(self, data):
        if self.right != None:
            return False
        
        self.right = TreeNode(data, self)
        return True

    def is_locked(self):
        return self._lock

    def _checkAncestorsLock(self):
        not_lockable = False
        if self.parent != None:
            not_lockable = self.parent.is_locked() or self.parent._checkAncestorsLock()
        return not_lockable

    def _checkDescendantsLock(self):
        not_lockable = False
        if self.left != None:
            not_lockable = not_lockable or self.left.is_locked() or self.left._checkDescendantsLock()
        if self.right != None:
            not_lockable = not_lockable or self.right.is_locked() or self.right._checkDescendantsLock()
        return not_lockable

    def lock(self):
        # Node is already locked.
        if self._lock:
            return False

        # Node is not lockable if both at least one ancestor and one descendant are locked.
        if self._checkAncestorsLock() and self._checkDescendantsLock():
            return False
        
        # Lock the node.
        self._lock = True
        return True

    def unlock(self):
        # Node is already unlocked.
        if not self._lock:
            return False

        # Node is not unlockable if both at least one ancestor and one descendant are locked.
        if self._checkAncestorsLock() and self._checkDescendantsLock():
            return False
        
        # Lock the node.
        self._lock = False
        return True