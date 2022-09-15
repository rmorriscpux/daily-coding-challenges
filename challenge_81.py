'''
Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent.
You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], ...} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
'''

LETTER_MAPPING = {
    '2': ['A', 'B', 'C'],
    '3': ['D', 'E', 'F'],
    '4': ['G', 'H', 'I'],
    '5': ['J', 'K', 'L'],
    '6': ['M', 'N', 'O'],
    '7': ['P', 'Q', 'R', 'S'],
    '8': ['T', 'U', 'V'],
    '9': ['W', 'X', 'Y', 'Z'], 
}

def phoneNumberString(phone_number: int):

    def buildStringList(remaining_num_str, string_list, current_string):
        # End case: Remaining string is empty.
        # Add current_string to string_list and return.
        if remaining_num_str == "":
            string_list.append(current_string)
            return

        # Error case.
        if remaining_num_str[0] not in LETTER_MAPPING:
            raise ValueError(f"Invalid Character '{remaining_num_str[0]}'.")

        # Recur into buildStringList() adding a letter to the current_string and removing the leading digit.
        for letter in LETTER_MAPPING[remaining_num_str[0]]:
            buildStringList(remaining_num_str[1:], string_list, current_string + letter)

        return

    string_list = []
    buildStringList(str(phone_number), string_list, "")
    return string_list

print(phoneNumberString(23))
print(phoneNumberString(9876543))