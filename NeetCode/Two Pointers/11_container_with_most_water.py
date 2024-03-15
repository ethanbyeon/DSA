"""
11. Container With Most Water

You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith
line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.

Example 1:
    Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    Output: 49

Example 2:
    Input: height = [1, 1]
    Output: 1
"""

from typing import List


def max_area(height: List[int]) -> int:
    """
    Edge Case:
        When both heights are equal,
        moving either pointer inward won't change the maximum area.
        At equal heights, the container's width is already maximized,
        so further inward movement reduces the width without increasing the area.

    Time Complexity: O(n)
    """
    if len(height) == 2:
        return min(height[0], height[1])

    max_area = 0

    left = 0
    right = len(height) - 1
    while left < right:
        area = (right - left) * min(height[left], height[right])
        max_area = max(area, max_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area
