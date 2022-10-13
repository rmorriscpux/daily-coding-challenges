/*
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
*/

class SLLNode {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class SLL {
    #len = 0;
    constructor() {
        this.head = null;
    }

    get length() {
        return this.#len;
    }

    addFront(value) {
        const newNode = new SLLNode(value);
        newNode.next = this.head;
        this.head = newNode;
        this.#len++;
        return this;
    }

    addBack(value) {
        const newNode = new SLLNode(value);
        if (this.head == null) {
            this.head = newNode;
        }
        else {
            let nodePtr = this.head;
            while (nodePtr.next != null) {
                nodePtr = nodePtr.next;
            }
            nodePtr.next = newNode;
        }
        this.#len++;
        return this;
    }
}

function getIntersection(M, N) {
    let mPtr = M.head;
    let nPtr = N.head;

    let lenDiff = M.length - N.length;

    if (lenDiff > 0) { // M is longer than N.
        for (let i = 0; i < lenDiff; i++) {
            mPtr = mPtr.next;
        }
    }
    else { // N is longer than or the same length as M.
        for (let i = lenDiff; i < 0; i++) {
            nPtr = nPtr.next;
        }
    }

    while (mPtr != null) {
        if (mPtr.value == nPtr.value) {
            return mPtr.value;
        }
        mPtr = mPtr.next;
        nPtr = nPtr.next;
    }

    return null;
}

M = new SLL();
M.addFront(10).addFront(8).addFront(9).addFront(3);

N = new SLL();
N.addFront(10).addFront(8).addFront(9).addFront(18).addFront(4).addFront(5);

console.log(getIntersection(M, N));