"""
100. Same Tree

Given the roots of two binary trees p and q,
write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.

Example:
    Input: p = [1, 2, 3], q = [1, 2, 3]
    Output: true
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    # Time Complexity: O(p + q)
    if p is None and q is None:
        return True
    if (p is None or q is None) and (p.val != q.val):
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
