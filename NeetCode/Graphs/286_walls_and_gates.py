"""
286. Walls and Gates

You are given a m × n 2D grid initialized with these three possible values:
    1. -1 - A water cell that can not be traversed.
    2. 0 - A treasure chest.
    3. INF - A land cell that can be traversed.
        We use the integer 2^31 - 1 = 2147483647 to represent INF.

Fill each land cell with the distance to its nearest treasure chest.
If a land cell cannot reach a treasure chest than the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.

Example 1:
    Input: [
        [2147483647,-1,0,2147483647],
        [2147483647,2147483647,2147483647,-1],
        [2147483647,-1,2147483647,-1],
        [0,-1,2147483647,2147483647]
    ]

    Output: [
      [3,-1,0,1],
      [2,2,1,-1],
      [1,-1,2,-1],
      [0,-1,3,4]
    ]

Example 2:
    Input: [
      [0,-1],
      [2147483647,2147483647]
    ]

    Output: [
      [0,-1],
      [1,2]
    ]
"""

from collections import deque
from typing import List


def islandsAndTreasureDFS(grid: List[List[int]]) -> None:
    # Time Complexity: O(m * n * 4^(m * n))
    ROWS, COLS = len(grid), len(grid[0])
    INF = 2147483647
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    visited = [[False] * COLS for _ in range(ROWS)]

    def dfs(row: int, col: int) -> int:
        if row < 0 or col < 0 or row >= ROWS or col >= COLS or visited[row][col]:
            return INF
        if grid[row][col] == 0:
            return 0

        visited[row][col] = True
        distance = INF
        for dr, dc in directions:
            distance = min(distance, 1 + dfs(row + dr, col + dc))
        visited[row][col] = False
        return distance

    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == INF:
                grid[row][col] = dfs(row, col)


def islandsAndTreasureBFS(grid: List[List[int]]) -> None:
    # Time Complexity: O((m * n)^2)
    ROWS, COLS = len(grid), len(grid[0])
    INF = 2147483647
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def bfs(row: int, col: int) -> int:
        q = deque([(row, col)])
        visited = [[False] * COLS for _ in range(ROWS)]
        visited[row][col] = True
        distance = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] == 0:
                    return distance
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < ROWS
                        and 0 <= nc < COLS
                        and not visited[nr][nc]
                        and grid[nr][nc] != -1
                    ):
                        q.append((nr, nc))
            distance += 1
        return INF

    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == INF:
                grid[row][col] = bfs(row, col)


def islandsAndTreasureMultiSourceBFS(grid: List[List[int]]) -> None:
    # Time Complexity: O(m * n)
    ROWS, COLS = len(grid), len(grid[0])
    visited = set()
    q = deque()

    def add_cell(row: int, col: int) -> None:
        if (
            min(row, col) < 0
            or row == ROWS
            or col == COLS
            or (row, col) in visited
            or grid[row][col] == -1
        ):
            return
        visited.add((row, col))
        q.append([row, col])

    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 0:
                q.append([row, col])
                visited.add((row, col))

    distance = 0
    while q:
        for _ in range(len(q)):
            row, col = q.popleft()
            grid[row][col] = distance
            add_cell(row, col - 1)
            add_cell(row, col + 1)
            add_cell(row - 1, col)
            add_cell(row + 1, col)
        distance += 1
