#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (41.56%)
# Likes:    16377
# Dislikes: 4304
# Total Accepted:    2.9M
# Total Submissions: 6.9M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
#
# If there is no common prefix, return an empty string "".
#
#
# Example 1:
#
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
#
# Constraints:
#
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.
#
#
#

# @lc code=start
from collections import *
from typing import *


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        for i in range(len(strs[0])):
            for word in strs:
                # i == len(word) to check if out of bounds
                if i == len(word) or word[i] != strs[0][i]:
                    return common
            common += strs[0][i]

        return common


Solution.longestCommonPrefix("", ["flower", "flow", "flight"])
# @lc code=end
