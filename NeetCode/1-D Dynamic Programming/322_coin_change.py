"""
322. Coin Change

You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins,
return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
    Input: coins = [1, 2, 5], amount = 11
    Ouptut: 3
    Explanation: 11 = 5 + 5 + 1

Example 2:
    Input: coins = [2], amount = 3
    Output: -1

Example 3:
    Input: coins = [1], amount = 0
    Output: 0
"""

from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    """
    Bottom-Up Approach:

    Example: coins = [1, 3, 4, 5], amount = 7

    dp[0] = 0
    dp[1] = 1
    dp[2] = 1 + dp[2 - 1] = 1 + dp[1] = 2
    dp[3] = 1
    dp[4] = 1
    dp[5] = 1
    dp[6] = 1 + dp[6 - 1] = 1 + dp[5] = 2 <- MIN
          = 1 + dp[6 - 3] = 1 + dp[3] = 2
          = 1 + dp[6 - 4] = 1 + dp[2] = 3
          = 1 + dp[6 - 5] = 1 + dp[1] = 2
    dp[7] = 1 + dp[7 - 1] = 1 + dp[6] = 3
          = 1 + dp[7 - 3] = 1 + dp[4] = 2 <- MIN
          = 1 + dp[7 - 4] = 1 + dp[3] = 2
          = 1 + dp[7 - 5] = 1 + dp[2] = 3

    Recurrence Relation:
        dp[amount] = min{dp[amount], dp[amount - coin] + 1}

    Time Complexity: O(amount * coins)
    """
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for coin in coins:
            if (a - coin) >= 0:
                dp[a] = min(dp[a], dp[a - coin] + 1)

    if dp[amount] == amount + 1:
        return -1
    return dp[amount]
