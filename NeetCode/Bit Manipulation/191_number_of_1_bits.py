"""
191. Number of 1 Bits

Write a function that takes the binary representation of a positive integer
and returns the number of set bits it has (also known as the Hamming weight).

Example 1:
    Input: n = 11
    Output: 3
"""


def hamming_weight(n: int) -> int:
    # Time Complexity: O(1)
    total = 0
    while n > 0:
        # Trick:
        # n = n & (n - 1) # Gets rid of one bit (right-most 1)
        # total += 1
        total += n % 2
        n = n >> 1  # OR n //= 2
    return total
