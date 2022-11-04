'''
Given an array of numbers representing the stock prices of a company in chronological order and an integer k,
return the maximum profit you can make from k buys and sells.
You must buy the stock before you can sell it, and you must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.
'''

from typing import List

def getMaxProfit(price_list: List[int], k: int):
    def rGetMaxProfit(price_list, index, profit, buys, sells):
        if index == len(price_list) or sells == 0:
            # End states
            return profit

        if buys == sells:
            # Buy state. Buying results in the current price subtracted from profit.
            return max(rGetMaxProfit(price_list, index+1, profit-price_list[index], buys-1, sells),
                rGetMaxProfit(price_list, index+1, profit, buys, sells))
        else:
            # Sell state. Selling results in the current price added to profit.
            return max(rGetMaxProfit(price_list, index+1, profit+price_list[index], buys, sells-1),
                rGetMaxProfit(price_list, index+1, profit, buys, sells))

    return rGetMaxProfit(price_list, 0, 0, k, k)

print(getMaxProfit([5, 2, 4, 0, 1], 2))