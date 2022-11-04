'''
Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is “ab”, and S is “abxaba”, return 0, 3, and 4.
'''

def findAnagramIndices(W: str, S: str):
    if (len(W) > len(S)) or (len(W) == 0):
        return []

    # Build W letter dictionary to compare.
    w_dict = {}
    for letter in W:
        if letter not in w_dict:
            w_dict[letter] = 0
        w_dict[letter] += 1

    anagram_indices = []

    # Go through each index where we can fit the length of W inside of S.
    for index in range(0, len(S)-len(W)+1):
        s_dict = {}
        for letter in S[index:index+len(W)]:
            # Optimization
            if letter not in w_dict:
                break
            # Build S letter dictionary to compare.
            if letter not in s_dict:
                s_dict[letter] = 0
            s_dict[letter] += 1

        # Compare dictionaries and add index if they match.
        if w_dict == s_dict:
            anagram_indices.append(index)

    return anagram_indices

print(findAnagramIndices("ab", "abxaba"))