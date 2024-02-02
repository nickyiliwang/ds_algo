#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii/description/
#
# algorithms
# Hard (36.18%)
# Likes:    9143
# Dislikes: 435
# Total Accepted:    619.8K
# Total Submissions: 1.7M
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' + '["oath","pea","eat","rain"]'
#
# Given an m x n board of characters and a list of strings words, return all
# words on the board.
#
# Each word must be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once in a word.
#
#
# Example 1:
#
#
# Input: board =
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
#
#
# Example 2:
#
#
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
#
#
#
# Constraints:
#
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 10^4
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.
#
#
#

from typing import *
from testCases import board, words

# @lc code=start


class TriNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Solution:
    def __init__(self):
        self.root = TriNode()

    def addWords(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TriNode()
            curr = curr.children[char]
        curr.isEnd = True

    def searchWord(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        row, col = len(board), len(board[0])
        path = set()
        result = set()

        for word in words:
            self.addWords(word)

        def dfs(r, c, node, word):
            if (
                r < 0
                or c < 0
                or r >= row
                or c >= col
                or (r, c) in path
                or board[r][c] not in node.children
            ):
                return

            path.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isEnd:
                result.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            path.remove((r, c))

        for r in range(row):
            for c in range(col):
                dfs(r, c, self.root, "")

        return list(result)


# @lc code=end
solution = Solution()
print(
    solution.findWords(
        board,
        words,
    )
)


# Brute force
def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    row, col = len(board), len(board[0])
    path = set()
    pointer = 0
    result = set()

    def dfs(r, c, i):
        if i == len(word):
            return True

        if (
            r < 0
            or c < 0
            or r >= row
            or c >= col
            or word[i] != board[r][c]
            or (r, c) in path
        ):
            return False

        path.add((r, c))
        res = (
            dfs(r + 1, c, i + 1)
            or dfs(r - 1, c, i + 1)
            or dfs(r, c + 1, i + 1)
            or dfs(r, c - 1, i + 1)
        )
        path.remove((r, c))
        return res

    while pointer < len(words):
        word = words[pointer]
        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    result.add(word)
        pointer += 1

    return result
