#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (41.18%)
# Likes:    14855
# Dislikes: 613
# Total Accepted:    1.5M
# Total Submissions: 3.5M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given an m x n grid of characters board and a string word, return true if
# word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
#
#
# Example 1:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCCED"
# Output: true
#
#
# Example 2:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "SEE"
# Output: true
#
#
# Example 3:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCB"
# Output: false
#
#
#
# Constraints:
#
#
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
#
#
#
# Follow up: Could you use search pruning to make your solution faster with a
# larger board?
#
#

from typing import *


# BigO O(n * m * 4 ^ len(word))
# @lc code=start
class Solution:
    def exist(self, board, word: str) -> bool:
        row, col = len(board), len(board[0])
        path = set()

        def dfs(i, r, c):
            if i == len(word):
                return True

            if (
                r < 0
                or r >= row
                or c < 0
                or c >= col
                or (r, c) in path
                or word[i] != board[r][c]
            ):
                return False

            path.add((r, c))
            res = (
                dfs(i + 1, r + 1, c)
                or dfs(i + 1, r - 1, c)
                or dfs(i + 1, r, c + 1)
                or dfs(i + 1, r, c - 1)
            )

            path.remove((r, c))
            return res

        for r in range(row):
            for c in range(col):
                if dfs(0, r, c):
                    return True

        return False


# @lc code=end

print(
    Solution.exist(
        "", [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"
    )
)
