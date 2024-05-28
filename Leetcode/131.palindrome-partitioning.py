#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (69.26%)
# Likes:    12732
# Dislikes: 486
# Total Accepted:    890.1K
# Total Submissions: 1.3M
# Testcase Example:  '"aab"'
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
#
#


# @lc code=start
class Solution:
    def isPali(self, str):
        l, r = 0, len(str) - 1
        while l < r:
            while l < r and not str[l].isalnum():
                l += 1
            while l < r and not str[r].isalnum():
                r -= 1
            if str[l].lower() != str[r].lower():
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
