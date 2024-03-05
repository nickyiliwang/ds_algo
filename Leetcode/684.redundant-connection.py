#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#
# https://leetcode.com/problems/redundant-connection/description/
#
# algorithms
# Medium (62.72%)
# Likes:    6022
# Dislikes: 387
# Total Accepted:    340.2K
# Total Submissions: 542.4K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
# In this problem, a tree is an undirected graph that is connected and has no
# cycles.
#
# You are given a graph that started as a tree with n nodes labeled from 1 to
# n, with one additional edge added. The added edge has two different vertices
# chosen from 1 to n, and was not an edge that already existed. The graph is
# represented as an array edges of length n where edges[i] = [ai, bi] indicates
# that there is an edge between nodes ai and bi in the graph.
#
# Return an edge that can be removed so that the resulting graph is a tree of n
# nodes. If there are multiple answers, return the answer that occurs last in
# the input.
#
#
# Example 1:
#
#
# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
#
#
# Example 2:
#
#
# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]
#
#
#
# Constraints:
#
#
# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ai < bi <= edges.length
# ai != bi
# There are no repeated edges.
# The given graph is connected.
#
#
#

from typing import List


# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjacencyList = [[] for _ in range(len(edges))]
        visited, cycle = set(), set()

        for a, b in edges:
            adjacencyList[a].append(b)

        def dfs(edge):
            if edge in cycle:
                print(edge, adjacencyList[edge - 1], adjacencyList)
                return False
            if edge in visited:
                return True

            cycle.add(edge)
            for eg in adjacencyList[edge - 1]:
                if dfs(eg) == False:
                    return False
            cycle.remove(edge)
            visited.add(edge)
            return True

        for eg in range(len(edges)):
            if dfs(eg) == False:
                return False

        return True


# @lc code=end

# print(Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
# [2,3]
print(Solution().findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
# [1,4]

# WIP non union find
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjacencyList = [[] for _ in range(len(edges))]
        visited, cycle = set(), set()

        for a, b in edges:
            adjacencyList[a].append(b)

        def dfs(edge):
            if edge in cycle:
                print(edge, adjacencyList[edge - 1], adjacencyList)
                return False
            if edge in visited:
                return True

            cycle.add(edge)
            for eg in adjacencyList[edge - 1]:
                if dfs(eg) == False:
                    return False
            cycle.remove(edge)
            visited.add(edge)
            return True

        for eg in range(len(edges)):
            if dfs(eg) == False:
                return False

        return True