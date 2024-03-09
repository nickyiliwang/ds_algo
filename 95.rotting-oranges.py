#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
# https://leetcode.com/problems/rotting-oranges/description/
#
# algorithms
# Medium (53.87%)
# Likes:    12336
# Dislikes: 387
# Total Accepted:    784.1K
# Total Submissions: 1.5M
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# You are given an m x n grid where each cell can have one of three
# values:
#
#
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
#
#
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten
# orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange. If this is impossible, return -1.
#
#
# Example 1:
#
#
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
#
#
# Example 2:
#
#
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
#
#
# Example 3:
#
#
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer
# is just 0.
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.
#
#
#

from typing import List
from collections import deque

# Multi value BFS

# @lc code=start


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        rowBound, colBound = range(row), range(col)
        time, fresh = 0, 0
        q = deque()

        # Start with all fresh oranges count and location
        for r in rowBound:
            for c in colBound:
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])

        def transformOranges(r, c):
            nonlocal fresh
            if r not in rowBound or c not in colBound or grid[r][c] != 1:
                return

            grid[r][c] = 2
            fresh -= 1
            q.append([r, c])

        while q and fresh > 0:
            # need to process all items in queue
            for _ in range(len(q)):
                r, c = q.popleft()

                transformOranges(r + 1, c)
                transformOranges(r - 1, c)
                transformOranges(r, c + 1)
                transformOranges(r, c - 1)

            time += 1

        return time if fresh == 0 else -1


# @lc code=end

print(Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))


# DFS does not work here ?
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        rowBound, colBound = range(row), range(col)
        time = 0

        def dfs(r, c):
            if (
                row not in rowBound
                or col not in colBound
                or grid[r][c] == "0"
                or grid[r][c] == "2"
            ):
                return

            grid[r][c] = "2"
            time += 1

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in rowBound:
            for c in colBound:
                if grid[r][c] == "2":
                    dfs(r, c)

        for r in rowBound:
            for c in colBound:
                if grid[r][c] == "1":
                    return -1
        return time
