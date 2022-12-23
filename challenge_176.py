'''
Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
'''

def cryptogram(s1: str, s2: str):
    # Strings must be the same length.
    if len(s1) != len(s2):
        return False
    
    char_map = {}
    for i in range(0, len(s1)):
        if s1[i] not in char_map:
            # Character in s2 already mapped to a character in s1.
            if s2[i] in char_map.values():
                return False
            # s1[i] and s2[i] are not in char_map, so map them together.
            char_map[s1[i]] = s2[i]
        # Check if s1[i] is mapped to a different s2 character.
        elif char_map[s1[i]] != s2[i]:
            return False
    # All done, 1-to-1 mapping confirmed.
    return True

print(cryptogram("abc", "bcd"))
print(cryptogram("foo", "bar"))
print(cryptogram("bar", "foo"))