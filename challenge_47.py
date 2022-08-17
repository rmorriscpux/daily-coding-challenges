'''
Given a array of numbers representing the stock prices of a company in chronological order,
write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
'''

from typing import List

# Brute Force: O(N^2). 0 essentially means never buy.
# Good luck if you can predict the future.
def stockProfit(prices: List[int]):
    if len(prices) <= 1:
        return 0

    buy_price = prices[0]

    max_profit = 0

    for i in range(1, len(prices)):
        if prices[i] - buy_price > max_profit:
            max_profit = prices[i] - buy_price

    recur_max_profit = stockProfit(prices[1:])

    return max_profit if max_profit >= recur_max_profit else recur_max_profit

print(stockProfit([9, 11, 8, 5, 7, 10]))