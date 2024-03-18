"""
198. House Robber

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent
houses have security systems connected and it will automatically call the police
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without 
alerting the police.

Example 1:
    Input: nums = [1, 2, 3, 1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).

Example 2:
    Input: nums = [2, 7, 9, 3, 1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9),
    and rob house 5 (money = 1).
"""

from typing import List


def rob(nums: List[int]) -> int:
    """
    Track the maximum loot achievable up to the current house,
    considering whether to rob the current house or skip it.
    Iterate through the houses, calculating the maximum loot at each house
    based on the loot from previous houses.

    Time Complexity: O(n)
    """
    h1 = 0
    h2 = 0
    # [h1, h2, n, n + 1, ...]
    for n in nums:
        temp = max(n + h1, h2)
        h1 = h2
        h2 = temp
    return h2
