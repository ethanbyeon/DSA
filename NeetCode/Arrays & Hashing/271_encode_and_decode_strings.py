"""
271. Encode and Decode Strings

Design an algorithm to encode a list of strings to a single string.
The encoded string is then decoded back to the original list of strings.

Please implement 'encode' and 'decode'

Example 1:
    Input: ["lint","code","love","you"]

    Output:["lint","code","love","you"]

Example 2:

    Input: ["we","say",":","yes"]

    Output: ["we","say",":","yes"]
"""

from typing import List


def encode(strs: List[str]) -> str:
    """
    Encodes a list of strings into a single string.

    Approach:
    - For each string in the list, prepend its length followed by a delimiter.
    - This allows the decoder to determine the boundaries of each string.

    Time Complexity: O(n)
    """
    output = ""
    for s in strs:
        output += str(len(s)) + "_" + s
    return output


def decode(s: str) -> List[str]:
    """
    Decodes a single string back into a list of strings.

    Approach:
    - Iterate through the encoded string, identifying each string's length
      from the prefix before the delimiter "_".
    - Extract the substring of the specified length and add it to the output.
    - Continue until the entire encoded string is processed.

    Time Complexity: O(n)
    """
    output = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "_":
            j += 1
        length = int(s[i:j])
        output.append(s[j + 1 : (j + 1) + length])
        i = (j + 1) + length
    return output
