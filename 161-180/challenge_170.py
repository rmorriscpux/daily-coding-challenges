'''
Given a start word, an end word, and a dictionary of valid words, find the shortest transformation sequence from start to end
such that only one letter is changed at each step of the sequence, and each transformed word exists in the dictionary.
If there is no possible transformation, return null. Each word in the dictionary have the same length as start and end and is lowercase.

For example, given start = "dog", end = "cat", and dictionary = {"dot", "dop", "dat", "cat"}, return ["dog", "dot", "dat", "cat"].

Given start = "dog", end = "cat", and dictionary = {"dot", "tod", "dat", "dar"}, return null as there is no possible transformation from dog to cat.
'''

from typing import Set

def shortestSequence(start: str, end: str, word_dict: Set[str]):
    def rShortestSequence(start, end, word_dict, transformation_list):
        list_length = float('inf')
        final_list = None

        for word in word_dict:
            letter_diff_count = 0

            for i in range(0, len(word)):
                if start[i] != word[i]:
                    letter_diff_count += 1

            if letter_diff_count == 1:
                if word == end:
                    return transformation_list + [word]
                word_dict.remove(word)
                new_list = rShortestSequence(word, end, word_dict, transformation_list + [word])
                if new_list != None and new_list[-1] == end:
                    if not final_list or len(new_list) < list_length:
                        final_list = new_list
                        list_length = len(new_list)
                word_dict.add(word)

        return final_list

    return rShortestSequence(start, end, word_dict, [start])

print(shortestSequence("dog", "cat", {"dot", "dop", "dat", "cat"}))
print(shortestSequence("dog", "cat", {"dot", "tod", "dat", "dar"}))