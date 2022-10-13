/*
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
*/

const CHARMAP = "_abcdefghijklmnopqrstuvwxyz";

function waysToDecode(message) {
    function rWaysToDecode(remainingMessage, decodeWords, currentWord) {
        // End case: remainingMessage used up.
        if (remainingMessage.length == 0){
            decodeWords.push(currentWord);
            return;
        }

        let index = remainingMessage.charAt(0);

        // Case where first character is 0: Invalid setup.
        if (index == '0'){
            return;
        }

        // Recursion Part
        rWaysToDecode(remainingMessage.slice(1), decodeWords, currentWord + CHARMAP.charAt(index));

        if (remainingMessage.length >= 2){
            if (index == '1' || (index == '2' && Number(remainingMessage.charAt(1)) <= 6)) {
                index += remainingMessage.charAt(1);
                rWaysToDecode(remainingMessage.slice(2), decodeWords, currentWord + CHARMAP.charAt(index));
            }
        }

        return decodeWords;
    }

    const allWords = rWaysToDecode(String(message), [], "");
    return allWords.length;
}

console.log(waysToDecode(1111));
console.log(waysToDecode(1126));
console.log(waysToDecode(2127));
console.log(waysToDecode(16541324));