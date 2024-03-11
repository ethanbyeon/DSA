"""
Determine if a 9 x 9 Sudoku board is valid.
Only the filled cells need to be validated according to the following rules:

    1. Each row must contain the digits 1-9 without repetition.
    2. Each column must contain the digits 1-9 without repetition.
    3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits
        1-9 without repetition.

Note:
    - A Sudoku board (partially filled) could be valid but
        is not necessarily solvable.
    - Only the filled cells need to be validated according to the mentioned
      rules.
"""

from typing import List
from collections import defaultdict


def is_valid_sudoku(board: List[List[str]]) -> bool:
    """
                0     |     1     |     2
            0   1   2 | 3   4   5 | 6   7   8
    |  0  [   ,   ,   |   ,   ,   |   ,   ,   ]
    0  1  [   ,   ,   |   ,   ,   |   ,   ,   ]
    |  2  [   ,   ,   |   ,   ,   |   ,   ,   ]
    ------------------|-----------|------------
    |  3  [   ,   ,   |   ,   ,   |   ,   ,   ]
    1  4  [   ,   ,   |   ,   ,   |   ,   ,   ]
    |  5  [   ,   ,   |   ,   ,   |   ,   ,   ]
    ------------------|-----------|------------
    |  6  [   ,   ,   |   ,   ,   |   ,   ,   ]
    2  7  [   ,   ,   |   ,   ,   |   ,   ,   ]
    |  8  [   ,   ,   |   ,   ,   |   ,   ,   ]

    cell    = (row, col)
    sub-box = (row // 3, col // 3)

    Approach:
        Cell not in row hash map
        Cell not in column hash map
        Cell not in sub-box hash map

    Time Complexity: O(9^2)
    """
    col_map = defaultdict(set)
    row_map = defaultdict(set)
    sqr_map = defaultdict(set)  # key = (row // 3, col // 3)

    for r in range(9):
        for c in range(9):
            cell_value = board[r][c]
            if cell_value == ".":
                continue
            if (
                cell_value in row_map[r]
                or cell_value in col_map[c]
                or cell_value in sqr_map[(r // 3, c // 3)]
            ):
                return False
            row_map[r].add(cell_value)
            col_map[c].add(cell_value)
            sqr_map[(r // 3, c // 3)].add(cell_value)
    return True
