/*
Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less.
You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words.
If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return:
["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.
*/

function stringIntoLines(wordString, k) {
    function buildLines(wordString, k, lines) {
        // Return if empty.
        if (wordString.length == 0) {
            return;
        }
        // Add the last words and return if wordString.length is less than k.
        if (wordString.length <= k) {
            lines.push(wordString);
            return;
        }

        // Find the point where the last space within k is.
        let endPoint = k;
        while (endPoint > 0 && wordString.charAt(endPoint) != " ") {
            endPoint--;
        }

        if (endPoint == 0) { // Word is larger than k.
            throw RangeError("Single word larger than k value.");
        }

        // Add the line.
        lines.push(wordString.slice(0, endPoint));
        // And recur.
        buildLines(wordString.slice(endPoint+1), k, lines);

        return;
    }

    lines = [];
    buildLines(wordString, k, lines);
    return lines;
}

console.log(stringIntoLines("The quick brown fox jumps over the lazy dog", 10));