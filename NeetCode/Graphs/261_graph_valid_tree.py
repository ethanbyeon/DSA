"""
261. Graph Valid Tree

Given n nodes labeled from 0 to n - 1 and
a list of undirected edges (each edge is a pair of nodes),
write a function to check whether these edges make up a valid tree.

Example 1:
    Input: n = 5
           edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    Output: true

Example 2:
    Input: n = 5
           edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    Output: false

Note:
- You can assume that no duplicate edges will appear in edges.
  Since all edges are undirected, [0, 1] is the same as [1, 0]
  and thus will not appear together in edges.
"""

from collections import deque
from typing import List


def validTreeDFS(n: int, edges: List[List[int]]) -> bool:
    if len(edges) > n - 1:
        return False

    adj_map = [[] for _ in range(n)]
    for a, b in edges:
        adj_map[a].append(b)
        adj_map[b].append(a)

    visited = set()

    def dfs(node: int, parent: int) -> bool:
        if node in visited:
            return False

        visited.add(node)
        for nei in adj_map[node]:
            if nei == parent:
                continue
            if not dfs(nei, node):
                return False
        return True

    return dfs(0, -1) and len(visited) == n


def validTreeBFS(n: int, edges: List[List[int]]) -> bool:
    if len(edges) > n - 1:
        return False

    adj_map = [[] for _ in range(n)]
    for a, b in edges:
        adj_map[a].append(b)
        adj_map[b].append(a)

    visited = set([0])
    q = deque([(0, -1)])

    while q:
        for _ in range(len(q)):
            node, parent = q.popleft()
            for nei in adj_map[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                visited.add(node)
                q.append((nei, node))

    return len(visited) == n
