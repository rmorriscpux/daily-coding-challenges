'''
Given a string and a number of lines k, print the string in zigzag form.
In zigzag, characters are printed out diagonally from top left to bottom right until reaching the kth line, then back up to top right, and so on.

For example, given the sentence "thisisazigzag" and k = 4, you should print:

t     a     g
 h   s z   a
  i i   i z
   s     g
'''

def zigzag(word: str, k: int):
    assert k > 0
    # If one line or word is an empty string, print the word and return.
    if k == 1 or not word:
        print(word)
        return
    # Setup. Make a list of lines, start at line 0, and direct to go down.
    lines = [""] * min(k, len(word))
    l_index = 0
    next = 1

    for i, letter in enumerate(word):
        # Add spaces up to length i on the current line, then place the current letter.
        lines[l_index] += " " * (i - len(lines[l_index])) + letter
        # Go to the next line, down or up depending on the value of next.
        l_index += next
        # Change directions if at the first or last line.
        if l_index in [0, len(lines)-1]:
            next = -next
    # Print out the lines, with newline character as the separator.
    print("\n".join(lines))

    return

zigzag("thisisazigzag", 4)
zigzag("abcdefghijklmnopqrstuvwxyz", 5)