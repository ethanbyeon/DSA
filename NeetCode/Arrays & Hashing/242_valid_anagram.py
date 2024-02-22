"""
242. Valid Anagram

Given two strings `s` and `t`,
return true if 't' is an anagram of `s`,
and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters
of a different word or phrase, typically using all the original letters
exactly once.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:
    Input: s = "rat", t = "car"
    Output: false
"""


def is_anagram(s: str, t: str) -> bool:
    """
    Determines if two strings, `s` and `t`, are anagrams.
    Unequal lengths disqualify them.
    This approach uses a hashmap to track character frequencies in `s`.
    Then, it decrements frequencies for characters in `t`.
    Non-zero frequencies mean they are not anagrams.
    Otherwise, they are considered anagrams.

    Time Complexity: O(n), where n is the length of the longer input string.
    """
    if len(s) != len(t):
        return False

    freq_map = {}

    for letter in s:
        if letter in freq_map:
            freq_map[letter] += 1
        else:
            freq_map[letter] = 1

    for letter in t:
        if letter not in freq_map:
            return False
        freq_map[letter] -= 1

    for freq in freq_map.values():
        if freq != 0:
            return False
    return True
