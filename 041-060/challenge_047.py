'''
Given a array of numbers representing the stock prices of a company in chronological order,
write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
'''

from typing import List

# Note: This function as it is here assumes that there is an option to never buy.
def stockProfit(prices: List[int]):
    if len(prices) <= 1:
        return 0

    min_price = prices[0]
    max_price_diff = 0 # Set this to float('-inf') for the case where one must buy and sell once.

    for price in prices[1:]:
        if price - min_price > max_price_diff:
            max_price_diff = price - min_price

        if price < min_price:
            min_price = price

    return max_price_diff

print(stockProfit([9, 11, 8, 5, 7, 10]))