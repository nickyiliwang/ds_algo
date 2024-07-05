#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#
# https://leetcode.com/problems/longest-common-subsequence/description/
#
# Given two strings text1 and text2, return the length of their longest common
# subsequence. If there is no common subsequence, return 0.
#
# A subsequence of a string is a new string generated from the original string
# with some characters (can be none) deleted without changing the relative
# order of the remaining characters.
#
#
# For example, "ace" is a subsequence of "abcde".
#
#
# A common subsequence of two strings is a subsequence that is common to both
# strings.
#
#
# Example 1:
#
#
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.
#
#
# Example 2:
#
#
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
#
#
# Example 3:
#
#
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
#
#
#
# Constraints:
#
#
# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.
#


# Key
# text1 and text2 are row and col, 2D Matrix
# Bottom up approach to avoid repeated work
# if text1[r] == text2[c] we look diagonally for the next sub problem
# if no match we look bottom and right to any of them are a match


# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row, col = len(text1), len(text2)
        dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]

        for r in range(row - 1, -1, -1):
            for c in range(col - 1, -1, -1):
                if text1[r] == text2[c]:
                    dp[r][c] = dp[r + 1][c + 1] + 1
                else:
                    dp[r][c] = max(dp[r + 1][c], dp[r][c + 1])
        return dp[0][0]


# @lc code=end

print(Solution().longestCommonSubsequence("abcefd", "aacsd"))  # acd => 3
