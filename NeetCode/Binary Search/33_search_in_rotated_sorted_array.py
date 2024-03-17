"""
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown
pivot index k (1 <= k < nums.length) such that the resulting array is
[nums[k], nums[k + 1], ..., nums[n - 1], nums[0], nums[1], ..., nums[k - 1]]
(0-indexed). For example, [0, 1, 2, 4, 5, 6, 7] might be rotated at pivot
index 3 and become [4, 5, 6, 7, 0, 1, 2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    """
    1. Determine the pivot point occurs in the sorted array.
    2. Based on the target value and the pivot point,
        decide whether to search the left or right portion of the array.
    3. Conduct binary search within the identified portion of the array to
        locate the target element.
    4. Acount for edge cases where the target might be on the opposite side
        of the pivot.
    5. Repeat the process until the target is found or the search space is exhausted.

    Time Complexity: O(log n)
    """
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1
