#
# @lc app=leetcode id=1189 lang=python
#
# [1189] Maximum Number of Balloons
#
# https://leetcode.com/problems/maximum-number-of-balloons/description/
#
# algorithms
# Easy (60.07%)
# Likes:    1631
# Dislikes: 93
# Total Accepted:    180.9K
# Total Submissions: 301.2K
# Testcase Example:  '"nlaebolko"'
#
# Given a string text, you want to use the characters of text to form as many
# instances of the word "balloon" as possible.
#
# You can use each character in text at most once. Return the maximum number of
# instances that can be formed.
#
#
# Example 1:
#
#
#
#
# Input: text = "nlaebolko"
# Output: 1
#
#
# Example 2:
#
#
#
#
# Input: text = "loonbalxballpoon"
# Output: 2
#
#
# Example 3:
#
#
# Input: text = "leetcode"
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= text.length <= 10^4
# text consists of lower case English letters only.
#
#
#


import math


# @lc code=start
class Solution(object):
    def maxNumberOfBalloons(self, text):
        counter = {}
        for char in text:
            if char in "balloon":
                counter[char] = counter.get(char, 0) + 1

        if len(counter.values()) == 5:
            counter["l"] = counter["l"] // 2
            counter["o"] = counter["o"] // 2

            return min(counter.values())
        return 0


# @lc code=end
print(Solution.maxNumberOfBalloons("", "balon"))
