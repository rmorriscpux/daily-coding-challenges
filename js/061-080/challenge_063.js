/*
Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

and the target word 'FOAM', you should return true, since it's the leftmost column.
Similarly, given the target word 'MASS', you should return true, since it's the last row.
*/

// Leaving out logic for case insensitivity, but a line like "let upperWord = word.toUpperCase()" can be added at the start.

const assert = require('assert');

function hasWord(matrix, word) {
    for (let i = 1; i < matrix.length; i++) {
        assert(matrix[i].length == matrix[0].length);
    }

    // Check if word is too long to fit in matrix.
    if (word.length > matrix.length && word.length > matrix[0].length) {
        return false;
    }

    let maximumX = matrix[0].length - word.length;
    let maximumY = matrix.length - word.length;
    let letterCount = 0;

    for (let y = 0; y < matrix.length; y++) {
        for (let x = 0; x < matrix[0].length; x++) {
            if (matrix[y][x] == word.charAt(0)) {
                // Check Left-to-Right
                if (x <= maximumX) {
                    letterCount = 1;
                    for (let i = 1; i < word.length; i++) {
                        if (matrix[y][x+i] == word.charAt(i)) {
                            letterCount++;
                        }
                        else {
                            break;
                        }
                    }
                    if (letterCount == word.length) {
                        return true;
                    }
                }
                // Check Up-to-Down
                if (y <= maximumY) {
                    letterCount = 1;
                    for (let i = 1; i < word.length; i++) {
                        if (matrix[y+i][x] == word.charAt(i)) {
                            letterCount++;
                        }
                        else {
                            break;
                        }
                    }
                    if (letterCount == word.length) {
                        return true;
                    }
                }
            }
        }
    }
    return false;
}

const matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']
];

console.log(hasWord(matrix, "FOAM"));
console.log(hasWord(matrix, "MASS"));