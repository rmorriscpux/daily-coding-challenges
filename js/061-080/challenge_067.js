/*
Implement an LFU (Least Frequently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

    set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item,
    then it should also remove the least frequently used item. If there is a tie, then the least recently used key should be removed.

    get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.
*/

class LFUNode {
    constructor(key, value) {
        this.key = key
        this.value = value;
        this.timesUsed = 0;
        this.next = null;
        this.prev = null;
    }
}

class LFUCache {
    #maxCacheSize;

    constructor(n) {
        if (n <= 0) throw RangeError("n must be positive.");

        this.#maxCacheSize = n;
        this.head = null;
        this.cache = {};
    }

    #sort(node) {
        while (true) {
            if (!node.next) {
                return;
            }

            const after = node.next;
            const before = node.prev;

            if (after.timesUsed > node.timesUsed) {
                return;
            }
            node.next = after.next;
            node.prev = after;
            if (node.next != null) {
                node.next.prev = node;
            }
            after.next = node;
            after.prev = before;
            if (before != null) {
                before.next = after;
            }
            else {
                this.head = after;
            }
        }
    }

    set(key, value) {
        if (Object.keys(this.cache).includes(key)) {
            this.cache[key].value = value;
            this.cache[key].timesUsed++;
            this.#sort(this.cache[key])
        }
        else {
            if (Object.keys(this.cache).length == this.#maxCacheSize) {
                let popNode = this.head;
                this.head = this.head.next;
                if (this.head != null) {
                    this.head.prev = null;
                }
                delete this.cache[popNode.key];
            }
            const newNode = new LFUNode(key, value);
            this.cache[key] = newNode;
            if (this.head != null) {
                newNode.next = this.head;
                this.head.prev = newNode;
            }
            this.head = newNode;
            this.#sort(this.head);
        }
        return;
    }

    get(key) {
        if (!Object.keys(this.cache).includes(key)){
            return null;
        }
        this.cache[key].timesUsed++;
        this.#sort(this.cache[key]);
        return this.cache[key].value;
    }
}

const cache = new LFUCache(3);

cache.set('one', 1);
cache.set('two', 2);
cache.set('three', 3);
cache.get('one');
cache.set('four', 4);
let cPtr = cache.head;
while (cPtr != null) {
    console.log(cPtr.value);
    cPtr = cPtr.next;
}
// console.log(cache.cache);