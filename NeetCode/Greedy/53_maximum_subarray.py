"""
53. Maximum Subarray

Given an integer array nums,
find the subarray with the largest sum, and return its sum.

Example 1:
    Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Output: 6
    Explanation: The subarray [4, -1, 2, 1] has the largest sum 6.

Example 2:
    Input: nums = [1]
    Output: 1
    Explanation: The subarray [1] has the largest sum 1.
"""

from typing import List


def max_subarray(nums: List[int]) -> int:
    # Time Complexity: O(n)
    max_sub = nums[0]
    current_sum = 0
    for n in nums:
        if current_sum < 0:
            current_sum = 0
        current_sum += n
        max_sub = max(max_sub, current_sum)
    return max_sub
