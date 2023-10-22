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
        def validator(s):
            left, right = 0, len(s) - 1

            while left < right:
                while left < right and not s[left].isalnum():
                    left += 1

                while left > right and not s[right].isalnum():
                    right -= 1

                if s[left].lower() != s[right].lower():
                    return False
                
            return True
        
        left, right = 0, len(s) - 1
        
        while left < right: