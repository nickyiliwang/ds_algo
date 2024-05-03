#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# Given two strings s and t of lengths m and n respectively, return the minimum
# window substring of s such that every character in t (including duplicates)
# is included in the window. If there is no such substring, return the empty
# string "".
#
# The testcases will be generated such that the answer is unique.
#
#
# Example 1:
#
#
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C'
# from string t.
#
#
# Example 2:
#
#
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
#
#
# Example 3:
#
#
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
#
#
#
# Constraints:
#
#
# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s and t consist of uppercase and lowercase English letters.
#
#
#
# Follow up: Could you find an algorithm that runs in O(m + n) time?
#
#
from collections import Counter

# Key
# Sliding window
# increment have count one be one until we reach needed len
# only increment have len when the count does not exceed the needed count for the char
# while we find/still have a matching length
# update the results and shrink the left pointer/window

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        haveC, needC = Counter(), Counter(t)
        haveLen, needLen = 0, len(t)
        res, resLen = "", float("inf")

        left = 0

        for right in range(len(s)):
            haveC[s[right]] += 1

            if haveC[s[right]] <= needC[s[right]]:
                haveLen += 1

            while haveLen == needLen:
                currLen = right - left + 1
                if currLen < resLen:
                    res = s[left : right + 1]
                    resLen = currLen

                haveC[s[left]] -= 1 

                if haveC[s[left]] < needC[s[left]]:
                    haveLen -= 1

                left += 1
        return res

# @lc code=end
