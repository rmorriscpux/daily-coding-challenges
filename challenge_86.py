'''
Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the string valid
(i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we must remove all of them.
'''

def countRemoveParentheses(parentheses: str):
    unmatched_open = 0
    unmatched_closed = 0

    for p in parentheses:
        if p == "(":
            unmatched_open += 1
        elif p == ")":
            if unmatched_open > 0:
                unmatched_open -= 1
            else:
                unmatched_closed += 1

    return unmatched_open + unmatched_closed

print(countRemoveParentheses("()())()"))
print(countRemoveParentheses(")("))