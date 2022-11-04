'''
Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
'''

def shiftedStrings(A: str, B: str):
    if len(A) != len(B):
        return False

    return A in (B*2)

print(shiftedStrings('abcde', 'cdeab'))
print(shiftedStrings('abc', 'acb'))
print(shiftedStrings('abcde', 'abcde'))