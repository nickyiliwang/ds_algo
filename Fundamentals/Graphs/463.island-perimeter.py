#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#
# https://leetcode.com/problems/island-perimeter/description/
#
# algorithms
# Easy (72.90%)
# Likes:    6809
# Dislikes: 380
# Total Accepted:    640.5K
# Total Submissions: 878.5K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# You are given row x col grid representing a map where grid[i][j] = 1
# represents land and grid[i][j] = 0 represents water.
#
# Grid cells are connected horizontally/vertically (not diagonally). The grid
# is completely surrounded by water, and there is exactly one island (i.e., one
# or more connected land cells).
#
# The island doesn't have "lakes", meaning the water inside isn't connected to
# the water around the island. One cell is a square with side length 1. The
# grid is rectangular, width and height don't exceed 100. Determine the
# perimeter of the island.
#
#
# Example 1:
#
#
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
#
#
# Example 2:
#
#
# Input: grid = [[1]]
# Output: 4
#
#
# Example 3:
#
#
# Input: grid = [[1,0]]
# Output: 4
#
#
#
# Constraints:
#
#
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] is 0 or 1.
# There is exactly one island in grid.
#
#
#


from typing import List


# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        rowBound, colBound = range(row), range(col)
        visited = set()

        def dfs(r, c):
            if r not in rowBound or c not in colBound or grid[r][c] == 0:
                return 1

            if (r, c) in visited:
                return 0

            visited.add((r, c))
            return dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in rowBound:
            for c in colBound:
                if grid[r][c]:
                    return dfs(r, c)


# @lc code=end

print(
    Solution().islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]])
)
