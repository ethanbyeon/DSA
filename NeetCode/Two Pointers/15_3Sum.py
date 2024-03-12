"""
15. 3Sum

Given an integer array nums, return all triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
    Input: nums = [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]

Example 2:
    Input: nums = [0, 1, 1]
    Output: []

Example 3:
    Input: nums = [0, 0, 0]
    Output: [[0, 0, 0]]
"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Ex 1. [-1, 0, 1, 2, -1, -4] -> [-4, -1, -1, 0, 1, 2]

    _ + _ + _ = 0
    a   b   c

    [-4, -1, -1, 0, 1, 2]
      a  {b            c}

    -> a + two_sum([b...c]) = 0

    Duplicate Cases:
        For a:
            Increment 'a' to move to the next value,
            as all combinations starting with the current value have been computed.
        For b and c:
            Increment 'b' or decrement 'c' to explore different combinations.

    Time Complexity: O(n log n) + O(n^2) = O(n^2)
    """
    triplets_list = []
    nums.sort()

    for i, i_val in enumerate(nums):
        if (i > 0) and (i_val == nums[i - 1]):
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            three_sum = i_val + nums[left] + nums[right]
            if three_sum > 0:
                right -= 1
            elif three_sum < 0:
                left += 1
            else:
                triplets_list.append([i_val, nums[left], nums[right]])
                left += 1
                while (nums[left] == nums[left - 1]) and (left < right):
                    left += 1
    return triplets_list
