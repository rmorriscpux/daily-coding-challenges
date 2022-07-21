'''
This problem was asked by Facebook.

Implement regular expression matching with the following special characters:

    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.
'''

def myRegex(input_str, pattern):
    # Recursive matching function.
    def rMyRegex(input_str, pattern):
        # Terminator condition: pattern is empty.
        if pattern == "":
            # If there are still characters in input_str, it does not fit the pattern. So return True if input_str is empty, False if not.
            return input_str == ""

        # Check that the first character in input_str matches itself or the wild '.' character in pattern.
        match = bool(input_str) and pattern[0] in {input_str[0], '.'}

        # Now check for asterisk matching. Asterisk indicates that the previous character can occur 0 or more times.
        # We'll need separate recursions for when the character is not in the start of input_str or when it occurs at least once. Either case matches.
        if len(pattern) >= 2 and pattern[1] == '*':
            return rMyRegex(input_str, pattern[2:]) or (match and rMyRegex(input_str[1:], pattern))
        else:
            # Case where the next character is not '*':
            return match and rMyRegex(input_str[1:], pattern[1:])

    # Remove leading '*' characters since they are effectively null, along with duplicate, adjacent '*' since they're redundant.
    pattern = pattern.lstrip('*')
    clean_pattern = pattern.replace("**", "*")
    while clean_pattern != pattern:
        pattern = clean_pattern
        clean_pattern = pattern.replace("**", "*")

    return rMyRegex(input_str, clean_pattern)

print(myRegex("ray", "ra."))
print(myRegex("raymond", "ra."))
print(myRegex("chat", ".*at"))
print(myRegex("chat", ".*ats"))
print(myRegex("ray", "ra."))
print(myRegex("chat", ".**at"))
print(myRegex("chat", "c**at"))