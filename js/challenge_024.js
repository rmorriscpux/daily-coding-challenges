/*
Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

    is_locked, which returns whether the node is locked
    lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
    unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you would like.
You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes.
Each method should run in O(h), where h is the height of the tree.
*/

class TreeNode {
    #nodeLock = false;
    constructor(value, parent=null) {
        this.value = value;
        this.parent = parent;
        this.left = null;
        this.right = null;
    }

    addLeft(value) {
        if (this.left) {
            return false;
        }
        this.left = new TreeNode(value, this);
        return true;
    }

    addRight(value) {
        if (this.right) {
            return false;
        }
        this.right = new TreeNode(value, this);
        return true;
    }

    isLocked() {
        return this.#nodeLock;
    }

    checkAncestorsLock() {
        let notLockable = false;
        if (this.parent) {
            notLockable = this.parent.isLocked() || this.parent.checkAncestorsLock();
        }
        return notLockable;
    }

    checkDescendantsLock() {
        let notLockable = false;
        if (this.left) {
            notLockable = notLockable || this.left.isLocked() || this.left.checkDescendantsLock();
        }
        if (this.right) {
            notLockable = notLockable || this.right.isLocked() || this.right.checkDescendantsLock();
        }
        return notLockable;
    }

    lock() {
        if (this.#nodeLock) {
            return false;
        }

        if (this.checkAncestorsLock() && this.checkDescendantsLock()) {
            return false;
        }

        this.#nodeLock = true;
        return true;
    }

    unlock() {
        if (!this.#nodeLock) {
            return false;
        }

        if (this.checkAncestorsLock() && this.checkDescendantsLock()) {
            return false;
        }

        this.#nodeLock = false;
        return true;
    }
}