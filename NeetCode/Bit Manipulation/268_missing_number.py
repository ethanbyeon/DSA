"""
268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Example:
    Input: nums = [3,0,1]
    Output: 2
"""

from typing import List


def missing_nums(nums: List[int]) -> int:
    # Time Complexity: O(n)
    series_sum = (len(nums) * (len(nums) + 1)) // 2
    return series_sum - sum(nums)
