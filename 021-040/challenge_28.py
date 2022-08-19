'''
Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line.
There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k.
Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly

'''

def justifyText(word_list, k):
    def rJustifyText(sub_list, k, justified_lines):
        # Terminator condition.
        if len(sub_list) == 0:
            return
        # Remove the first words from the sub_list to start the new line words list.
        char_count = len(sub_list[0])
        new_line_words = [sub_list.pop(0)]
        # Now see how many words fit on a line.
        while 1:
            # List complete.
            if len(sub_list) == 0:
                break
            # Add words until the next word would put the number of characters on the line above k.
            # 1 needs to be added to each iteration so there is at least one space between words.
            if char_count + 1 + len(sub_list[0]) <= k:
                char_count += 1 + len(sub_list[0])
                new_line_words.append(sub_list.pop(0))
            else:
                break
        # We now have what fits on the next line. Now to add spaces.
        extra_spaces = k - char_count
        # Case where there is only one word: Add spaces to the right until k is filled.
        if len(new_line_words) == 1:
            justified_lines.append(new_line_words[0] + (" " * extra_spaces))
        # Case where there is more than one word: Use integer division and modulo operations to determine the whitespace size between words.
        else:
            # Get number of whitespaces between words.
            whitespaces = len(new_line_words) - 1
            # Figure out the spaces between 
            space_distance = extra_spaces // whitespaces + 1
            leftover_spaces = extra_spaces % whitespaces
            # Now build the line, taking into account extra spaces needed to fill the justification.
            new_line = new_line_words[0]
            for word in new_line_words[1:]:
                new_line = new_line + (" " * space_distance)
                if leftover_spaces > 0:
                    new_line = new_line + " "
                    leftover_spaces -= 1
                new_line = new_line + word
            # Add to the justified_lines list.
            justified_lines.append(new_line)

        # Now recur with the remaining words.
        return rJustifyText(sub_list, k, justified_lines)

    # Initial Setup
    justified_lines = []
    rJustifyText(word_list, k, justified_lines)
    # Return
    return justified_lines

print(justifyText(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16))
print(justifyText(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "hippopotamus"], 16))
