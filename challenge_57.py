'''
Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less.
You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words.
If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return:
["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.
'''

# Done With Splitting.
def stringIntoLines1(s: str, k: int):
    def buildLines(s_list, k, lines):
        new_line = s_list[0]
        for i in range(1, len(s_list)):
            if len(new_line) + 1 + len(s_list[i]) > k:
                new_start = i
                break
            new_line += " " + s_list[i]
        else:
            lines.append(new_line)
            return
        
        lines.append(new_line)
        buildLines(s_list[new_start:], k, lines)
    
    lines = []
    buildLines(s.split(), k, lines)
    return lines

# Done Without Splitting. I like this better, but I have a feeling it's faster with the split.
def stringIntoLines2(s: str, k: int):
    def buildLines(s, k, lines):
        # Return if empty.
        if len(s) == 0:
            return
        # Add the last word(s) and return if len(s) is less than or equal to k.
        if len(s) <= k:
            lines.append(s)
            return

        # Find the point where the last space within k is.
        end_point = k
        while end_point > 0 and s[end_point] != " ":
            end_point -= 1

        if end_point == 0:
            # Word larger than k
            raise Exception("No word can be longer than k characters.")

        lines.append(s[:end_point])
        # Recur after the space.
        buildLines(s[end_point+1:], k, lines)

        return

    lines = []
    buildLines(s, k, lines)
    return lines

print(stringIntoLines1("The quick brown fox jumps over the lazy dog", 10))
print(stringIntoLines2("The quick brown fox jumps over the lazy dog", 10))