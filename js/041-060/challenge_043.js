/*
Implement a stack that has the following methods:

    push(val), which pushes an element onto the stack
    pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
    max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.
*/

class Stack {
    #maxStack = [];
    constructor() {
        this.stack = [];
    }

    // When a value is pushed, check if it's greater than the value at the position where the current max is.
    push(value) {
        this.stack.push(value);
        if (this.#maxStack.length == 0 || value > this.stack[this.#maxStack[this.#maxStack.length-1]]) {
            this.#maxStack.push(this.stack.length-1);
        }
    }

    // When a value is popped, check if the index popped was the last value in max_stack. If so, remove that as well.
    pop() {
        if (this.stack.length == 0) {
            return null;
        }

        if (this.#maxStack[this.#maxStack.length-1] == this.stack.length-1){
            this.#maxStack.pop();
        }

        return this.stack.pop();
    }

    max() {
        if (this.stack.length == 0) {
            return null;
        }

        return this.stack[this.#maxStack[this.#maxStack.length-1]];
    }
}