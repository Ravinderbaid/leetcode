from typing import List


class Solution:
    """
    Say you have an array for which the ith element is the price of a given stock on day i.

    If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

    Note that you cannot sell a stock before you buy one.

    Example 1:

    Input: [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
                Not 7-1 = 6, as selling price needs to be larger than buying price.

    Example 2:

    Input: [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.
    """

    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        profit = 0
        for i in prices:
            if stack != []:
                if stack[-1] > i:
                    stack.pop()
                    stack.append(i)
                else:
                    if stack[-1] < i:
                        profit = max(profit, i - stack[-1])
            else:
                stack.append(i)
            print(stack)
        return profit


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        min_prices = prices[0]
        profit = 0
        for i in prices[1:]:
            if min_prices > i:
                min_prices = i
            else:
                profit = max(profit, i - min_prices)
        return profit
