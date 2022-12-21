/*
Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

    set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item,
    then it should also remove the least recently used item.

    get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.
*/

const assert = require("assert");

// Implemented as a dictionary with keys set to nodes in a doubly-linked list to track the last used.
// Hybridizing in this way allows for tracking the order used in O(1) time.

class LRUNode {
    constructor(key, value) {
        // Key is needed in the node class in order to accurately remove nodes.
        this.key = key;
        this.value = value;
        this.next = null;
        this.prev = null;
    }

    toString() {
        return `[${this.key.toString()} : ${this.value.toString()}]`;
    }
}

class LRUCache {
    #cacheSize;
    #cache = {};
    #head = new LRUNode(null, null)
    #tail = new LRUNode(null, null)

    constructor(cacheSize) {
        assert(typeof cacheSize == "number" && cacheSize >= 1);
        this.#cacheSize = Math.floor(cacheSize);
        this.#head.next = this.#tail;
        this.#tail.prev = this.#head;
    }

    // The below two methods are only to be called by the set() and get() methods.
    // Javascript ES6 doesn't support private methods, but ideally these would be set private.
    // The point of having these methods at all is to reduce redundant code.

    _insertNode(newNode) {
        // Get the next node after the head.
        let nextNode = this.#head.next;
        // Set the node after the head.
        newNode.prev = this.#head;
        newNode.next = nextNode;
        // Point back to the new node.
        this.#head.next = newNode;
        nextNode.prev = newNode;
        return;
    }

    _removeNode(lruNode) {
        let nextNode = lruNode.next;
        let prevNode = lruNode.prev;
        nextNode.prev = prevNode;
        prevNode.next = nextNode;
        return;
    }

    // Set a new key/value pair.
    set(key, value) {
        // Case for where key already exists: Remove so we can update.
        if (this.#cache.hasOwnProperty(key)) {
            this._removeNode(this.#cache[key]);
        }
        // Add new node to cache.
        const newNode = new LRUNode(key, value);
        this._insertNode(newNode);
        this.#cache[key] = newNode;
        // Remove the least recently used item if it exceeds the cache size.
        if (Object.keys(this.#cache).length > this.#cacheSize) {
            let lastUsedNode = this.#tail.prev;
            this._removeNode(lastUsedNode);
            delete this.#cache[lastUsedNode.key];
        }
        return;
    }

    // Get a value from a key.
    get(key) {
        // For when key is not in the cache.
        if (!this.#cache.hasOwnProperty(key)) {
            return null;
        }
        // Get the target node.
        const targetNode = this.#cache[key];
        // Move the node to the front of the cache.
        this._removeNode(targetNode);
        this._insertNode(targetNode);

        return targetNode.value;
    }

    // Added function to display cache.
    printCache() {
        console.log("Cache In Order:");
        let orderStr = "";
        let nodePtr = this.#head.next;
        while (nodePtr.next != null) {
            orderStr += nodePtr.toString();
            if (nodePtr.next.next != null) {
                orderStr += "-";
            }
            nodePtr = nodePtr.next;
        }
        console.log(orderStr);
        return;
    }
}

const c = new LRUCache(3);

c.set('one', 1);
c.set('two', 2);
c.set('three', 3);
console.log("Added 1, 2, 3");
console.log('----------');
c.printCache();
console.log('----------');
console.log(`Retrieved ${c.get('one')}`);
console.log('----------');
c.printCache();
console.log('----------');
c.set('four', 4);
console.log('Added 4');
console.log('----------');
c.printCache();
