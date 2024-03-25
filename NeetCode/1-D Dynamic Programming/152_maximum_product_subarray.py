"""
152. Maximum Product Subarray

Given an integer array nums,
find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
    Input: nums = [2, 3, -2, 4]
    Output: 6
    Explanation: [2, 3] has the largest product 6.

Example 2:
    Input: nums = [-2, 0, -1]
    Output: 0
    Explanation: The result cannot be 2, because [-2, -1] is not a subarray.
"""

from typing import List


def max_product(nums: List[int]) -> int:
    # Time Complexity: O(n)
    result = nums[0]
    current_min = 1
    current_max = 1
    for n in nums:
        temp = current_max * n
        current_max = max(temp, n * current_min, n)
        current_min = min(temp, n * current_min, n)
        result = max(result, current_max)
    return result
