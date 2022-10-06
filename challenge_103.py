'''
Given a string and a set of characters, return the shortest substring containing all the characters in the set.

For example, given the string “figehaeci” and the set of characters {a, e, i}, you should return “aeci”.

If there is no substring containing all the characters in the set, return null.
'''

from typing import Set

def shortestSubStrOfChars(charset: Set[str], search_string: str):
    string_list = []
    for i, character in enumerate(search_string):
        if character in charset:
            string_list.append([i, 0, set(), False])
            for s in string_list:
                s[2].add(character)

        for s in string_list:
            if s[3] == False:
                s[1] += 1
            if len(s[2]) == len(charset):
                s[3] = True
    
    min_string = None
    min_string_len = float("inf")
    for s in string_list:
        if (s[3] == True and s[1] < min_string_len):
            min_string = search_string[s[0]:s[0]+s[1]]
            min_string_len = s[1]

    return min_string

print(shortestSubStrOfChars({'a', 'e', 'i'}, "figehaeci"))