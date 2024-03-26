"""
235. Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST),
find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia:
    “The lowest common ancestor is defined between two nodes p and q 
    as the lowest node in T that has both p and q as descendants
    (where we allow a node to be a descendant of itself).”

Example:
    Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 8
    Output: 6
    Explanation: The LCA of nodes 2 and 8 is 6.
"""

from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def lca(
    root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]
) -> Optional[TreeNode]:
    # Time Complexity: O(log n)
    current = root
    while current is not None:
        if p.val > current.val and q.val > current.val:
            current = current.right
        elif p.val < current.val and q.val < current.val:
            current = current.left
        else:
            return current
    return TreeNode()
