"""
226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

Example:
    Input: root = [4, 2, 7, 1, 3, 6, 9]
    Output: [4, 7, 2, 9, 6, 3, 1]
"""

from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    # Time Complexity: O(n)
    if root is None:
        return None

    temp = root.left
    root.left = root.right
    root.right = temp
    invert_tree(root.left)
    invert_tree(root.right)
    return root
