/*
The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions
required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three:
substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
*/

function editDistance(word1, word2) {
    // Make a 2D array with the dimensions being the lengths of the strings plus 1, populated with 0's.
    const distanceMatrix = [[]];
    for (let i = 0; i < word2.length + 1; i++) {
        distanceMatrix[0].push(0);
    }
    for (let i = 1; i < word1.length + 1; i++) {
        // Spread to copy values instead of by reference.
        distanceMatrix.push([...distanceMatrix[0]]);
    }
    // Set base distances for cases where one string is blank.
    for (let i = 0; i < word1.length + 1; i++) {
        distanceMatrix[i][0] = i;
    }
    for (let i = 0; i < word2.length + 1; i++) {
        distanceMatrix[0][i] = i;
    }
    // Fill in the rest, up to the limits to determine the minimum distance between two substrings.
    for (let i = 1; i < word1.length + 1; i++) {
        for (let j = 1; j < word2.length + 1; j++) {
            // diffSubstr represents needing to make a modification between the strings.
            let diffSubstr = word1.charAt(i-1) == word2.charAt(j-1) ? 0 : 1;
            distanceMatrix[i][j] = Math.min(distanceMatrix[i-1][j-1] + diffSubstr, distanceMatrix[i][j-1] + 1, distanceMatrix[i-1][j] + 1);
        }
    }

    return distanceMatrix[word1.length][word2.length];
}

console.log(editDistance("kitten", "sitting"));
console.log(editDistance("kitten", "written"));