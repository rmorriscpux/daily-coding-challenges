'''
Given a string of parentheses, find the balanced string that can be produced from it using the minimum number of insertions and deletions.
If there are multiple solutions, return any of them.

For example, given "(()", you could return "(())". Given "))()(", you could return "()()()()".
'''

# Balance parentheses by insertion.
def balanceParenthesesIns(parentheses: str):
    open_count = 0

    i = 0
    # Traverse the parentheses string, adding parentheses as needed.
    while i < len(parentheses):
        if parentheses[i] == '(':
            # Increment open_count and move up.
            open_count += 1
            i += 1
        elif parentheses[i] == ')':
            if open_count > 0:
                # Matching open parenthesis exists earlier in the string. Decrement open_count and move up.
                open_count -= 1
                i += 1
            else:
                # Add an open parenthesis when there are none to match the close parenthesis, then move up 2 characters.
                parentheses = parentheses[:i] + '(' + parentheses[i:]
                i += 2

    # Close any remaining open parentheses at the end.
    parentheses += ')' * open_count

    return parentheses

# Balance parentheses by deletion.
def balanceParenthesesDel(parentheses: str):
    # End case: empty string.
    if not parentheses:
        return ""

    # Ignore all closing parentheses at the beginning of the string.
    start = 0
    while parentheses[start] == ')':
        start += 1
        if start == len(parentheses):
            return ""

    parentheses = parentheses[start:]
    open_count = 0

    # Traverse until wthere are balanced parentheses.
    for i, p in enumerate(parentheses):
        if p == '(':
            open_count += 1
        elif p == ')':
            open_count -= 1

        if open_count == 0:
            break

    # When there are balanced parentheses, recur into the tail afterward. Otherwise, there are leading open parentheses equal to open_count to be truncated.
    return parentheses[open_count:] if open_count > 0 else parentheses[:i+1] + balanceParenthesesDel(parentheses[i+1:])

# Wrapper function to combine solutions in a dictionary.
balanceParentheses = lambda parentheses: {
    "Input" : parentheses,
    "Insertion" : balanceParenthesesIns(parentheses),
    "Deletion" : balanceParenthesesDel(parentheses)
}

print(balanceParentheses("(()"))
print(balanceParentheses("))()("))
print(balanceParentheses("(()))("))
