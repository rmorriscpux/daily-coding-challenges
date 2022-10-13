/*
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb"
*/

function distinctChars(k, s) {
    if (k > s.length) {
        return s.length;
    }
    if (k < 1) {
        return 0;
    }

    let maxLength = 0;
    let charSet = "";

    for (let i = 0; i < s.length-k; i++) {
        charSet = "";
        for (let j = i; j < s.length; j++) {
            if (!charSet.includes(s.charAt(j))) {
                charSet += s.charAt(j);
            }
            if (charSet.length > k) {
                if (j-i > maxLength) {
                    maxLength = j-1;
                }
                break;
            }
            // Check at the end of the string.
            if (j == s.length-1 && j-i+1 > maxLength) {
                maxLength = j-i+1;
            }
        }
    }

    return maxLength;
}

console.log(distinctChars(2, "abcba"));