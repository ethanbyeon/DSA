"""
207. Course Schedule

There are a total of numCourses courses you have to take,
labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi]
indicates that you must take course bi first if you want to take course ai.

- For example, the pair [0, 1],
  indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.


Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take.
    To take course 1 you should have finished course 0. So it is possible.

Example 2:
    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take.
    To take course 1 you should have finished course 0,
    and to take course 0 you should also have finished course 1.
    So it is impossible.
"""

from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    prereq_map = {i: [] for i in range(numCourses)}
    for course, prereq in prerequisites:
        prereq_map[course].append(prereq)

    visited = set()

    def dfs(course: int) -> bool:
        if course in visited:
            return False
        if prereq_map[course] == []:
            return True

        visited.add(course)
        for prereq in prereq_map[course]:
            if not dfs(prereq):
                return False
        visited.remove(course)
        prereq_map[course] = []
        return True

    for course in range(numCourses):
        if not dfs(course):
            return False
    return True
