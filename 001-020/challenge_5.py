'''
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
'''

# Utilizing Lambda functions to access individual members of a pair from a nested function.

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(cons):
    return cons(lambda a,b: a)

def cdr(cons):
    return cons(lambda a,b: b)

print(car(cons(1,2)))
print(cdr(cons("X","Y")))