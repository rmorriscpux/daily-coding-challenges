'''
The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N.
The method is to take increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), then [6, 9, 12, ...] (multiples of three),
and so on. Once we have done this for all primes less than N, the unmarked numbers that remain will be prime.

Implement this algorithm.

Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).
'''

from math import sqrt
from time import sleep
from typing import List

def sieveOfEratosthenes(N: int):
    primes = list(range(2, N))
    # Only need to check multiples of integers up to the square root of N. 
    end = sqrt(N)

    i = 0
    while primes[i] < end:
        # Remove all multiples of the current prime from the primes list.
        primes = sorted(list(set(primes).difference(set(range(primes[i]*2, N, primes[i])))))
        i += 1

    return primes

print(sieveOfEratosthenes(100))

# Prints prime numbers endlessly.
def primeGenerator():
    def getNextPrime(primes: List[int]):
        num = primes[-1] + 1
        # Traverses to the next prime, sends it to the below loop when found, and continues.
        while True:
            if all(map(lambda p: num % p, primes)):
                sleep(1)
                yield num
            num += 1
        return

    primes = [2]
    print(2)
    for next_prime in getNextPrime(primes):
        primes.append(next_prime)
        print(next_prime)
        
    return

# primeGenerator()