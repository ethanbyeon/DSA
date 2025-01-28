"""
463. Island Perimeter

You are given row x col grid representing a map where grid[i][j] = 1
represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is exactly one island
(i.e., one or more connected land cells).

The island doesn't have "lakes",
meaning the water inside isn't connected to the water around the island.
One cell is a square with side length 1.
The grid is rectangular, width and height don't exceed 100.
Determine the perimeter of the island.


Example 1:
    Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    Output: 16
    Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:
    Input: grid = [[1]]
    Output: 4

Example 3:
    Input: grid = [[1,0]]
    Output: 4
"""

from typing import List


def islandPerimeter(grid: List[List[int]]) -> int:
    # DFS
    # visited = set()
    #
    # def dfs(i: int, j: int) -> int:
    #     if i < 0 or j < 0 or
    #         i >= len(grid) or j >= len(grid[0]) or
    #         grid[i][j] == 0:
    #             return 1
    #     if (i, j) in visited:
    #         return 0
    #
    #     visited.add((i, j))
    #     perimeter = dfs(i - 1, j)
    #     perimeter += dfs(i + 1, j)
    #     perimeter += dfs(i, j - 1)
    #     perimeter += dfs(i, j + 1)
    #     return perimeter
    #
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         if grid[i][j] == 1:
    #             return dfs(i, j)

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
