"""
98. Validate Binary Search Tree

Given the root of a binary tree,
determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:
    Input: root = [2, 1, 3]
    Output: true

Example 2:
    Input: root = [5, 1, 4, null, null, 3, 6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.
"""

from typing import Optional, Union


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    # Time Complexity: O(n)
    def is_valid(
        node: Optional[TreeNode],
        left: Union[TreeNode, int, float, None],
        right: Union[TreeNode, int, float, None],
    ) -> bool:
        if node is None:
            return True
        if not (node.val > left and node.val < right):
            return False
        return is_valid(node.left, left, node.val) and is_valid(
            node.right, node.val, right
        )

    return is_valid(root, float("-inf"), float("inf"))
