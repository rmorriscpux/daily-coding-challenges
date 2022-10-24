/*
Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
*/

class SLLNode {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

// The trick is to have a private length property in the SLL class that is updated whenever nodes are added or removed.
// It is then possible to deduce how far to go without having to backtrack.
class SLL {
    #length = 0;
    constructor(...args) {
        if (args.length == 0) {
            this.head = null;
            return;
        }
        this.head = new SLLNode(args[0]);
        this.#length++;
        let nodePtr = this.head;
        for (let i = 1; i < args.length; i++) {
            nodePtr.next = new SLLNode(args[i]);
            this.#length++;
            nodePtr = nodePtr.next;
        }
    }

    get length() {
        return this.#length;
    }

    addFront(value) {
        let newNode = new SLLNode(value);
        newNode.next = this.head;
        this.head = newNode;
        this.#length++;
        return;
    }

    addBack(value) {
        if (!this.head) {
            this.head = new SLLNode(value);
        }
        else {
            let nodePtr = this.head;
            while (nodePtr.next) {
                nodePtr = nodePtr.next;
            }
            nodePtr.next = new SLLNode(value);
        }
        this.#length++;
        return;
    }

    removeKthLastElement(k) {
        if (!this.head || k <= 0 || k > this.#length) {
            return null;
        }

        let poppedValue = null;
        if (k == this.#length) {
            poppedValue = this.head.value;
            this.head = this.head.next;
        }
        else {
            let nodePtr = this.head;
            for (let i = 0; i < this.#length-k-1; i++) {
                nodePtr = nodePtr.next;
            }
            poppedValue = nodePtr.next.value;
            nodePtr.next = nodePtr.next.next;
        }

        this.#length--;
        return poppedValue;
    }

    printAsList() {
        let outStr = "[ "
        let nodePtr = this.head;
        while (nodePtr) {
            outStr = outStr.concat(nodePtr.value.toString());
            if (nodePtr.next) {
                outStr = outStr.concat(", ");
            }
            nodePtr = nodePtr.next;
        }
        outStr = outStr.concat(" ]");
        console.log(outStr);
        return;
    }
}

const l1 = new SLL(1, 2, 3, 4, 5);
l1.printAsList();
l1.removeKthLastElement(4);
l1.printAsList();
l1.removeKthLastElement(4);
l1.printAsList();
console.log(l1.length);