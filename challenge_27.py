'''
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
'''

def balancedBrackets(bracket_str):
    bracket_stack = []
    for b in bracket_str:
        # Opening Brackets - Add to stack.
        if b in "({[":
            bracket_stack.append(b)
        # Check each closing bracket. If its match is on top of the stack, pop it. If it's not, the bracket string is not balanced.
        elif b == ')':
            if len(bracket_stack) > 0 and bracket_stack[-1] == '(':
                bracket_stack.pop()
            else:
                return False
        elif b == '}':
            if len(bracket_stack) > 0 and bracket_stack[-1] == '{':
                bracket_stack.pop()
            else:
                return False
        elif b == ']':
            if len(bracket_stack) > 0 and bracket_stack[-1] == '[':
                bracket_stack.pop()
            else:
                return False
    # Loop complete. Return True if bracket_stack is empty.
    return len(bracket_stack) == 0

assert balancedBrackets("([])[]({})")
assert not balancedBrackets("([)]")
assert not balancedBrackets("((()")