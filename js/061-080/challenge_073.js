/*
Given the head of a singly linked list, reverse it in-place.
*/

class SLLNode {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class SLL {
    #length = 0;

    constructor() {
        this.head = null;
        for (let i = arguments.length; i > 0; i--) {
            this.addToFront(arguments[i-1]);
        }
    }

    print() {
        let outStr = "";
        let nodePtr = this.head;
        while (nodePtr != null) {
            outStr = outStr.concat(nodePtr.data.toString());
            if (nodePtr.next != null) {
                outStr = outStr.concat("->");
            }
            nodePtr = nodePtr.next;
        }
        console.log(outStr);
        return;
    }

    addToFront(data) {
        const newNode = new SLLNode(data);
        newNode.next = this.head;
        this.head = newNode;
        this.#length++;
        return;
    }

    addToBack(data) {
        const newNode = new SLLNode(data);
        this.#length++;

        if (this.head == null) {
            this.head = newNode;
            return;
        }

        let nodePtr = this.head;
        while (nodePtr.next != null) {
            nodePtr = nodePtr.next;
        }
        nodePtr.next = newNode;
        return;
    }

    reverse() {
        if (this.head == null || this.head.next == null) {
            return;
        }

        let prv = this.head;
        let cur = this.head.next;
        prv.next = null;
        while (cur != null) {
            let nxt = cur.next;
            cur.next = prv;
            prv = cur;
            cur = nxt;
        }
        this.head = prv;
        return;
    }
}

const sll = new SLL(1, 2, 3, 4, 5);
sll.print();
sll.reverse();
sll.print();