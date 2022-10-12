'''
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''

import random

# Note: In practice, should have a separate .py file for this and import.
CODE_MAP = {
    '1'  : 'a',
    '2'  : 'b',
    '3'  : 'c',
    '4'  : 'd',
    '5'  : 'e',
    '6'  : 'f',
    '7'  : 'g',
    '8'  : 'h',
    '9'  : 'i',
    '10' : 'j',
    '11' : 'k',
    '12' : 'l',
    '13' : 'm',
    '14' : 'n',
    '15' : 'o',
    '16' : 'p',
    '17' : 'q',
    '18' : 'r',
    '19' : 's',
    '20' : 't',
    '21' : 'u',
    '22' : 'v',
    '23' : 'w',
    '24' : 'x',
    '25' : 'y',
    '26' : 'z'
}

def waysToDecode(message):
    def rWaysToDecode(remaining_message, decode_words, current_word):
        # End case - remaining_message depleted.
        if not remaining_message:
            decode_words.append(current_word)
            return

        index = remaining_message[0]

        # index is 0 = Invalid case.
        if index == 0:
            return

        # Recursion part.
        rWaysToDecode(remaining_message[1:], decode_words, current_word + CODE_MAP[index])

        if len(remaining_message) >= 2:
            if index == '1' or (index == '2' and int(remaining_message[1]) <= 6):
                index += remaining_message[1]
                rWaysToDecode(remaining_message[2:], decode_words, current_word + CODE_MAP[index])

        return decode_words

    all_words = rWaysToDecode(str(message), [], "")
    return len(all_words)

# Original implementation I had, not using recursion, based on a Monte Carlo method.
# It takes more time and loses reliability with more digits in the message.
def waysToDecodeRandom(message):
    message = str(message)
    decodes_found = set(())

    for i in range(0, 1000000):
        decode = ""
        # Traverse through the message to get letters.
        digit = 0
        while digit < len(message):
            key = message[digit]

            # Special case for 1, since it could be 10-19 as well, so long as it's not the last digit.
            if (key == '1' and digit < len(message) - 1):
                decision = random.randint(0,1)
                # On decision of 1, add the next digit to the key and increment i.
                if decision == 1:
                    key = key + message[digit+1]
                    digit += 1

            # Special case for 2, since it could be 20-26 as well, so long as it's not the last digit.
            elif (key == '2' and digit < len(message) - 1 and message[digit+1] != ('7' or '8' or '9')):
                decision = random.randint(0,1)
                # On decision of 1, add the next digit to the key and increment i.
                if decision == 1:
                    key = key + message[digit+1]
                    digit += 1

            # Add to the decode
            decode = decode + CODE_MAP[key]

            digit += 1

        decodes_found.add(decode) # Since python sets don't allow duplicate values, if the decoded message already exists in the set, it won't be added.

    return len(decodes_found)

print(waysToDecode(1111))
print(waysToDecode(1126))
print(waysToDecode(2127))
print(waysToDecode(16541324))