'''
In academia, the h-index is a metric used to calculate the impact of a researcher's papers. It is calculated as follows:

A researcher has index h if at least h of her N papers have h citations each. If there are multiple h satisfying this formula, the maximum is chosen.

For example, suppose N = 5, and the respective citations of each paper are [4, 3, 0, 1, 5].
Then the h-index would be 3, since the researcher has 3 papers with at least 3 citations.

Given a list of paper citations of a researcher, calculate their h-index.
'''

# Better example via https://en.wikipedia.org/wiki/H-index
# "If an author has five publications, with 9, 7, 6, 2, and 1 citations (ordered from greatest to least), 
# then the author's h-index is 3, because the author has three publications with 3 or more citations. 
# However, the author does not have four publications with 4 or more citations."

from typing import List

def calcHIndex(citations_per: List[int]) -> int:
    for i, count in enumerate(sorted(citations_per, reverse=True)):
        if i >= count:
            return i

    return len(citations_per)

print(calcHIndex([4, 5, 0, 1, 3]))
print(calcHIndex([9, 7, 6, 2, 1]))