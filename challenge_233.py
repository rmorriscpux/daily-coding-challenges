'''
Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.
'''

# Uses O(1) space at the cost of having O(n) time complexity.
# A quicker fib(n), but with high space complexity, is a recursive algorithm utilizing a cache.
def fib(n: int) -> int:
    assert isinstance(n, int) and n > 0

    if n <= 2:
        return n-1

    prev2, prev1 = 0, 1
    cur = None
    for i in range(2, n):
        cur = prev2 + prev1
        prev2 = prev1
        prev1 = cur
    return cur

print([fib(i) for i in range(1, 11)])