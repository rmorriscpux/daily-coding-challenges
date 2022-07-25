'''
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
'''

import time

# Using functions as variables.
def schedule(n, f, *args, **kwargs):
    time.sleep(n/1000) # time.sleep() parameter is in seconds, our function should use milliseconds.
    return f(*args, **kwargs)

def my_function(str):
    return "Returning " + str

output = schedule(5000, my_function, "This Cat.")
print(output)