'''
Given a set of characters C and an integer k, a De Bruijn sequence is a cyclic sequence in which every possible k-length string of characters in C occurs exactly once.

For example, suppose C = {0, 1} and k = 3. Then our sequence should contain the substrings {'000', '001', '010', '011', '100', '101', '110', '111'},
and one possible solution would be 00010111.

Create an algorithm that finds a De Bruijn sequence.
'''

from typing import Set

def deBruijn(C: Set[str], k: int):
    # Subroutine to build every substring permutation of length k using characters in C.
    def buildSubStrings(C: Set[str], k: int, built_ss: str="", sub_strings: Set[str]=set()):
        if len(built_ss) == k:
            sub_strings.add(built_ss)
            return
        
        for character in C:
            buildSubStrings(C, k, built_ss+character, sub_strings)

        return
    
    def rDeBruijn(C: Set[str], k: int, db_string: str, used_ss: Set[str], remaining_ss: Set[str]):
        if len(remaining_ss) == k - 1:
            # At this point, the string is long enough.
            # Wrap around the last k-1 characters and the first k-1 characters.
            wrap_string = db_string[-(k-1):] + db_string[:k-1]
            # Check that all length k substrings in wrap_string are in remaining_ss.
            for i in range(0, k-1):
                if wrap_string[i:i+k] not in remaining_ss:
                    return None
            # db_string is valid if loop completes.
            return db_string
        
        for character in C:
            # Make a new substring and verify that it hasn't already been used.
            new_ss = db_string[-(k-1):] + character
            if new_ss in used_ss:
                continue
            # Recur and return built_string if the recursive function returns a valid string.
            built_string = rDeBruijn(C, k, db_string + character, used_ss.union({new_ss}), remaining_ss.difference({new_ss}))
            if built_string:
                return built_string
            
        return None
    # Setup
    if not C: # Empty set.
        return ""
    C = set(map(lambda s: str(s)[0], C))
    assert k > 0
    # Get all substring permutations.
    sub_strings = set()
    buildSubStrings(C, k, "", sub_strings)
    # Select a character to create the starter_string. This can vary, so the result will vary on each call, but any string returned is valid.
    starter_string = list(C)[0] * k
    # Recur to build out the De Bruijn sequence.
    return rDeBruijn(C, k, starter_string, {starter_string}, sub_strings.difference({starter_string}))

print(deBruijn({0, 1}, 3))
print(deBruijn({0, 1, 2, 3}, 3))