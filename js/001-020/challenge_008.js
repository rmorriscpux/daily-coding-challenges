/*
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.
*/

class TreeNode {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

function countUnivalTrees(root) {
    function rCountUnivalTrees(node, count) {
        let leftFlag = node.left == null;
        let rightFlag = node.right == null;
    
        if (!leftFlag) { // TreeNode on left exists.
            leftFlag = (node.value == node.left.value) && rCountUnivalTrees(node.left, count);
        }
        if (!rightFlag) { // TreeNode on right exists.
            rightFlag = (node.value == node.right.value) && rCountUnivalTrees(node.right, count);
        }

        if (leftFlag && rightFlag) {
            count[0] += 1;
        }

        return (leftFlag && rightFlag);
    }
    
    count = [0];
    rCountUnivalTrees(root, count);
    return count[0];
}