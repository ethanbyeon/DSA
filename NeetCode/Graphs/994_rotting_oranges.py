"""
994. Rotting Oranges

You are given an m x n grid where each cell can have one of three values:
    - 0 representing an empty cell,
    - 1 representing a fresh orange, or
    - 2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to
a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until
no cell has a fresh orange. If this is impossible, return -1.


Example 1:
    Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4

Example 2:
    Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1
    Explanation: The orange in the bottom left corner (row 2, column 0) is
                 never rotten, because rotting only happens 4-directionally.

Example 3:
    Input: grid = [[0,2]]
    Output: 0
    Explanation: Since there are already no fresh oranges at minute 0,
                 the answer is just 0.
"""

from collections import deque
from typing import List


def orangesRotting(grid: List[List[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()
    fresh = 0
    mins = 0

    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 1:
                fresh += 1
            if grid[row][col] == 2:
                q.append((row, col))

    while fresh > 0 and q:
        for _ in range(len(q)):
            row, col = q.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (
                    nr in range(ROWS)
                    and nc in range(COLS)
                    and grid[nr][nc] == 1
                ):
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1
        mins += 1

    if fresh != 0:
        return -1
    return mins
