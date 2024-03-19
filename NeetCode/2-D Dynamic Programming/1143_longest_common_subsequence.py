"""
1143. Longest Common Subsequence

Given two strings text1 and text2,
return the length of their longest common subsequence.
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string
with some characters (can be none) deleted without changing the relative order
of the remaining characters.

- For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
    Input: text1 = "abcde", text2 = "ace"
    Output: 3

Example 2:
    Input: text1 = "abc"m text2 = "abc"
    Output: 3

Example 3:
    Input: text1 = "abc", text2 = "def"
    Output: 0
"""


def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    Example 1:
          a   c   e
    i     0   1   2   3
        |---|---|---|---|
    a 0 | 3 | 2 | 1 | 0 |
    b 1 | 2 | 2 | 1 | 0 |
    c 2 | 2 | 2 | 1 | 0 |
    d 3 | 1 | 1 | 1 | 0 |
    e 4 | 1 | 1 | 1 | 0 |
      5 | 0 | 0 | 0 | 0 |

    Conditions:
        1. If cell has matching characters: 1 + bottom-right cell
        2. Otherwise: max{bottom cell, right cell}

    Time Complexity: O(n * m)
    """
    dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
    return dp[0][0]
