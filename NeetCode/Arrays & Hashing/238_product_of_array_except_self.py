"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is
equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and 
without using the division operation.

Example 1:
    Input: nums = [1, 2, 3, 4]
    Output: [24, 12, 8, 6]

Example 2:
    Input: nums = [-1, 1, 0, -3, 3]
    Output: [0, 0, 9, 0, 0]
"""

from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    """
    Given:    [    a   ,   b  ,   c  ,    d    ]
    Prefix  = [    a   ,  a*b , a*b*c, a*b*c*d ]
    Postfix = [ a*b*c*d, b*c*d,  c*d ,    d    ]

    result[i] = prefix[i - 1] * postfix[i + 1]
    --> [ 1(b*c*d), a(c*d), (a*b)d, (a*b*c)1 ]

    Time Complexity: O(n)
    """
    product_list = [1] * len(nums)
    prefix = 1
    postfix = 1
    for i in range(len(nums)):
        product_list[i] = prefix
        prefix *= nums[i]
    for i in range(len(nums) - 1, -1, -1):
        product_list[i] *= postfix
        postfix *= nums[i]
    return product_list
