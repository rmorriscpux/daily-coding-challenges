'''
Find an efficient algorithm to find the smallest distance (measured in number of words) between any two given words in a string.

For example, given words "hello", and "world" and a text content of "dog cat hello cat dog dog hello cat world",
return 1 because there's only one word "cat" in between the two words.
'''

# Time complexity: O(N)
def findSmallestDistance(word_string: str, word1: str, word2: str):
    if word1 == word2:
        return 0
    # Will return None if either target word is not in the string.
    dist = None
    last_word, last_index = None, None
    # Split the word string into a list and loop, tracking the index and word when a target word appears.
    for index, word in enumerate(word_string.split()):
        if word in [word1, word2]:
            if (word == word1 and last_word == word2) or (word == word2 and last_word == word1):
                # Comparison needed to ensure that we get the smallest distance.
                dist = index - last_index - 1 if dist == None or index - last_index -1 < dist else dist
            last_word = word
            last_index = index

    return dist

print(findSmallestDistance("dog cat hello cat world dog dog cat hello", "hello", "world"))