'''
Given a string, return whether it represents a number. Here are the different kinds of numbers:

    "10", a positive integer
    "-10", a negative integer
    "10.1", a positive real number
    "-10.1", a negative real number
    "1e5", a number in scientific notation

And here are examples of non-numbers:

    "a"
    "x 1"
    "a -2"
    "-"
'''

import re

def isNumber(num_str: str):
    zero_pattern = re.match("0", num_str)
    int_pattern = re.match("-?[1-9][0-9]*", num_str)
    decimal_lt1_pattern = re.match("-?0[.][0-9]+", num_str)
    decimal_pattern = re.match("-?[1-9][0-9]*[.][0-9]+", num_str)
    sci_pattern = re.match("-?[1-9]e-?[0-9]+", num_str)
    sci_deci_pattern = re.match("-?[0-9][.][0-9]+e-?[0-9]+", num_str)

    return bool(zero_pattern or
        int_pattern or
        decimal_lt1_pattern or
        decimal_pattern or
        sci_pattern or
        sci_deci_pattern)

print(isNumber("10"))
print(isNumber("-10"))
print(isNumber("10.1"))
print(isNumber("-10.1"))
print(isNumber("1e5"))
print(isNumber("a"))
print(isNumber("x 1"))
print(isNumber("a -2"))
print(isNumber("-"))