"""
49. Group Anagrams

Given an array of strings str, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.

Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
    Input: strs = [""]
    Output: [[""]]

Example 3:
    Input: strs = ["a"]
    Output: [["a"]]
"""

from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Ex. 1: ["eat", "tea", "tan", "ate", "nat", "bat"]

    (a=1, ..., e=1, ..., t=1, ..., z=0) : ["eat", "tea", "ate"]
    (a=1, ..., n=1, ..., t=1, ..., z=0) : ["tan", "nat"]
    (a=1, ..., b=1, ..., t=1, ..., z=0) : ["bat"]
    """
    hash_map = defaultdict(list)  # char_count : [anagrams]

    for s in strs:
        count = [0] * 26  # a ... z
        for char in s:
            count[ord(char) - ord("a")] += 1
        hash_map[tuple(count)].append(s)

    return list(hash_map.values())
