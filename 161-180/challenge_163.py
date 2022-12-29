'''
Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.

The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.

For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

You can assume the given expression is always valid.
'''

def evalReversePolishNotation(num_op_list: list):
    number_stack = []

    for k in num_op_list:
        if isinstance(k, int) or isinstance(k, float):
            # When k is a number, add it to the stack.
            number_stack.append(k)
        else:
            # When k is an operand, remove the top two numbers from the stack and operate on them, then place the result back on the stack.
            num1 = number_stack.pop()
            num2 = number_stack.pop()
            if k == '+':
                num_result = num1 + num2
            elif k == '-':
                num_result = num1 - num2
            elif k == '*':
                num_result = num1 * num2
            elif k == '/':
                num_result = num1 / num2
            else:
                raise ValueError("Not a valid arithmetic expression.")
            number_stack.append(num_result)

    # At the end, there should be only a single number in the stack.
    return number_stack[0]

print(evalReversePolishNotation([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']))