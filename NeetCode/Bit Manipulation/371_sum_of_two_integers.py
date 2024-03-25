"""
371. Sum of Two Integers

Given two integers a and b,
return the sum of the two integers without using the operators + and -.

Example 1:
    Input: a = 1, b = 2
    Output: 3

Example 2:
    Input: a = 2, b = 3
    Output: 5
"""


def get_sum(a: int, b: int) -> int:
    # Time Complexity: O(1)
    mask = 0xFFFFFFFF
    while b & mask > 0:
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    if b > 0:
        return a & mask
    return a
