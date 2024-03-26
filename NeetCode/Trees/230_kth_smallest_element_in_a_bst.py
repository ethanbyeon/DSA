"""
230. Kth Smallest Element in a BST

Given the root of a binary search tree,and an integer k,
return the kth smallest value (1-indexed) of all the values
of the nodes in the tree.

Example:
    Input: root = [3, 1, 4, null, 2], k = 1
    Output: 1
"""

from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    # Time Complexity: O(n)
    stack = []
    current = root
    while current is not None or stack is not None:
        while current is not None:
            stack.append(current)
            current = current.left
        stack.pop()
        k -= 1
        if k == 0:
            return current.val
        current = current.right
    return -1
