"""
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Example:
    Input: root = [3, 9, 20, null, null, 15, 7]
    Output: 3
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode) -> int:
    # Time Complexity: O(n)
    # BFS Approach:
    # if root is None:
    #     return 0
    # level = 0
    # queue = deque([root])
    # while queue is not None:
    #     for i in range(len(queue)):
    #         node = queue.popleft()
    #         if node.left is not None:
    #             queue.append(node.left)
    #         if node.right is not None:
    #             queue.append(node.right)
    #     level += 1
    # return level

    # Iterative DFS (Pre-Order) Approach:
    # stack = [[root, 1]]
    # max_depth = 0
    # while stack is not None:
    #     node, depth = stack.pop()
    #     if node is not None:
    #         max_depth = max(max_depth, depth)
    #         stack.append([node.left, depth + 1])
    #         stack.append([node.right, depth + 1])
    # return max_depth

    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
