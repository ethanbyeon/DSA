"""
213. House Robber II

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected,
and it will automatically contact the police if two adjacent houses
were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

Example:
    Input: nums = [2, 3, 2]
    Output: 3
"""

from typing import List


def rob_one(nums: List[int]) -> int:
    one = 0
    two = 0
    for n in nums:
        temp = max(one + n, two)
        one = two
        two = temp
    return two


def house_robber_two(nums: List[int]) -> int:
    # Time Complexity: O(n)
    return max(nums[0], rob_one(nums[1:]), rob_one(nums[:-1]))
