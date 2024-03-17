"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3

Example 2:
    Input: s = "bbbbb"
    Output: 1

Example 3:
    Input: s = "pwwkew"
    Output: 3
"""


def length_of_longest_substring(s: str) -> int:
    # Time Complexity: O(n)
    substring_length = 0
    char_set = set()

    left = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        substring_length = max(substring_length, len(char_set))
    return substring_length
