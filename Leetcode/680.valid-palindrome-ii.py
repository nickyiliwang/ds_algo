#
# @lc app=leetcode id=680 lang=python
#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (39.97%)
# Likes:    7945
# Dislikes: 412
# Total Accepted:    677.4K
# Total Submissions: 1.7M
# Testcase Example:  '"aba"'
#
# Given a string s, return true if the s can be palindrome after deleting at
# most one character from it.
#
#
# Example 1:
#
#
# Input: s = "aba"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
#
#
# Example 3:
#
#
# Input: s = "abc"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.
#
#
#


""
# @lc code=start
class Solution:
    def validUtil(self, s, left, right):
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

    def validPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.validUtil(s, left + 1, right) or self.validUtil(
                    s, left, right - 1
                )
            else:
                left += 1
                right -= 1
        return True


# @lc code=end

print(Solution.validPalindrome("", "abcba"))


# # 462/469 cases passed (N/A)
# class Solution(object):
#     def validPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         left, right = 0, len(s) - 1
#         leeway = 1

#         while left <= right:
#             if s[left] != s[right]:
#                 if leeway > 0:
#                     if left + 1 <= right and s[left + 1] == s[right]:
#                         leeway -= 1
#                         left += 1
#                         continue
#                     elif left <= right - 1 and s[left] == s[right - 1]:
#                         right -= 1
#                         leeway -= 1
#                         continue
#                     else:
#                         return False
#                 else:
#                     return False
#             left += 1
#             right -= 1
#         return True
