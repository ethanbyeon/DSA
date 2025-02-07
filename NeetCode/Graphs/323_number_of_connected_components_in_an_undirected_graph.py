"""
323. Number of Connected Components in an Undirected Graph

There is an undirected graph with n nodes.
There is also an edges array, where edges[i] = [a, b] means that
there is an edge between node a and node b in the graph.

The nodes are numbered from 0 to n - 1.

Return the total number of connected components in that graph.

Example 1:
    Input: n=3
           edges=[[0,1], [0,2]]
    Output: 1

Example 2:
    Input: n=6
           edges=[[0,1], [1,2], [2,3], [4,5]]
    Output: 2
"""

from collections import deque
from typing import List


def countComponentsDFS(n: int, edges: List[List[int]]) -> int:
    adj_map = [[] for _ in range(n)]
    for a, b in edges:
        adj_map[a].append(b)
        adj_map[b].append(a)

    visited = set()

    def dfs(node: int) -> None:
        for nei in adj_map[node]:
            if node not in visited:
                visited.add(node)
                dfs(nei)

    total = 0
    for node in range(n):
        if node not in visited:
            visited.add(node)
            dfs(node)
            total += 1
    return total


def countComponentsBFS(n: int, edges: List[List[int]]) -> int:
    adj_map = [[] for _ in range(n)]
    for a, b in edges:
        adj_map[a].append(b)
        adj_map[b].append(a)

    visited = set()

    def bfs(node: int) -> None:
        q = deque([node])
        visited.add(node)
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                for nei in adj_map[curr]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)

    total = 0
    for node in range(n):
        if node not in visited:
            bfs(node)
            total += 1
    return total
