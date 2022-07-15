'''
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb"
'''

def distinct_chars(k, str):
    if k > len(str):
        return len(str)
    if k < 1:
        return None

    max_length = 0
    all_chars = set(())
    for i in range(0, len(str)-k):
        all_chars.clear()
        for j in range(i, len(str)):
            all_chars.add(str[j])
            if len(all_chars) > k:
                if (j-i) > max_length:
                    max_length = j-i
                break
            # Check at the end of the string.
            if j == len(str) - 1:
                if (j-i+1) > max_length:
                    max_length = j-i+1
        
    return max_length

print(distinct_chars(2, 'abcba'))
