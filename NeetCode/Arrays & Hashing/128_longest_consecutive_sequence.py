"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums,
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
    Input: nums = [100, 4, 200, 1, 3, 2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
                 Therefore its length is 4.

Example 2:
    Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    Output: 9
"""

from typing import List


def longest_consecutive(nums: List[int]) -> int:
    """
    Ex. 1: [100, 4, 200, 1, 3, 2] -> {100, 4, 200, 1, 3, 2}

    1->2->3->4, 100, 200

    Start of a sequence: (num - 1) exists in set

    Time Complexity: O(n)
    """
    longest_length = 0
    nums_set = set(nums)

    for n in nums:
        if (n - 1) not in nums_set:
            curr_length = 0
            while (n + curr_length) in nums_set:
                nums_set.remove(n + curr_length)  # Reduce search space
                curr_length += 1
            longest_length = max(curr_length, longest_length)
    return longest_length
