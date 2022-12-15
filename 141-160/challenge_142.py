'''
You're given a string consisting solely of (, ), and *. * can represent either a (, ), or an empty string.
Determine whether the parentheses are balanced.

For example, (()* and (*) are balanced. )*( is not balanced.
'''

def balancedParentheses(parentheses_str: str) -> bool:
    def rBalancedParentheses(remaining_str, open_num):
        # End case. Parentheses are balanced if all open parentheses have matching closing parentheses.
        if len(remaining_str) == 0:
            return open_num == 0

        # Closing parentheses
        if remaining_str[0] == ')':
            # No matching opening parentheses: Return False
            if open_num == 0:
                return False
            # Else, recur, subtract 1 from open_num.
            else:
                return rBalancedParentheses(remaining_str[1:], open_num-1)

        # Opening parentheses: Recur, add 1 to open_num.
        elif remaining_str[0] == '(':
            return rBalancedParentheses(remaining_str[1:], open_num+1)

        # Wild card case. OR over recursion of every case: '(', blank, or ')'.
        elif remaining_str[0] == '*':
            wild_card = rBalancedParentheses(remaining_str[1:], open_num+1) or rBalancedParentheses(remaining_str[1:], open_num)
            if open_num > 0:
                wild_card = wild_card or rBalancedParentheses(remaining_str[1:], open_num-1)
            return wild_card

        # Ignore invalid characters; recur without modifying open_num.
        else:
            return rBalancedParentheses(remaining_str[1:], open_num)

        # Shouldn't get here.
        return False

    return rBalancedParentheses(parentheses_str, 0)

print(balancedParentheses("(()*"))
print(balancedParentheses("(*)"))
print(balancedParentheses(")*("))