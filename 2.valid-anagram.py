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
#
#
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
#
#
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
#
#

from collections import Counter


# Time: O(s + t), Space: O(s + t)
# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cS, cT = Counter(s), Counter(t)

        for char in s:
            if cS[char] != cT[char]:
                return False

        return True


# @lc code=end


def isAnagram(s, t):
    if len(s) != len(t):
        return False

    countA, countB = {}, {}

    for i in range(len(s)):
        # get method gets the key's value, if the key doesn't exit, return 0 as default
        # s[i] is the value we want to search, t[i] for countB
        countA[s[i]] = countA.get(s[i], 0) + 1
        countB[t[i]] = countB.get(t[i], 0) + 1

    for j in countA:
        # using get so no key error if the key doesn't exist
        if countA[j] != countB.get(j, 0):
            return False
    return True
