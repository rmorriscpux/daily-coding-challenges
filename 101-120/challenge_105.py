'''
Given a function f, and N return a debounced f of N milliseconds.

That is, as long as the debounced f continues to be invoked, f itself will not be called for N milliseconds.
'''

from time import time, sleep

def debounce(N: int):
    time_limit = N / 1000
    current_time = None

    def decorate(f):
        def wrapper(*args, **kwargs):
            nonlocal current_time
            start_time = time()
            if current_time == None or start_time - current_time >= time_limit:
                result = f(*args, **kwargs)
                current_time = time()
                return result
        return wrapper
    return decorate

@debounce(3000)
def printSomething(input):
    print("Here is something:", input)
    return

printSomething("A")
sleep(1)
printSomething("B")
sleep(1)
printSomething("C")
sleep(1)
printSomething("D")