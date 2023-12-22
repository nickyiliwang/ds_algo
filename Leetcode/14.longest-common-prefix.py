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
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        validator = strs[0]

        # making sure we have a base range
        # looping each character index of first word
        for i in range(len(validator)):
            for w in strs:
                # if the index is equal to the length of word we are checking
                # then we know it's still inbound
                # if the i letter of each word does not match the first, return the current result

                # i == len(word) to check if out of bounds
                if i == len(w) or w[i] != validator[i]:
                    return res
            # else append each letter that passed the condition
            res += validator[i]

        return res


Solution.longestCommonPrefix("", ["flower", "flow", "flight"])
# @lc code=end
