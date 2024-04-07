#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#
# https://leetcode.com/problems/interleaving-string/description/
#
# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of
# s1 and s2.
#
# An interleaving of two strings s and t is a configuration where s and t are
# divided into n and m substrings respectively, such that:
#
#
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 +
# t3 + s3 + ...
#
#
# Note: a + b is the concatenation of strings a and b.
#
#
# Example 1:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Explanation: One way to obtain s3 is:
# Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
# Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" =
# "aadbbcbcac".
# Since s3 can be obtained by interleaving s1 and s2, we return true.
#
#
# Example 2:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
# Explanation: Notice how it is impossible to interleave s2 with any other
# string to obtain s3.
#
#
# Example 3:
#
#
# Input: s1 = "", s2 = "", s3 = ""
# Output: true
#
#
#
# Constraints:
#
#
# 0 <= s1.length, s2.length <= 100
# 0 <= s3.length <= 200
# s1, s2, and s3 consist of lowercase English letters.
#
#
#
# Follow up: Could you solve it using only O(s2.length) additional memory
# space?
#
#

# Keys
# dp or recursive this problem has:
# i + j = k which is the position of the letter we are checking for i or j
# checking i + 1 or j + 1 to move on to the next grid/sub problem
# if we run out of bounds, this base case means we reached the end, for dfs we return true

# 2DP
# nested loops bottom up approach
# need to make sure


# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        iLen, jLen, kLen = len(s1), len(s2), len(s3)

        if iLen + jLen != kLen:
            return False

        # like row and col, outside layer
        dp = [[False] * (jLen + 1) for _ in range(iLen + 1)]
        dp[iLen][jLen] = True  # this will point to outer because 0 base indexing

        for i in range(iLen, -1, -1):
            for j in range(jLen, -1, -1):
                if i < iLen and s3[i + j] == s1[i] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < jLen and s3[i + j] == s2[j] and dp[i][j + 1]:
                    dp[i][j] = True

        return dp[0][0]


# @lc code=end

print(Solution().isInterleave("abc", "acb", "aabccb"))


# DFS with recursion:
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        iLen, jLen, kLen = len(s1), len(s2), len(s3)

        if (iLen + jLen) != kLen:
            return False

        def dfs(i, j):
            # notice out of bounds meaning we reached the end
            if i == iLen and j == jLen:
                return True
            if (i, j) in dp:
                return dp[(i, j)]

            # i or j in bound, i + j = k to find the index we need for the letter, find the next sub problem with dfs
            if i < iLen and s3[i + j] == s1[i] and dfs(i + 1, j):
                return True
            if j < jLen and s3[i + j] == s2[j] and dfs(i, j + 1):
                return True

            dp[(i, j)] = False
            return False

        return dfs(0, 0)
