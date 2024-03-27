#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
#
# There is a robot on an m x n grid. The robot is initially located at the
# top-left corner (i.e., grid[0][0]). The robot tries to move to the
# bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move
# either down or right at any point in time.
#
# Given the two integers m and n, return the number of possible unique paths
# that the robot can take to reach the bottom-right corner.
#
# The test cases are generated so that the answer will be less than or equal to
# 2 * 10^9.
#
#
# Example 1:
#
#
# Input: m = 3, n = 7
# Output: 28
#
#
# Example 2:
#
#
# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach
# the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
#
#
#
# Constraints:
#
#
# 1 <= m, n <= 100
#
#
#


# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row, col = m, n
        rowBound, colBound = range(row), range(col)
        matrix = [[0 for _ in colBound] for _ in rowBound]
        matrix[row - 1][col - 1] = 1

        for r in range(row - 1, -1, -1):
            for c in range(col - 1, -1, -1):
                if r + 1 in rowBound:
                    matrix[r][c] += matrix[r + 1][c]
                if c + 1 in colBound:
                    matrix[r][c] += matrix[r][c + 1]

        return matrix[0][0]


# @lc code=end

print(Solution().uniquePaths(3, 2))
