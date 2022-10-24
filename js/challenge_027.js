/*
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
*/

function balancedBrackets(bracketStr) {
    const openBrackets = [];
    const bracketMatch = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    };
    for (let i = 0; i < bracketStr.length; i++) {
        switch(bracketStr.charAt(i)) {
        // Add opening brackets to the openBrackets stack.
            case '(':
            case '[':
            case '{':
                openBrackets.push(bracketStr.charAt(i));
                break;
        // For closing brackets, determine if the matching opening bracket is at the top of the stack.
            case ')':
            case ']':
            case '}':
                if (openBrackets.length == 0 || openBrackets[openBrackets.length-1] != bracketMatch[bracketStr.charAt(i)]){
                    return false
                } else {
                    openBrackets.pop();
                }
                break;
            default:
        // Do nothing for non-bracket characters.
        }
    }
    // Balanced if all open brackets are gone from the stack.
    return openBrackets.length == 0;
}

console.log(balancedBrackets("([])[]({})"));
console.log(balancedBrackets("([)]"));
console.log(balancedBrackets("((()"));