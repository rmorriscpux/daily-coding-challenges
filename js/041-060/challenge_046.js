/*
Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".
*/

function longestPalindrome(s) {
    // Terminator condition.
    if (s.length <= 1) {
        return "";
    }

    // Get pointer positions for left and right.
    let lPtr = Math.floor(s.length / 2 - 1);
    let rPtr = s.length - 1 - lPtr;

    // Determine if we have a palindrome.
    let isPalindrome = true;

    while (lPtr >= 0) {
        if (s.charAt(lPtr) != s.charAt(rPtr)) {
            isPalindrome = false;
            break;
        }
        lPtr--;
        rPtr++;
    }

    // Palindrome found.
    if (isPalindrome) {
        return s;
    }

    // Determine longest palindrome if we haven't found it yet.
    let leftSubS = longestPalindrome(s.slice(0, -1));
    let rightSubS = longestPalindrome(s.slice(1));

    return leftSubS.length >= rightSubS.length ? leftSubS : rightSubS;
}

console.log(longestPalindrome("aabcdcb"));
console.log(longestPalindrome("bananas"));
console.log(longestPalindrome('abcdefg'));