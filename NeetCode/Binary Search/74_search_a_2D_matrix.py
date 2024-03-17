"""
74. Search a 2D Matrix

You are given a m x n integer matrix with the following two properties:
    1. Each row is sorted in non-decreasing order.
    2. The first integer of each row is greater than the last integer 
        of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    # Time Complexity: O(log(m * n))
    h = len(matrix)
    w = len(matrix[0])
    l = 0
    r = (w * h) - 1
    while l <= r:
        mid = (l + r) // 2
        row = mid // w
        col = mid % w
        if matrix[row][col] == target:
            return True
        if matrix[row][col] < target:
            l = mid + 1
        else:
            r = mid - 1
    return False
