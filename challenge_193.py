'''
Given a array of numbers representing the stock prices of a company in chronological order,
write a function that calculates the maximum profit you could have made from buying and selling that stock.
You're also given a number fee that represents a transaction fee for each buy and sell transaction.

You must buy before you can sell the stock, but you can make as many transactions as you like.

For example, given [1, 3, 2, 8, 4, 10] and fee = 2, you should return 9, since you could buy the stock at 1 dollar,
and sell at 8 dollars, and then buy it at 4 dollars and sell it at 10 dollars.
Since we did two transactions, there is a 4 dollar fee, so we have 7 + 6 = 13 profit minus 4 dollars of fees.
'''

from typing import List

def maxProfit(stock_prices: List[int], fee: int):
    def rMaxProfit(stock_prices, fee, profit, index, holding):
        # End case.
        if index == len(stock_prices):
            return profit

        # When holding the stock, change reflects selling the stock. When not holding, change reflects buying the stock.
        change = stock_prices[index] - fee if holding else -stock_prices[index]
        # Recur into both the stay case and the action case, return the max profit between them.
        return max(rMaxProfit(stock_prices, fee, profit, index+1, holding), rMaxProfit(stock_prices, fee, profit+change, index+1, not holding))

    assert all(map(lambda p: p > 0, stock_prices)) and fee >= 0

    return rMaxProfit(stock_prices, fee, 0, 0, False)

print(maxProfit([1, 3, 2, 8, 4, 10], 2))