"""
102. Binary Tree Level Order Traversal

Given the root of a binary tree,
return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

Example:
    Input: root = [3, 9, 20, null, null, 15, 7]
    Output: [[3], [9, 20], [15, 7]]
"""

from collections import deque
from typing import List, Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    # Time Complexity: O(n)
    bfs = []
    queue = deque([root])
    while queue is not None:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            if node is not None:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
       if len(level) > 0: 
            bfs.append(level)
    return bfs
