/*
Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.
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
        for (let i = arguments.length-1; i >= 0; i--) {
            this.addToFront(arguments[i]);
        }
    }

    get length() {
        return this.#len;
    }

    print() {
        let outStr = "";
        let nodePtr = this.head;
        while (nodePtr != null) {
            outStr = outStr.concat(nodePtr.value.toString());
            if (nodePtr.next != null) {
                outStr = outStr.concat(" -> ");
            }
            nodePtr = nodePtr.next;
        }
        console.log(outStr);
        return;
    }

    addToFront(value) {
        const newNode = new SLLNode(value);
        newNode.next = this.head;
        this.head = newNode;
        this.#len++;
        return;
    }

    addToBack(value) {
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
        return;
    }

    removeFront() {
        if (this.head != null) {
            let popNode = this.head;
            this.head = this.head.next;
            this.#len--;
            return popNode.value;
        }
        return null;
    }
}

function mergeSortedLists(linkedLists) {
    const mergedList = new SLL();
    if (linkedLists.length == 0) {
        return mergedList;
    }

    while (true) {
        let curMinIndex = null;
        for (let i = 0; i < linkedLists.length; i++) {
            // Ignore empty lists.
            if (linkedLists[i].length == 0) {
                continue;
            }
            if (curMinIndex == null) {
                curMinIndex = i;
            }
            else if (linkedLists[i].head.value < linkedLists[curMinIndex].head.value) {
                curMinIndex = i;
            }
        }

        // Merge complete.
        if (curMinIndex == null) {
            break;
        }

        // Remove the minimum value among all input linked lists and add it to the back of the merged list.
        let popNode = linkedLists[curMinIndex].removeFront();
        mergedList.addToBack(popNode);

        for (l of linkedLists) {
            delete l;
        }
    }

    return mergedList;
}

const list1 = new SLL(1, 5, 9);
const list2 = new SLL(2, 6, 7);
const list3 = new SLL(3, 4, 8);

list1.print();
list2.print();
list3.print();

const mergedList = mergeSortedLists([list1, list2, list3]);

mergedList.print();