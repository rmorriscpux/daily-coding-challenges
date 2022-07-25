'''
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2
'''

# The first part is a math problem that boils down to the fibonacci sequence.
# Best case is to use a list to calculate as we go. Lists are passed by reference so this is easy.
def fib(n, fib_list):
    # Initial positions
    if n <= 1:
        fib_list[n] = 1
    # If already calculated, 
    if fib_list[n] != -1:
        return fib_list[n]
    # Get next number in the sequence. At this point we won't be going deep down a rabbit hole for huge numbers since we have the previous two calculated already.
    fib_list[n] = fib(n-1, fib_list) + fib(n-2, fib_list)
    return fib_list[n]

def calc_steps(n):
    # Sanity check
    n = int(n)
    if n < 0:
        return 0
    # Initialize the list.
    fib_list = []
    for i in range(0, n+1):
        fib_list.append(-1)
    # Call Fibonacci Function.
    fib(n, fib_list)
    
    return fib_list[n]

# print(calc_steps(0))
# print(calc_steps(1))
# print(calc_steps(2))
# print(calc_steps(3))
# print(calc_steps(4))
# print(calc_steps(5))
# print(calc_steps(6))
# print(calc_steps(7))
# print(calc_steps(8))
# print(calc_steps(9))
# print(calc_steps(10))
# print(calc_steps(100))

'''
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X?
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
'''

# This is more complicated but can be solved in a manner similar to the one above. We just need to know the number of options we have.
def poly_fib(n, ways_list, num_options):
    # If already calculated
    if ways_list[n] != -1:
        return ways_list[n]
    # Calculate next number in the sequence and return.
    ways_list[n] = poly_fib(n-1, ways_list, num_options)
    for i in range(1, num_options):
        ways_list[n] += poly_fib(n-(2+i), ways_list, num_options)
    return ways_list[n]

def calc_mult_steps(n, options):
    # Sanity Check
    n = int(n)
    if n < 0:
        return 0
    if len(options) <= 1:
        return 1
    # Initialize ways_list
    ways_list = []
    for i in range(0, n+1):
        ways_list.append(-1)
    # Calculate the first full options for the ways_list.
    options.sort()
    # Up to the lowest number option, the number of ways will always be 1 (i.e. either one move, or impossible)
    for i in range(0, options[0]+1):
        ways_list[i] = 1
    # Now do up to the number in the last option. As far as I can tell, this kind of needs to be brute forced.
    for i in range(1, len(options)):
        for j in range(options[i-1], options[i]-1):
            poly_fib(j+1, ways_list, i)
        ways_list[options[i]] = ways_list[options[i-1]] + 1
    # And return
    poly_fib(n, ways_list, len(options))

    return ways_list[n]

print("==========")
print(calc_mult_steps(7, [1,2,3]))
print(calc_mult_steps(10, [1,3,5]))