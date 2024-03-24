"""
572. Subtree of Another Tree

Given the roots of two binary trees root and subRoot,
return true if there is a subtree of root with the same structure and
node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node 
in tree and all of this node's descendants.
The tree tree could also be considered as a subtree of itself.

Example:
    Input: root = [3, 4, 5, 1, 2], subRoot = [4, 1, 2]
    Output: true
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    if p is None and q is None:
        return True
    if (p is None or q is None) and (p.val != q.val):
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


def is_subtree(root: TreeNode, sub_root: TreeNode) -> bool:
    # Time Complexity: O(root * sub_root)
    if sub_root is None:
        return True
    if root is None:
        return False
    if is_same_tree(root, sub_root) == True:
        return True
    return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)
