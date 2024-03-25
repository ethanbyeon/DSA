"""
297. Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object
into a sequence of bits so that it can be stored in a file or memory buffer,
or transmitted across a network connection link to be reconstructed later
in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree.
There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and
this string can be deserialized to the original tree structure.

Clarification:
The input/output format is the same as how LeetCode serializes a binary tree.
You do not necessarily need to follow this format,
so please be creative and come up with different approaches yourself.

Example 1:
    Input: root = [1, 2, 3, null, null, 4, 5]
    Output: [1, 2, 3, null, null, 4, 5]

Example 2:
    Input: root = []
    Output: []
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: TreeNode) -> str:
        result = []

        def dfs(node: TreeNode) -> str | None:
            if node is None:
                result.append("N")
                return ""
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(result)

    def deserialize(self, data: str) -> TreeNode | None:
        values = data.split(",")
        self.i = 0

        def dfs():
            if values[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(values[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
