'''
Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string.
For example, given the string “abracadabra” and the pattern “abr”, you should return [0, 7].
'''

def findPatternIndices(s: str, pattern: str):
    s_len, p_len = len(s), len(pattern)
    indices = []

    for i in range(0, s_len - p_len + 1):
        if pattern == s[i:i+p_len]:
            indices.append(i)

    return indices

print(findPatternIndices("abracadabra", "abr"))