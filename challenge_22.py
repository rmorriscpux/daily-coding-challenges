'''
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
'''

# Slow, but working implementation.

def getSentence(str, word_list):
    def rGetSentence(str, word_list, sentence):
        # Terminal condition for recursion.
        if len(str) == 0:
            return sentence

        for i in range(len(str), 0, -1):
            try:
                word = word_list.index(str[:i])
            except ValueError:
                # No match found.
                continue
            else:
                # Match found. Add matching word to the sentence and recur, then break the loop.
                sentence.append(word_list[word])
                rGetSentence(str[len(word_list[word]):], word_list, sentence)
                break
        else:
            # End of loop, no matching words found starting at the beginning of the substring.
            return sentence

        # When there is a valid sentence, the total length of the sentence word list will be the same as the initial string.
        sentence_len = 0
        for each_word in sentence:
            sentence_len += len(each_word)
        if sentence_len == len(str):
            return sentence
        else:
            return None

    return rGetSentence(str, word_list, [])

print(getSentence("thequickbrownfox", ['quick', 'brown', 'the', 'fox']))
print(getSentence("bedbathandbeyond", ['bed', 'bath', 'bedbath', 'and', 'beyond']))