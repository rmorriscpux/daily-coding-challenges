/*
Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word.
If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome).
There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
*/

function makePalindrome(word) {
    // Word has only 0 or 1 characters.
    if (word.length <= 1) {
        return word;
    }
    // Check edges.
    if (word.charAt(0) == word.charAt(word.length-1)) {
        // Edges are the same. Keep the same edges and go in.
        return "".concat(word.charAt(0), makePalindrome(word.slice(1, word.length-1)), word.charAt(word.length-1));
    }
    else {
        // Edges are different.
        let newWord1 = "".concat(word.charAt(0), makePalindrome(word.slice(1, word.length)), word.charAt(0));
        let newWord2 = "".concat(word.charAt(word.length-1), makePalindrome(word.slice(0, word.length-1)), word.charAt(word.length-1));

        // Now return the shortest. If they're the same length, return the first alphabetically.
        if (newWord1.length < newWord2.length) {
            return newWord1;
        }
        else if (newWord2.length < newWord1.length) {
            return newWord2;
        }
        else {
            return newWord1 < newWord2 ? newWord1 : newWord2;
        }
    }
}

console.log(makePalindrome("race"));
console.log(makePalindrome("google"));