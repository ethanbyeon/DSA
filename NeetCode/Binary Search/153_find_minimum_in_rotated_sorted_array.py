"""
153. Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between
1 and n times.
For example, the array nums = [0, 1, 2, 4, 5, 6, 7] might become:
    [4, 5, 6, 7, 0, 1, 2] if it was rotated 4 times.
    [0, 1, 2, 4, 5, 7, 8] if it was rotated 7 times.

Notice that rotating the array [a[0], a[1], a[2], ..., a[n - 1]]
1 times results in the array [a[n - 1], a[0], a[1], a[2], ..., a[n - 2]].

Given the sorted rotated array nums of unique elements,
return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""

from typing import List


def find_min(nums: List[int]) -> int:
    """
    Two conditions guide the approach:

    1. If the value at the middle index is greater than the value at the right
    index, the pivot (rotation point) is on the right side.
    Hence, we update our search space to span from the index immediately to
    the right of the middle index up to the right index.

    2. If the value at the middle index is not greater than the value at the
    right index, either the pivot is on the left side or there's no rotation.
    Here, the search space begins from the left index up to and including the
    middle index, covering the possibility of the middle index being the
    minimum element.

    Time Complexity: O(log n)
    """
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid
    return nums[l]
