"""
105. Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is 
the preorder traversal of a binary tree and inorder is 
the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
    Input: preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]
    Output: [3, 9, 20, null, null, 15, 7]

Example 2:
    Input: preorder = [-1], inorder = [-1]
    Output: [-1]
"""

from typing import List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder: List[int], inorder: List[int]) -> TreeNode | None:
    # Time Complexity: O(n)
    if len(preorder) == 0 or len(inorder) == 0:
        return None
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = build_tree(preorder[1 : mid + 1], inorder[:mid])
    root.right = build_tree(preorder[mid + 1 :], inorder[mid + 1 :])
    return root
