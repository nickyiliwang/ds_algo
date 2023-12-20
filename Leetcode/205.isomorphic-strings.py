#
# @lc app=leetcode id=205 lang=python
#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (43.46%)
# Likes:    7930
# Dislikes: 1848
# Total Accepted:    1.1M
# Total Submissions: 2.4M
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to
# get t.
#
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character, but a character may map to itself.
#
#
# Example 1:
# Input: s = "egg", t = "add"
# Output: true
# Example 2:
# Input: s = "foo", t = "bar"
# Output: false
# Example 3:
# Input: s = "paper", t = "title"
# Output: true
#
#
# Constraints:
#
#
# 1 <= s.length <= 5 * 10^4
# t.length == s.length
# s and t consist of any valid ascii character.
#
#
#


# @lc code=start


# O(n) solution, one loop
class Solution(object):
    def isIsomorphic(self, s, t):
        mapST, mapTS = {}, {}

        for c1, c2 in zip(s, t):  # iterating both str in parallel
            # 1. check key exist in dict
            # 2. check the if mapST[c1] == c2
            # 3. check the if mapTS[c2] == c1
            if (c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1):
                return False

            mapST[c1] = c2
            mapTS[c2] = c1

        return True


# @lc code=end

Solution.isIsomorphic("", "foo", "bar")


# My solution logic:
# build a replacementHash for iteration + replacement in s
# split s into list replace individual char => join
# compare s and t for bool return
class Solution(object):
    def isIsomorphic(self, s, t):
        if len(set(s)) != len(set(t)):
            return False

        replacementHash = {}

        for i, c in enumerate(t):
            replacementHash[s[i]] = c

        s = [c for c in s]
        for i, c in enumerate(s):
            s[i] = replacementHash[c]

        return "".join(s) == t
