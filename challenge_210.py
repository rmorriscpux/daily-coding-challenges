'''
A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

if n is even, the next number in the sequence is n / 2
if n is odd, the next number in the sequence is 3n + 1
It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?
'''

def collatzSeq(n: int, steps: int=0):
    assert n > 0
    global collatzCache

    if n == 1:
        return steps

    if collatzCache and n in collatzCache:
        return steps + collatzCache[n]

    if n % 2 == 1:
        return collatzSeq(n * 3 + 1, steps + 1)
    else:
        return collatzSeq(n // 2, steps + 1)

def collatzTest():
    global collatzCache
    collatzCache.clear()

    for i in range(1, 1000001):
        collatzCache[i] = collatzSeq(i)

    print(max(collatzCache, key=lambda k: collatzCache[k]))
    return

collatzCache = {}

collatzTest()