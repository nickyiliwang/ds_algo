#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#
#
# Constraints:
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
#
from typing import *
from collections import *

# Time:
# Space:

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

# @lc code=end
print(Solution().isAnagram("anagram", "nagaram"))
