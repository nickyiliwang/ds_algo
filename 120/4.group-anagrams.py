#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
#
#
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
# Input: strs = [""]
# Output: [[""]]
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
#
#
# Constraints:
#
#
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
#
#
#

# Key
# sorted will break the string into an array, so we need to join it or use a tuple when appending to res
# Cleaver if you can remember it, with ord

from typing import List
from collections import defaultdict


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            res[tuple(sorted(word))].append(word)

        return res.values()


# @lc code=end

print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


# Cleaver if you can remember it, with ord
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for w in strs:
            alpha = [0] * 26
            for c in w:
                alpha[ord(c) - ord("a")] += 1
            res[tuple(alpha)].append(w)

        return res.values()
