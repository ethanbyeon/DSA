"""
424. Longest Repeating Character Replacement

You are given a string s and an integer k.
You can choose any other character of the string and change it to any other
uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can
get after performing the above operations.

Example 1:
    Input: s = "ABAB", k = 2
    Output: 4

Example 2:
    Input: s = "AABABBA", k = 1
    Output: 4
"""


def character_replacement(s: str, k: int) -> int:
    """
    To ensure a substring's validity within a sliding window,
    we compare the window length to the frequency of its most common character,
    represented by max_freq.

    A substring is valid if the difference between the window length and
    max_freq is no greater than k,
    indicating the minimal changes required to make the window uniform.

    The maximum potential length of a valid substring is max_freq + k,
    where a higher max_freq implies a longer substring.

    If max_freq remains unchanged or decreases as the window expands,
    the best substring length remains unaffected, requiring no update.

    However, if max_freq increases, it indicates a character appearing more
    frequently, suggesting the potential for a longer valid substring,
    prompting an update to max_freq.

    Time Complexity: O(n)
    """
    max_length = 0
    char_count = {}
    max_freq = 0
    l = 0
    for r in range(len(s)):
        char_count[s[r]] = 1 + char_count.get(s[r], 0)
        max_freq = max(max_freq, char_count[s[r]])
        if (r - l + 1) - max_freq > k:
            char_count[s[l]] -= 1
            l += 1
        max_length = max(max_length, r - l + 1)
    return max_length
