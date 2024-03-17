"""
704. Binary Search

Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
    Output: 4

Example 2:
    Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
    Output: -1
"""

from typing import List


def binary_search(nums: List[int], target: int) -> int:
    """
    Let T(n) be the runtime for an algorithm that satisfies the recursion
    T(n) = T(n/2) + 1 (and T(1) = 1). Prove that T(n) = O(log n).

    T(n) = T(n/2) + 1
         = (T(n/4) + 1) + 1
         = (T(n/8) + 1) + 1 + 1
         ...
    T(n) = T(n/(2^k)) + k

    Assume n/(2^k) = 1.
        n = 2^k
        log_2(n) = log_2(2^k)
        k = log_2(n)

    T(n) = T(1) + log_2(n)

    Therefore, T(n) = O(log n)
    """
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1
