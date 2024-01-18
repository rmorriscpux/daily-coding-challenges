'''
You are presented with an array representing a Boolean expression. The elements are of two kinds:

T and F, representing the values True and False.
&, |, and ^, representing the bitwise operators for AND, OR, and XOR.
Determine the number of ways to group the array elements using parentheses so that the entire expression evaluates to True.

For example, suppose the input is ['F', '|', 'T', '&', 'T']. In this case, there are two acceptable groupings: (F | T) & T and F | (T & T).
'''

BOOL_VAL = {
    'T' : True,
    'F' : False
}

def getGroupings(arr: list[str]) -> int:
    def eval_group(expr1: bool, expr2: bool, oper: str) -> bool:
        assert oper in ['&', '|', '^']
        return eval(str(expr1) + oper + str(expr2))
    
    def rGetGroupings(arr: list[str]) -> int:
        count = 0
        for i in range(0, len(arr)-2, 2):
            new_arr = arr[:i] + [eval_group(arr[i], arr[i+2], arr[i+1])] + arr[i+3:]
            if len(new_arr) == 1:
                count += int(new_arr[0])
            else:
                count += rGetGroupings(new_arr)
        return count
    
    work_arr = []
    for ele in arr:
        if ele in ['T', 'F']:
            work_arr.append(BOOL_VAL[ele])
        else:
            work_arr.append(ele)

    return rGetGroupings(work_arr)

if __name__ == "__main__":
    print(getGroupings(['F', '|', 'T', '&', 'T']))
    print(getGroupings(['F', '|', 'T', '&', 'T', '^', 'T']))
    print(getGroupings(['F', '|', 'T', '&', 'T', '^', 'F']))