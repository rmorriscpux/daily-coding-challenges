'''
Create a basic sentence checker that takes in a stream of characters and determines whether they form valid sentences.
If a sentence is valid, the program should print it out.

We can consider a sentence valid if it conforms to the following rules:

The sentence must start with a capital letter, followed by a lowercase letter or a space.
All other characters must be lowercase letters, separators (,,;,:) or terminal marks (.,?,!,‽).
There must be a single space between each word.
The sentence must end with a terminal mark immediately following a word.
'''

import re

def sentenceChecker(char_stream: str):
    # Construct regex patterns.
    FIRST_WORD = re.compile('[A-Z][a-z]*')
    ADDL_WORD = re.compile('[a-z]+')
    SPACE = re.compile('\s')
    SEPARATORS = re.compile('[,;:]')
    TERMINALS = re.compile('[.?!‽]')

    start_word = FIRST_WORD.search(char_stream)
    word = start_word
    while start_word:
        end = word.span()[1]
        # End of string with no terminator. Ends loop without index errors.
        if end == len(char_stream):
            break
        # Reached a terminal character immediately after a word. Print the sentence, then go to the next valid first word if it exists and continue loop.
        if TERMINALS.match(char_stream, end):
            print(char_stream[start_word.span()[0]:end+1])
            start_word = FIRST_WORD.search(char_stream, end+1)
            word = start_word
            continue
        # Reached a separator character immediately after a word. Increment the end index. Can only have a single separator character.
        if SEPARATORS.match(char_stream, end):
            end += 1
        # Reached a space immediately after a word or separator. Increment the end index and check that the following character starts a new word. If so, continue loop.
        if SPACE.match(char_stream, end):
            end += 1
            word = ADDL_WORD.match(char_stream, end)
            if word:
                continue
        # Valid sentence not found from the start of the first word. Go to the next valid first word if it exists.
        start_word = FIRST_WORD.search(char_stream, end)
        word = start_word

    return

char_stream = "ibfaThe quick brown fox jumped swiftly over the lazy dog. So then, how do you do?onlnj---Okay!...."
sentenceChecker(char_stream)