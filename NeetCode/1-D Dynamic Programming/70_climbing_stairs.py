"""
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Example 1:
    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

Example 2:
    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
"""


def climb_stairs(n: int) -> int:
    """
    Approach 1: Fibonacci Sequence
    fib(n) = fib(n - 1) + fib(n - 2)

    Approach 2: Bottom-Up
    Example:
                ___
            ___|   |
        ___|       |
    ___|           |
     0   1   2   3

    [3   2   1   1 ]

    Time Complexity: O(n)
    """

    # Bottom-Up Approach:
    # Space Complexity: O(n + 1)
    # dp = [0] * (n + 1)
    # dp [0] = 1
    # dp [1] = 1
    # for i in range(2, n + 1):
    #   dp[i] = dp[i - 1] + dp[i - 2]
    # return dp[n]

    prev = 1
    next = 1
    for _ in range(n - 1):
        temp = next
        next += prev
        prev = temp
    return next
