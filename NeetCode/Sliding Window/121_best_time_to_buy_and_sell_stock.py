"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given
stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Example 1:
    Input: prices = [7, 1, 5, 3, 6, 4]
    Output: 5

Example 2:
    Input: prices = [7, 6, 4, 3, 1]
    Output: 0
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    """
    "Buy Low, Sell High"

    Time Complexity: O(n)
    """
    max_profit = 0
    l = 0
    for r in range(1, len(prices)):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
        else:
            l = r
    return max_profit
