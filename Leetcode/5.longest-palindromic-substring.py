#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (32.76%)
# Likes:    27265
# Dislikes: 1616
# Total Accepted:    2.6M
# Total Submissions: 8M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
#
#
# Example 1:
#
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: s = "cbbd"
# Output: "bb"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
#
#
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        def isPali(l, r):
            nonlocal res
            nonlocal resLen
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            # odd
            l, r = i, i
            isPali(l, r)

            # even
            l, r = i, i + 1
            isPali(l, r)

        return res


# @lc code=end
print(Solution().longestPalindrome("babad"))
