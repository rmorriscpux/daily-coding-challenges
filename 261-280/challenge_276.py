'''
Implement an efficient string matching algorithm.

That is, given a string of length N and a pattern of length k,
write a program that searches for the pattern in the string with less than O(N * k) worst-case time complexity.

If the pattern is found, return the start index of its location. If not, return False.
'''

# This is the Knuth-Morris-Pratt (KMP) search algorithm, which does preprocessing on the pattrn to optimize pattern-in-text searches.
# Worst case time complexity is O(N).

def kmpMatch(text: str, pattern: str):
    k = len(pattern)
    N = len(text)

    if k > N:
        return False
    # Initialize longest prefix size (LPS) list.
    lps = [0] * k
    prev_lps = 0
    # Step 1: Compute LPS list
    i = 1
    while i < k:
        if pattern[i] == pattern[prev_lps]:
            prev_lps += 1
            lps[i] = prev_lps
            i += 1
        elif prev_lps != 0:
            prev_lps = lps[prev_lps-1]
        else:
            lps[i] = 0
            i += 1

    # Step 2: Find pattern in txt.
    i, j = 0, 0
    while (N-i) >= (k-j):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        if j == k:
            return i-j
        elif (i < N) and (text[i] != pattern[j]):
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

    # Pattern not found if loop completes.
    return False