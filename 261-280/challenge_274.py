'''
Given a string consisting of parentheses, single digits, and positive and negative signs, convert the string into a mathematical expression to obtain the answer.

Don't use eval or a similar built-in parser.

For example, given '-1 + (2 + 3)', you should return 4.
'''

def evalExpression(expression: str):
    DIGITS = "0123456789"

    def balancedParentheses(expression: str):
        open_p = 0
        for c in expression:
            if c == '(':
                open_p += 1
            elif c == ')':
                if open_p == 0:
                    return False
                open_p -= 1
        return open_p == 0
    
    def rEvalExpression(exp_str: str):
        if exp_str == "":
            return 0
        if exp_str.isnumeric() or (exp_str[0] == '-' and exp_str[1:].isnumeric()):
            return int(exp_str)
        p_open = exp_str.find('(')
        while p_open != -1:
            p_close = -1
            p_count = 1
            for i in range(p_open+1, len(exp_str)):
                if exp_str[i] == ')':
                    p_count -= 1
                elif exp_str[i] == '(':
                    p_count += 1

                if p_count == 0:
                    p_close = i
                    break

            sub_total = rEvalExpression(exp_str[p_open+1:p_close])
            sub_str = exp_str[p_open:p_close+1]
            exp_str = exp_str.replace(sub_str, str(sub_total), 1)
            
            p_open = exp_str.find('(')

        first_num_str = exp_str[0]
        i = 1
        while i < len(exp_str) and exp_str[i] in DIGITS:
            first_num_str += exp_str[i]
            i += 1

        total = int(first_num_str)

        while i < len(exp_str):
            subtract = exp_str[i] == '-'
            start = i+1
            end = start
            while end < len(exp_str) and exp_str[end] in DIGITS:
                end += 1
            i = end
            if start == end:
                continue
            if subtract:
                total -= int(exp_str[start:end])
            else:
                total += int(exp_str[start:end])

        return total

    assert balancedParentheses(expression)

    return rEvalExpression(expression.replace(' ', ''))

print(evalExpression('-1 + (2 + 3)'))