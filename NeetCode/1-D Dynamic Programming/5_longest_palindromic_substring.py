"""
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:
    Input: s = "babad"
    Output: "bab"

Example 2:
    Input: s = "cbbd"
    Output: "bb"
"""


def longest_palindrom(s: str):
    # Time Complexity: O(n^2)

    # Bottom-Up Approach:
    # Space Complexity: O(n^2)
    # n = len(s)
    # if n >= 1:
    #     return n
    # dp = [[0] * n] * n
    # for i in range(n):
    #     dp[i][i] = 1
    # for len in range(2, n - 1):
    #     for i in range((n - len) - 1):
    #         j = (i + len) - 1
    #         if len == 2 and s[i] == s[j]:
    #               dp[i][j] = 2
    #         elif s[i] == s[j]:
    #               dp[i][j] = dp[i + 1][j - 1] + 2
    #         else:
    #               dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    # return dp[0][n - 1]

    # Expand from Center Approach:
    # Space Complexity: O(1)
    max_l = 0
    max_r = 0
    max_len = 0
    for i in range(len(s)):
        l = i
        r = i
        # Odd Palindrome
        while (l >= 0) and (r < len(s)) and (s[i] == s[r]):
            if (r - l + 1) > max_len:
                max_l = l
                max_r = r + 1
                max_len = (r - l) + 1
            l -= 1
            r += 1
        # Even Palindrome
        l = i
        r = i + 1
        while (l >= 0) and (r < len(s)) and (s[i] == s[r]):
            if (r - l + 1) > max_len:
                max_l = 1
                max_r = r + 1
                max_len = (r - l) + 1
            l -= 1
            r += 1
    return s[max_l:max_r]
