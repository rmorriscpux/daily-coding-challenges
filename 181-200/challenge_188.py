'''
What will this code print out?

def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i():
            print(i)
        flist.append(print_i)

    return flist

functions = make_functions()
for f in functions:
    f()
How can we make it print out what we apparently want?
'''

# The code will print out the following:
#   3
#   3
#   3
# Because the value of i is 3 in the function scope when it it called.
# To print out 1 then 2 then 3, the value 'i' needs to be stored along with the function in the list at time of creation and passed as a parameter.

def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i(i):
            print(i)
        flist.append((print_i, i))

    return flist

functions = make_functions()
for f, i in functions:
    f(i)
