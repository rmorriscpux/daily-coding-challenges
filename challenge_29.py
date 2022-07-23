'''
Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character.
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding.
You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.
'''

def runLengthEncode(in_str):
    # Setup
    encoded_str = ""
    current_char = in_str[0]
    count = 1
    # Loop
    for character in in_str[1:]:
        if character == current_char:
            count += 1
        else:
            encoded_str = encoded_str + str(count) + current_char
            # Reset
            count = 1
            current_char = character
    # Finish
    encoded_str = encoded_str + str(count) + current_char
    return encoded_str

def runLengthDecode(in_str):
    decoded_str = ""
    for i in range(0, len(in_str), 2):
        decoded_str = decoded_str + in_str[i+1] * int(in_str[i])
    return decoded_str

encoded = runLengthEncode("AAAABBBCCDAA")
decoded = runLengthDecode(encoded)
print(encoded)
print(decoded)