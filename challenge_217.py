'''
We say a number is sparse if there are no adjacent ones in its binary representation.
For example, 21 (10101) is sparse, but 22 (10110) is not. For a given input N, find the smallest sparse number greater than or equal to N.

Do this in faster than O(N log N) time.
'''

# Unlike most programming languages, binary representations of positive and negative integers are equivalent in Python, save for a '-' prefacing negative integers.

def nextSparseNumber(N: int):
    n_bin = bin(N).split('b')[1]
    out_bin = ""

    if N >= 0:
        prev = None
        flag = False
        for i, digit in enumerate(n_bin):
            if digit == '1' and prev == '1':
                flag = True
            
            if flag:
                out_bin += '0' * (len(n_bin) - i)
                break
            else:
                out_bin += digit
                prev = digit

        if flag:
            out_bin = '10' + out_bin[1:] if out_bin[0] == '1' else '1' + out_bin

        return int(out_bin, base=2)
    else:
        prev = None
        flag = False
        for i, digit in enumerate(n_bin):
            if digit == '1' and prev == '1':
                flag = True

            if flag:
                out_bin += '01' * ((len(n_bin) - i) // 2)
                if len(out_bin) < len(n_bin):
                    out_bin += '0'
                break
            else:
                out_bin += digit
                prev = digit
                
        return -int(out_bin, base=2)

print(nextSparseNumber(21))
print(nextSparseNumber(22))
print(nextSparseNumber(-21))
print(nextSparseNumber(-22))