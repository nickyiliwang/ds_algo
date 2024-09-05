#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome. Return all possible palindrome partitioning of s.
#
#
# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:
# Input: s = "a"
# Output: [["a"]]
#
#
# Constraints:
#
#
# 1 <= s.length <= 16
# s contains only lowercase English letters.
#

from typing import List

# Key:
# simple implementation since s only contains lower case letters

# @lc code=start
class Solution:
    def isPali(self, a):
        l, r = 0, len(a) - 1
        while l < r:
            if a[l] != a[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(i, subset):
            if i >= len(s):
                res.append(subset.copy())
                return

            for j in range(i, len(s)):
                potential = s[i : j + 1]
                if self.isPali(potential):
                    dfs(j + 1, subset + [potential])

        dfs(0, [])

        return res


# @lc code=end

print(Solution().partition("aab"))
