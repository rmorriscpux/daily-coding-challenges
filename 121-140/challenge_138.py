'''
Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
'''

def minCoins(n: int):
    if n < 0:
        raise ValueError("n must be non-negative")

    coin_count = n // 25
    n %= 25
    coin_count += n // 10
    n %= 10
    coin_count += n // 5
    coin_count += n % 5

    return coin_count

print(minCoins(16))
print(minCoins(108))