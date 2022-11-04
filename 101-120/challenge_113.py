'''
Given a string of words delimited by spaces, reverse the words in string. For example, given “hello world here”, return “here world hello”

Follow-up: given a mutable string representation, can you perform this operation in-place?
'''

def reverseWords(word_string: str):
    word_list = word_string.split()
    word_list.reverse()
    return " ".join(word_list)

print(reverseWords("Alpha Beta Gamma Delta"))