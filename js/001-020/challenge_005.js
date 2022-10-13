/*
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
*/

function cons(a, b){
    function pair(f){
        return f(a, b);
    }
    return pair;
}

function car(cons){
    return cons((a, b) => a);
}

function cdr(cons){
    return cons((a, b) => b);
}

console.log(car(cons(1, 2)));
console.log(cdr(cons(1, 2)));