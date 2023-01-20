'''
Write a program that computes the length of the longest common subsequence of three given strings.
For example, given "epidemiologist", "refrigeration", and "supercalifragilisticexpialodocious",
it should return 5, since the longest common subsequence is "eieio".
'''

def longestCommonSubseqLen(word1: str, word2: str, word3: str):
    def rlongestCommonSubseqLen(target: str, comp1: str, comp2: str, built_str: str):
        if not (target and comp1 and comp2): # At least one string is empty.
            return {built_str}

        target_letter = target[0]
        substring_set = set()

        # Find the next occurrence of the target letter in comp1 and comp2. If it isn't found, set the index to the length of the comp string.
        for index1, letter1 in enumerate(comp1):
            if letter1 == target_letter:
                break
        else:
            index1 += 1

        for index2, letter2 in enumerate(comp2):
            if letter2 == target_letter:
                break
        else:
            index2 += 1

        if index1 == len(comp1) or index2 == len(comp2):
            # Reached the end of comp1 or comp2, so add the current built_str to the set.
            substring_set.add(built_str)
        else:
            # When target_letter is found, update the set with the recursion using substrings past
            # the first instance of target_letter in each string, and add target_letter to built_str.
            substring_set.update(rlongestCommonSubseqLen(target[1:], comp1[index1+1:], comp2[index2+1:], built_str + target_letter))

        # Update the set with recursion using the target string past the first character.
        substring_set.update(rlongestCommonSubseqLen(target[1:], comp1, comp2, built_str))

        return substring_set

    substrings = rlongestCommonSubseqLen(word1, word2, word3, "")
    substrings.update(rlongestCommonSubseqLen(word2, word3, word1, ""))
    substrings.update(rlongestCommonSubseqLen(word3, word1, word2, ""))

    # Calculate the length of each substring returned in the set and return the max value from that.
    return max(map(lambda s: len(s), substrings))

print(longestCommonSubseqLen("epidemiologist", "refrigeration", "supercalifragilisticexpialodocious"))
print(longestCommonSubseqLen("abc", "def", "ghi"))