'''
Given a string with repeated characters, rearrange the string so that no two adjacent characters are the same.
If this is not possible, return None.

For example, given “aaabbc”, you could return “ababac”. Given “aaab”, return None.
'''

from math import ceil

def rearrangeString(input_str: str):
    letter_list = list(input_str)
    
    prev_letter = None
    count = 0
    for letter in sorted(letter_list):
        if letter != prev_letter:
            if count > ceil(len(letter_list) / 2):
                return None
            count = 1
            prev_letter = letter
        else:
            count += 1

    i = 1
    while i < len(letter_list) - 1:
        if letter_list[i] in [letter_list[i-1], letter_list[i+1]]:
            move_letter = letter_list.pop(i)
            for j in range(len(letter_list), i-1, -1):
                if move_letter != letter_list[j-1] and (j == len(letter_list) or move_letter != letter_list[j]):
                    letter_list.insert(j, move_letter)
                    break
            else:
                return None
        else:
            i += 1

    return "".join(letter_list)

print(rearrangeString("aaabbc"))
print(rearrangeString("aaab"))