#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (42.88%)
# Likes:    15707
# Dislikes: 661
# Total Accepted:    1.7M
# Total Submissions: 3.9M
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


# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        rowBound, colBound = range(row), range(col)
        visited = set()

        def bt(i, r, c):
            if i == len(word):
                return True

            if (
                r not in rowBound
                or c not in colBound
                or (r, c) in visited
                or board[r][c] != word[i]
            ):
                return False

            visited.add((r, c))
            res = (
                bt(i + 1, r + 1, c)
                or bt(i + 1, r - 1, c)
                or bt(i + 1, r, c + 1)
                or bt(i + 1, r, c - 1)
            )
            visited.remove((r, c))

            return res

        for r in rowBound:
            for c in colBound:
                if bt(0, r, c):
                    return True

        return False


# @lc code=end
