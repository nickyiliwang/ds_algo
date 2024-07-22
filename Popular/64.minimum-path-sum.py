#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (64.46%)
# Likes:    12446
# Dislikes: 170
# Total Accepted:    1.2M
# Total Submissions: 1.9M
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right, which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
#
# Example 1:
#
#
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
#
#
# Example 2:
#
#
# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 200
#
#
#

from typing import List


# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        rowBound, colBound = range(row), range(col)

        for r in rowBound:
            for c in colBound:
                if r > 0 and c > 0:
                    grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])
                elif r > 0:
                    grid[r][0] += grid[r - 1][0]
                elif c > 0:
                    grid[0][c] += grid[0][c - 1]
        return grid[row - 1][col - 1]


# @lc code=end
