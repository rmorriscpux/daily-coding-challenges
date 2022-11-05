/*
Given the root to a binary search tree, find the second largest node in the tree.
*/

class BSTNode {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class BST {
    constructor(...values) {
        if (values.length == 0) {
            this.root = null;
            return;
        }

        values.forEach((v) => {
            this.add(v);
        });
    }

    add(value) {
        function rAddNode(value, curNode) {
            if (value < curNode.value) {
                if (curNode.left) {
                    rAddNode(value, curNode.left);
                } else {
                    curNode.left = new BSTNode(value);
                }
            } else if (value > curNode.value) {
                if (curNode.right) {
                    rAddNode(value, curNode.right);
                } else {
                    curNode.right = new BSTNode(value);
                }
            }
            return;
        }

        if (this.root) {
            rAddNode(value, this.root);
        } else {
            this.root = new BSTNode(value);
        }

        return this;
    }

    getSecondLargestNode() {
        function rGetSecondLargestNode(curNode) {
            // Case 1 - Node has no childred. Return node's value in a single value array.
            if (!(curNode.left || curNode.right)) {
                return [curNode.value];
            }
            // Case 2 - Node has a right child.
            if (curNode.right) {
                if (!(curNode.right.left || curNode.right.right)) {
                    // If right child has no children, return array containing curNode.data and curNode.right.data
                    return [curNode.right.value, curNode.value];
                } else {
                    // Else, return the two largest between the right child and the return value of its children.
                    const childValues = rGetSecondLargestNode(curNode.right);
                    if (childValues.length == 1) {
                        return childValues[0] > curNode.value ? [childValues[0], curNode.value] : [curNode.value, childValues[0]];
                    }
                    else { // childValues.length == 2
                        return curNode.right.value > childValues[0] ? [curNode.right.value, childValues[0]] : childValues;
                    }
                }
            }
            // Case 3 - Node has a left child and no right child.
            else {
                return [curNode.value, Math.max(rGetSecondLargestNode(curNode.left))];
            }
        }

        // Ensure there are at least two nodes in the tree.
        if (!this.root) {
            return null;
        }
        if (!(this.root.left || this.root.right)) {
            return null;
        }

        const result = rGetSecondLargestNode(this.root);
        return result[1];
    }
}

const tree = new BST(8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15);
console.log(tree.getSecondLargestNode());