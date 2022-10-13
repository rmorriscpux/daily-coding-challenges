/*
Implement an autocomplete system.
That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string 'de' and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
*/

class TrieNode {
    constructor(character) {
        this.character = character;
        this.word = null;
        this.nextChar = {};
    }
}

class TrieDict extends TrieNode {
    constructor() {
        super(null);
    }

    addWord(word) {
        let nodePtr = this;
        let currentChar = null;
        for (let i = 0; i < word.length; i++) {
            currentChar = word.charAt(i);
            if (!nodePtr.nextChar.keys().contains(currentChar)) {
                nodePtr.nextChar[currentChar] = new TrieNode(currentChar);
            }
            nodePtr = nodePtr.nextChar[currentChar];
        }
        nodePtr.word = word;
        return;
    }

    searchWord(searchString) {
        const foundList = [];
        let nodePtr = this;
        // Step 1: Get to the appropriate trie.
        let currentChar = null;
        for (let i = 0; i < searchString.length; i++) {
            currentChar = searchString.charAt(i);
            if (!nodePtr.nextChar.keys().contains(currentChar)) {
                // No words in dictionary matching searchString.
                return foundList;
            }
            nodePtr = nodePtr.nextChar[currentChar];
        }
        // Step 2: Get all words and return.
        function rSearchWord(node) {
            if (node.word != null) {
                foundList.push(node.word);
            }
            const charList = Object.keys(node.nextChar);
            charList.forEach((c) => {rSearchWord(node.nextChar[c]);});
        }
        return foundList;
    }
}

