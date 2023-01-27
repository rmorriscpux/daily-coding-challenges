'''
Given a number in Roman numeral format, convert it to decimal.

The values of Roman numerals are as follows:

{
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

In addition, note that the Roman numeral system uses subtractive notation for numbers such as IV and XL.

For the input XIV, for instance, you should return 14.
'''

def romanNumeralValue(roman_str: str):
    # Function assumes that the Roman numeral string is properly formatted.
    VALUES_DICT = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    total_value = 0

    i = 0
    while i < len(roman_str):
        if i < len(roman_str) - 1 and ((roman_str[i] == 'C' and roman_str[i+1] in ['D', 'M']) or 
            (roman_str[i] == 'X' and roman_str[i+1] in ['L', 'C']) or
            (roman_str[i] == 'I' and roman_str[i+1] in ['V', 'X'])):
            total_value += VALUES_DICT[roman_str[i+1]] - VALUES_DICT[roman_str[i]]
            i += 1
        else:
            total_value += VALUES_DICT[roman_str[i]]

        i += 1

    return total_value

print(romanNumeralValue("MCMLXXIX"))