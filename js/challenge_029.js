/*
Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character.
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding.
You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.
*/

function runLengthEncode(inStr) {
    if (inStr.length == 0) {
        return "";
    }

    let encodedStr = "";
    let charCount = 1;
    let currentChar = inStr.charAt(0);
    for (let i = 1; i < inStr.length; i++) {
        if (inStr.charAt(i) == currentChar) {
            charCount++;
        }
        else {
            encodedStr = encodedStr.concat(charCount.toString(), currentChar);
            charCount = 1;
            currentChar = inStr.charAt(i);
        }
    }

    return encodedStr.concat(charCount.toString(), currentChar);
}

function runLengthDecode(inStr) {
    if (inStr.length == 0) {
        return "";
    }

    let decodedStr = "";
    for (let i = 0; i < inStr.length; i+=2) {
        decodedStr = decodedStr.concat(inStr[i+1].repeat(Number(inStr[i])));
    }

    return decodedStr;
}

a = "AAAABBBCCDAA";
b = runLengthEncode(a);
c = runLengthDecode(b);
console.log(a);
console.log(b);
console.log(c);