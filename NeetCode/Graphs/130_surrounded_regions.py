"""
130. Surrounded Regions

You are given an m x n matrix board containing letters 'X' and 'O',
capture regions that are surrounded:

- Connect: A cell is connected to adjacent cells horizontally or vertically.
- Region: To form a region connect every 'O' cell.
- Surround: The region is surrounded with 'X' cells if you can connect
            the region with 'X' cells and none of the region cells are
            on the edge of the board.

To capture a surrounded region, replace all 'O's with 'X's in-place
within the original board. You do not need to return anything.


Example 1:
    Input: board = [
                    ["X","X","X","X"],
                    ["X","O","O","X"],
                    ["X","X","O","X"],
                    ["X","O","X","X"]]
    Output: [
                ["X","X","X","X"],
                ["X","X","X","X"],
                ["X","X","X","X"],
                ["X","O","X","X"]]
    Explanation: In the above diagram, the bottom region is not
                 captured because it is on the edge of the board
                 and cannot be surrounded.

Example 2:
    Input: board = [["X"]]
    Output: [["X"]]
"""

from typing import List


def solve(board: List[List[str]]) -> None:
    ROWS, COLS = len(board), len(board[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(row: int, col: int):
        if (
            row not in range(ROWS)
            or col not in range(COLS)
            or board[row][col] != "O"
        ):
            return
        board[row][col] = "#"
        for dr, dc in directions:
            dfs(row + dr, col + dc)

    for row in range(ROWS):
        if board[row][0] == "O":
            dfs(row, 0)
        if board[row][COLS - 1] == "O":
            dfs(row, COLS - 1)

    for col in range(COLS):
        if board[0][col] == "O":
            dfs(0, col)
        if board[ROWS - 1][col] == "O":
            dfs(ROWS - 1, col)

    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == "O":
                board[row][col] = "X"
            elif board[row][col] == "#":
                board[row][col] = "O"
