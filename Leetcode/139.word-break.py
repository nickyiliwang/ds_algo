#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# Given a string s and a dictionary of strings wordDict, return true if s can
# be segmented into a space-separated sequence of one or more dictionary
# words.
#
# Note that the same word in the dictionary may be reused multiple times in the
# segmentation.
#
#
# Example 1:
#
#
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
#
#
# Example 2:
#
#
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
#
#
#

from typing import List


# DP
# O(n * m ^ 2)
# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        pass


# @lc code=end
print(Solution().wordBreak("leetcode", ["leet", "code"]))


# DFS
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(curr, wordDict, memo):
            if curr in memo:
                return memo[curr]

            if not curr:
                return True

            for word in wordDict:
                if curr.startswith(word):
                    nextPart = curr[len(word) :]
                    if dfs(nextPart, wordDict, memo):
                        memo[curr] = True
                        return True

            memo[curr] = False
            return False

        return dfs(s, wordDict, {})


# 34/46 cases passed (N/A)
# "cars"
# ["car","ca","rs"]
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = s
        for word in wordDict:
            res = res.replace(word, "x")

        for c in res:
            if c != "x":
                return False

        return True
