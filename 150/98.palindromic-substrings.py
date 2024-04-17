#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#
# https://leetcode.com/problems/palindromic-substrings/description/
#
# Given a string s, return the number of palindromic substrings in it.
#
# A string is a palindrome when it reads the same backward as forward.
#
# A substring is a contiguous sequence of characters within the string.
#
#
# Example 1:
#
#
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
#
# Example 2:
#
#
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consists of lowercase English letters.
#
#
#


# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def isPali(l, r):
            nonlocal res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            l, r = i, i
            isPali(l, r)

            l, r = i, i + 1
            isPali(l, r)

        return res


# @lc code=end

print(Solution().countSubstrings("aaa"))
