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

# Key:
# len(s) + 1 because we want to get to the last empty letter without triggering False
# ie. "abc" if we reach 4 we can return True

# s[j:i]
# leetcode
#     ^ = i
# ^ = j
# s[j:i] = "leet"

# dp[j] == True : checking the cache before validating and adding new

# break here so we only search till find

# we are only returning dp[count] and not the last element in the dp, the count + 1 is here so the s[j:i] make sense.


# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        count = len(s)
        dp = [False] * (count + 1)
        dp[0] = True

        for i in range(count + 1):
            for j in range(i):
                if (dp[j] == True) and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[count]


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
