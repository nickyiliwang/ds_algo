#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (51.08%)
# Likes:    12314
# Dislikes: 340
# Total Accepted:    892.9K
# Total Submissions: 1.7M
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given two strings s and p, return an array of all the start indices of p's
# anagrams in s. You may return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
#
#
# Example 1:
#
#
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
#
# Example 2:
#
#
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#
#
#
# Constraints:
#
#
# 1 <= s.length, p.length <= 3 * 10^4
# s and p consist of lowercase English letters.
#
#
#

from typing import *
from collections import *

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        c1 = Counter(p)
        res = []
        window = len(p)

        c2 = Counter()

        for i in range(len(s)):
            if i < window:
                c2[s[i]] += 1
            else:
                c2[s[i - window]] -= 1
                c2[s[i]] += 1

            if c1 == c2:
                # here we appended the tail to c2 so the index is at the end of the window
                # window is length not index so to get the first index of the current window size, we add one after minus window.
                res.append(i - window + 1)

        return res


# @lc code=end
