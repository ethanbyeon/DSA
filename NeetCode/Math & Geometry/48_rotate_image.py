"""
48. Rotate Image

You are given an n x n 2D matrix representing an image,
rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place,
which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
    Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
"""

from typing import List


def rotate(matrix: List[List[int]]) -> List[List[int]]:
    # Time Complexity: O(n^2)
    left = 0
    right = len(matrix) - 1
    while left < right:
        for i in range(right - left):
            top = left
            bottom = right
            top_left = matrix[top][left + i]
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = top_left
        left += 1
        right -= 1
    return matrix
