#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#
# https://leetcode.com/problems/reverse-string/description/
#
# algorithms
# Easy (77.54%)
# Likes:    8178
# Dislikes: 1145
# Total Accepted:    2.4M
# Total Submissions: 3.1M
# Testcase Example:  '["h","e","l","l","o"]'
#
# Write a function that reverses a string. The input string is given as an
# array of characters s.
#
# You must do this by modifying the input array in-place with O(1) extra
# memory.
#
#
# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s[i] is a printable ascii character.
#
#
#

from typing import List


# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1

        while left <= right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            left += 1
            right -= 1

        return s


# @lc code=end
sol = Solution()

print(sol.reverseString(["h", "e", "l", "l", "o"]))
