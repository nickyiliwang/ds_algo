#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (39.96%)
# Likes:    8585
# Dislikes: 1836
# Total Accepted:    730.3K
# Total Submissions: 1.8M
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# You are given an m x n matrix board containing letters 'X' and 'O', capture
# regions that are surrounded:
#
#
# Connect: A cell is connected to adjacent cells horizontally or
# vertically.
# Region: To form a region connect every 'O' cell.
# Surround: The region is surrounded with 'X' cells if you can connect the
# region with 'X' cells and none of the region cells are on the edge of the
# board.
#
#
# A surrounded region is captured by replacing all 'O's with 'X's in the input
# matrix board.
#
#
# Example 1:
#
#
# Input: board =
# [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
#
# Output:
# [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
#
# Explanation:
#
# In the above diagram, the bottom region is not captured because it is on the
# edge of the board and cannot be surrounded.
#
#
# Example 2:
#
#
# Input: board = [["X"]]
#
# Output: [["X"]]
#
#
#
# Constraints:
#
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.
#
#
#


# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        rowBound, colBound = range(row), range(col)

        def dfs(r, c):
            if r not in rowBound or c not in colBound or board[r][c] != "O":
                return

            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in rowBound:
            dfs(r, 0)
            dfs(r, col - 1)

        for c in colBound:
            dfs(0, c)
            dfs(row - 1, c)

        for r in rowBound:
            for c in colBound:
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"


# @lc code=end
