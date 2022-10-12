'''
What does the below code snippet print out? How can we fix the anonymous functions to behave as we'd expect?

    functions = []
    for i in range(10):
        functions.append(lambda : i)

    for f in functions:
        print(f())
'''

# The code snippet will print the value of 'i' at the moment each function is called in the second loop.
# In this case, it will print '9' ten times.
# To have the loop print out 0 through 9 as expected, fix it as below.

functions = []
for i in range(10):
    functions.append(lambda x=i : x) 
    # This sets an input 'x' for each function to the value of 'i' at the time of declaration as a default.
    # Therefore it returns that 'x' value when called with no parameters, as in the second loop.

for f in functions:
    print(f())