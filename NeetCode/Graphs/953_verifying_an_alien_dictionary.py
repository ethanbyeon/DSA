"""
953. Verifying an Alien Dictionary

In an alien language, surprisingly, they also use English lowercase letters,
but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language,
and the order of the alphabet, return true if and only if the given words
are sorted lexicographically in this alien language.


Example 1:
    Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
    Output: true
    Explanation: As 'h' comes before 'l' in this language,
                 then the sequence is sorted.

Example 2:
    Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
    Output: false
    Explanation: As 'd' comes after 'l' in this language,
                 then words[0] > words[1], hence the sequence is unsorted.

Example 3:
    Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
    Output: false
    Explanation: The first three characters "app" match,
                 and the second string is shorter (in size.)
                 According to lexicographical rules "apple" > "app", because
                 'l' > '∅', where '∅' is defined as the blank character which
                 is less than any other character (More info).
"""

from typing import List


def isAlienSorted(words: List[str], order: str) -> bool:
    # Time Complexity: O(n * m)
    # Space Complexity: O(1)
    order = {c: i for i, c in enumerate(order)}
    for i in range(len(words) - 1):
        word_a, word_b = words[i], words[i + 1]
        for j in range(len(word_a)):
            if j == len(word_b):
                return False
            if word_a[j] != word_b[j]:
                if order[word_a[j]] > order[word_b[j]]:
                    return False
                break
    return True
