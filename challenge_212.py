'''
Spreadsheets often use this alphabetical encoding for its columns: “A”, “B”, “C”, …, “AA”, “AB”, …, “ZZ”, “AAA”, “AAB”, ….

Given a column number, return its alphabetical column id. For example, given 1, return “A”. Given 27, return “AA”.
'''

def getColumnId(col_num: int):
    assert col_num > 0

    col_id = ""
    while col_num > 0:
        col_num -= 1
        col_id = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[col_num % 26] + col_id
        col_num //= 26

    return col_id

print(getColumnId(1))
print(getColumnId(27))
print(getColumnId(28))
print(getColumnId(731))