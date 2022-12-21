/*
Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods:
enqueue, which inserts an element into the queue, and dequeue, which removes it.
*/

class Stack {
    #top = null;

    constructor() {
    }

    // Using an object structure that contains the next stack node as the stack node.
    push(data) {
        const lastTop = this.#top;
        this.#top = {
            'data' : data,
            'next' : lastTop
        };
        return;
    }

    pop() {
        if (this.#top == null) {
            return null;
        }

        let outData = this.#top.data;
        this.#top = this.#top.next;

        return outData;
    }

    isEmpty() {
        return this.#top == null;
    }

    // Print Methods
    toString() {
        let stackStr = "";
        let nodePtr = this.#top;

        while (nodePtr != null) {
            stackStr = stackStr.concat(nodePtr.data.toString());
            if (nodePtr.next != null) {
                stackStr = stackStr.concat("->");
            }
            nodePtr = nodePtr.next;
        }

        return stackStr;
    }

    printStack() {
        console.log(this.toString().concat("<Stack Top>"));
        return;
    }
}

class Queue {
    #holdStack = new Stack();
    #flipStack = new Stack();

    constructor() {
    }

    // Enqueue pushes the main holdStack to the flipStack from top to bottom, pushes the data to the holdStack, then flips the flipStack back.
    enqueue(data) {
        while (!this.#holdStack.isEmpty()) {
            this.#flipStack.push(this.#holdStack.pop());
        }

        this.#holdStack.push(data);

        while(!this.#flipStack.isEmpty()) {
            this.#holdStack.push(this.#flipStack.pop());
        }

        return;
    }

    // Dequeue simply calls pop() on the holdStack.
    dequeue() {
        return this.#holdStack.pop();
    }

    isEmpty() {
        return this.#holdStack.isEmpty();
    }

    // Print Methods
    toString() {
        return this.#holdStack.toString();
    }

    printQueue() {
        console.log("<Queue Start>".concat(this.#holdStack.toString()));
        return;
    }
}

const q = new Queue();
q.enqueue(1);
q.enqueue(2);
q.enqueue(3);
q.printQueue();
q.enqueue(4);
q.printQueue();
q.dequeue();
q.printQueue();