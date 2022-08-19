'''
The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions
required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three:
substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
'''

def editDistance(str1, str2):
    # Make a 2D list with the dimensions being the length of the strings + 1. Populate with 0
    distance_matrix = [[0 for j in range(0, len(str2)+1)] for i in range(0, len(str1)+1)]
    # Set base distances for cases where one string is blank.
    for i in range(0, len(str1)+1):
        distance_matrix[i][0] = i
    for j in range(0, len(str2)+1):
        distance_matrix[0][j] = j
    # Fill in the rest, up to the limits to determine the minimum distance between two substrings.
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            # diff_substr represents needing to make a modification between the strings.
            diff_substr = 1 if str1[i-1] != str2[j-1] else 0
            distance_matrix[i][j] = min(distance_matrix[i-1][j-1] + diff_substr, distance_matrix[i][j-1] + 1, distance_matrix[i-1][j] + 1)

    # for row in distance_matrix:
    #     print(row)

    return distance_matrix[len(str1)][len(str2)]


print(editDistance("kitten", "sitting"))
print(editDistance("kitten", "written"))