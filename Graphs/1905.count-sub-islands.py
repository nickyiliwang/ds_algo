#
# @lc app=leetcode id=1905 lang=python3
#
# [1905] Count Sub Islands
#
# https://leetcode.com/problems/count-sub-islands/description/
#
# algorithms
# Medium (67.43%)
# Likes:    2075
# Dislikes: 63
# Total Accepted:    93.6K
# Total Submissions: 138.8K
# Testcase Example:  '[[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]\n' +
# '[[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]'
#
# You are given two m x n binary matrices grid1 and grid2 containing only 0's
# (representing water) and 1's (representing land). An island is a group of 1's
# connected 4-directionally (horizontal or vertical). Any cells outside of the
# grid are considered water cells.
#
# An island in grid2 is considered a sub-island if there is an island in grid1
# that contains all the cells that make up this island in grid2.
#
# Return the number of islands in grid2 that are considered sub-islands.
#
#
# Example 1:
#
#
# Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],
# grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
# Output: 3
# Explanation: In the picture above, the grid on the left is grid1 and the grid
# on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island.
# There are three sub-islands.
#
#
# Example 2:
#
#
# Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],
# grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
# Output: 2
# Explanation: In the picture above, the grid on the left is grid1 and the grid
# on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island.
# There are two sub-islands.
#
#
#
# Constraints:
#
#
# m == grid1.length == grid2.length
# n == grid1[i].length == grid2[i].length
# 1 <= m, n <= 500
# grid1[i][j] and grid2[i][j] are either 0 or 1.
#
#
#


# @lc code=start
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        res = 0
        row, col = len(grid2), len(grid2[0])
        rowBound, colBound = range(row), range(col)
        visited = set()

        def dfs(r, c):
            res = True
            if (
                r not in rowBound
                or c not in colBound
                or grid2[r][c] == 0
                or (r, c) in visited
            ):
                return True

            visited.add((r, c))

            if grid1[r][c] == 0:
                res = False

            res = dfs(r + 1, c) and res
            res = dfs(r - 1, c) and res
            res = dfs(r, c + 1) and res
            res = dfs(r, c - 1) and res
            return res

        for r in rowBound:
            for c in colBound:
                if grid2[r][c] and (r, c) not in visited and dfs(r, c):
                    res += 1

        return res


# @lc code=end
