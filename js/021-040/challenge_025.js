/*
This problem was asked by Facebook.

Implement regular expression matching with the following special characters:

    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true.
The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true.
The same regular expression on the string "chats" should return false.
*/

function myRegex(inputStr, pattern) {
    // Recursive matching function.
    function rMyRegex(inputStr, pattern) {
        // Pattern is empty.
        if (pattern == ""){
            return inputStr == "";
        }

        // Check that the first character in input_str matches itself or the wild '.' character in pattern.
        let match = inputStr != "";
        if (match) {
            match = [inputStr.charAt(0), '.'].includes(pattern.charAt(0));
        }

        // Now check for asterisk matching. Asterisk indicates that the previous character can occur 0 or more times.
        // We'll need separate recursions for when the character is not in the start of input_str or when it occurs at least once. Either case matches.
        if (pattern.length == 2 && pattern.charAt(1) == '*') {
            return rMyRegex(inputStr, pattern.slice(2)) || (match && rMyRegex(inputStr.slice(1), pattern));
        }
        else { // Next character is not '*'
            return match && rMyRegex(inputStr.slice(1), pattern.slice(1));
        }
    }

    // Remove leading '*' characters since they are effectively null, along with duplicate, adjacent '*' since they're redundant.
    let start = 0;
    while (pattern.charAt(start) == '*') {
        start++;
    }
    pattern = pattern.slice(start);
    while (pattern.includes("**")) {
        pattern = pattern.replace("**", "*");
    }

    return rMyRegex(inputStr, pattern);
}