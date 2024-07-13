#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (43.22%)
# Likes:    17550
# Dislikes: 4545
# Total Accepted:    3.5M
# Total Submissions: 8.1M
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

from typing import List


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i, c in enumerate(strs[0]):
            for w in strs:
                if i == len(w) or c != w[i]:  # inbound and same validation
                    return res
            res += c

        return res


# @lc code=end
print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
