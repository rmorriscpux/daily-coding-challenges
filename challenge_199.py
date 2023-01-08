'''
Given a string of parentheses, find the balanced string that can be produced from it using the minimum number of insertions and deletions.
If there are multiple solutions, return any of them.

For example, given "(()", you could return "(())". Given "))()(", you could return "()()()()".
'''

def balanceParenthesesIns(parentheses: str):
    open_count = 0

    i = 0
    while i < len(parentheses):
        if parentheses[i] == '(':
            open_count += 1
            i += 1
        elif parentheses[i] == ')':
            if open_count > 0:
                open_count -= 1
                i += 1
            else:
                parentheses = parentheses[:i] + '(' + parentheses[i:]
                i += 2

    parentheses += ')' * open_count

    return parentheses

def balanceParenthesesDel(parentheses: str):
    def rBalanceParenthesesDel(rem_pars: str):
        if not rem_pars:
            return ""

        open_count = 0

        for i, p in enumerate(rem_pars):
            if p == '(':
                open_count += 1
            elif p == ')':
                open_count -= 1

            if open_count == 0:
                break

        return rem_pars[open_count:] if open_count else rem_pars[:i+1] + rBalanceParenthesesDel(rem_pars[i+1:])

    start, end = 0, len(parentheses)

    while parentheses[start] == ')':
        start += 1
        if start == len(parentheses):
            return ""

    while parentheses[end-1] == '(':
        end -= 1

    return rBalanceParenthesesDel(parentheses[start:end])

balanceParentheses = lambda parentheses: {
    "Input" : parentheses,
    "Insertion" : balanceParenthesesIns(parentheses),
    "Deletion" : balanceParenthesesDel(parentheses)
}

print(balanceParentheses("(()"))
print(balanceParentheses("))()("))

