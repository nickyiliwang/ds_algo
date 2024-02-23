#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
# https://leetcode.com/problems/n-queens/description/
#
# algorithms
# Hard (67.55%)
# Likes:    11947
# Dislikes: 267
# Total Accepted:    677.2K
# Total Submissions: 1M
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle. You
# may return the answer in any order.
#
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space,
# respectively.
#
#
# Example 1:
#
#
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above
#
#
# Example 2:
#
#
# Input: n = 1
# Output: [["Q"]]
#
#
#
# Constraints:
#
#
# 1 <= n <= 9
#
#
#
from typing import List


# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        row, col = n, n
        board = [["." for _ in range(n)] for _ in range(n)]
        # board = ["." * n for _ in range(n)]
        res = []
        path = set()

        def dfs(i, r, c, queens, board):
            if queens == n:
                res.append(board)
                return

            if (
                r < 0
                or r >= row
                or c < 0
                or c >= col
                or (r, c) in path
                or board[r][c] == "Q"
            ):
                return

            board[r][c] = "Q"
            queens += 1

            path.add((r, c))
            dfs(i + 1, r + 1, c, queens, board)
            dfs(i + 1, r - 1, c, queens, board)
            dfs(i + 1, r, c + 1, queens, board)
            dfs(i + 1, r, c - 1, queens, board)

            dfs(i + 1, r + 1, c + 1, queens, board)
            dfs(i + 1, r + 1, c - 1, queens, board)
            dfs(i + 1, r - 1, c + 1, queens, board)
            dfs(i + 1, r - 1, c + 1, queens, board)
            path.remove((r, c))

        for r in range(row):
            for c in range(col):
                dfs(0, r, c, 0, board)

        return res


# @lc code=end

print(Solution().solveNQueens(4))
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

# WIP recursive
# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         row, col = n, n

#         def dfs(i, r, c, queens):
#             if queens == n:


#         for r in range(row):
#             for c in range(col):
#                 dfs(0, r, c, 0)
