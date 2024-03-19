"""
647. Palindromic Substrings

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backwards as forward.

A substring is a contiguous sequence of characters within the string.

Example 1:
    Input: s = "abc"
    Output: 3

Example 2:
    Input: s = "aaa"
    Output: 6
"""


def count_palindrome(s: str, left: int, right: int) -> int:
    count = 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        count += 1
        left -= 1
        right += 1
    return count


def count_substrings(s: str) -> int:
    # Time Complexity: O(n^2)
    count = 0
    for i in range(len(s)):
        count += count_palindrome(s, i, i)
        count += count_palindrome(s, i, i + 1)
    return count
