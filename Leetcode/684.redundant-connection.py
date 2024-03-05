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
from collections import defaultdict


# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjacencyList = defaultdict(list)
        visited = set()

        def cycle_detect(a, b):
            if a == b:
                return True

            visited.add(a)
            for nei in adjacencyList[a]:
                if nei not in visited and cycle_detect(nei, b):
                    return True
            visited.remove(a)

            return False

        for a, b in edges:
            if cycle_detect(a, b):
                return [a, b]
            else:
                adjacencyList[a].append(b)
                adjacencyList[b].append(a)
        return None


# @lc code=end

print(Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
# [2,3]
# print(Solution().findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
# [1,4]


# DFS with O(N ^ 2)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjacencyList = defaultdict(list)
        visited = set()

        def cycle_detect(a, b):
            if a == b:
                return True

            visited.add(a)
            for nei in adjacencyList[a]:
                if nei not in visited and cycle_detect(nei, b):
                    return True
            visited.remove(a)

            return False

        for a, b in edges:
            if cycle_detect(a, b):
                return [a, b]
            else:
                adjacencyList[a].append(b)
                adjacencyList[b].append(a)
        return None
