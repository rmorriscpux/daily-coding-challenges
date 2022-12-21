/*
Implement a file syncing algorithm for two computers over a low-bandwidth network. What if we know the files in the two computers are mostly the same?
*/

const { createHash } = require('crypto');

class Node {
    constructor() {
        this.parent = null;
        this.digest = null;
        // Change the string here if you wish to use a different hash algorithm.
        this.hashAlgo = "sha256";
    }

    isEqual(otherNode) {
        return this.digest == otherNode.digest;
    }

    addToDirectory(directory) {
        this.parent = directory;
        directory.addChild(this);
        return;
    }

    calculateDigest() {
    }
}

class Directory extends Node {
    #isDirectory = true;
    constructor() {
        super();
        this.children = new Set();
        this.calculateDigest();
    }

    calculateDigest() {
        let newHash = createHash(this.hashAlgo);
        this.children.forEach(child => {
            newHash.update(child.digest);
        });
        let newDigest = newHash.digest('hex');
        if (this.digest != newDigest) {
            this.digest = newDigest;
            if (this.parent != null) {
                this.parent.calculateDigest();
            }
        }
        return;
    }

    addChild(child) {
        this.children.add(child);
        this.calculateDigest();
        return;
    }

    sync(otherDir) {
        if (this.isEqual(otherDir)) {
            return;
        }
        for (child of this.children) {
            if (!otherDir.children.has(child)) {
                otherDir.children.add(child)
            }
        }
        for (child of otherDir.children) {
            if (!this.children.has(child)) {
                this.children.add(child)
            }
        }
        return;
    }
}

class File extends Node {
    #isDirectory = false;
    constructor(data) {
        super();
        this.#data = data;
        this.calculateDigest();
    }

    calculateDigest() {
        let newDigest = createHash(this.hashAlgo).update(this.#data).digest('hex');
        if (newDigest != this.digest) {
            this.digest = newDigest;
            if (this.parent != null) {
                this.parent.calculateDigest();
            }
        }
    }

    set data(d) {
        this.#data = d;
        this.calculateDigest();
        return;
    }

    get data() {
        return this.#data;
    }
}

class Computer {
    constructor() {
        this.root = new Directory();
    }

    sync(otherCP) {
        this.root.sync(otherCP.root)
    }
}