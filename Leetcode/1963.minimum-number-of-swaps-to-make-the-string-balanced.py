#
# @lc app=leetcode id=1963 lang=python3
#
# [1963] Minimum Number of Swaps to Make the String Balanced
#
# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/
#
# algorithms
# Medium (70.99%)
# Likes:    1715
# Dislikes: 69
# Total Accepted:    65.3K
# Total Submissions: 91.9K
# Testcase Example:  '"][]["'
#
# You are given a 0-indexed string s of even length n. The string consists of
# exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.
#
# A string is called balanced if and only if:
#
#
# It is the empty string, or
# It can be written as AB, where both A and B are balanced strings, or
# It can be written as [C], where C is a balanced string.
#
#
# You may swap the brackets at any two indices any number of times.
#
# Return the minimum number of swaps to make s balanced.
#
#
# Example 1:
#
#
# Input: s = "][]["
# Output: 1
# Explanation: You can make the string balanced by swapping index 0 with index
# 3.
# The resulting string is "[[]]".
#
#
# Example 2:
#
#
# Input: s = "]]][[["
# Output: 2
# Explanation: You can do the following to make the string balanced:
# - Swap index 0 with index 4. s = "[]][][".
# - Swap index 1 with index 5. s = "[[][]]".
# The resulting string is "[[][]]".
#
#
# Example 3:
#
#
# Input: s = "[]"
# Output: 0
# Explanation: The string is already balanced.
#
#
#
# Constraints:
#
#
# n == s.length
# 2 <= n <= 10^6
# n is even.
# s[i] is either '[' or ']'.
# The number of opening brackets '[' equals n / 2, and the number of closing
# brackets ']' equals n / 2.
#
#
#

# Trick question
# Each operation can potentially remove 2 closing brackets
# ]]] => []] 3 closing to one closing in a single swap


# @lc code=start
class Solution:
    def minSwaps(self, s: str) -> int:
        extraClose = 0
        maxClose = 0

        for b in s:
            if b == "]":
                extraClose += 1
                maxClose = max(maxClose, extraClose)
            else:
                extraClose -= 1

        return (maxClose + 1) // 2


# @lc code=end

print(Solution().minSwaps("]]][[["))


# Counted brackets
class Solution:
    def minSwaps(self, s: str) -> int:
        res = 0
        stack = []
        valid = {"]": "["}

        for b in s:
            print(b)
            if b in valid:
                stack.append(b)
            elif len(stack) > 0:
                stack.pop()
                res += 1

        return res
