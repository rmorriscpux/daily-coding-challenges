/*
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
*/

function buildSentence(wordSet, wordString) {
    function rBuildSentence(wordSet, wordString, sentence) {
        // Termination condition.
        if (wordString.length == 0) {
            return sentence;
        }

        for (let i = wordString.length; i > 0; i--) {
            let wordCandidate = wordString.slice(0, i);
            if (wordSet.includes(wordCandidate)) {
                sentence.push(wordCandidate);
                checkRest = rBuildSentence(wordSet, wordString.slice(i), sentence);
                if (checkRest != null) {
                    return checkRest;
                } else {
                    sentence.pop();
                }
            }
        }

        return null;
    }

    return rBuildSentence(wordSet, wordString, []);
}

console.log(buildSentence(['quick', 'brown', 'the', 'fox'], 'thequickbrownfox'));
console.log(buildSentence(['bed', 'bath', 'bedbath', 'and', 'beyond'], 'bedbathandbeyond'));
console.log(buildSentence(['quick', 'brown', 'the', 'fox'], 'thequickbluefox'));