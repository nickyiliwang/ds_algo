#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
#
# Given an integer array nums, return an array answer such that answer[i] is
# equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
#
# You must write an algorithm that runs in O(n) time and without using the
# division operation.
#
#
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#
#
# Constraints:
#
#
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
#
#
#
# Follow up: Can you solve the problem in O(1) extra space complexity? (The
# output array does not count as extra space for space complexity analysis.)
#
#
from typing import *
from collections import *

# Time:
# Space:

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

# @lc code=end
print(Solution().productExceptSelf([1, 2, 3, 4]))

# nums: [1,2,3,4]
# prefix: [1,1,2,6] 24 [1, 2, 3, 4]
# postfix: [24,12,4,1] 1 [1, 2, 3, 4]
# res: [24, 12, 8, 6]

# chars: [a, b, c, d]
# prefix: -> | a | a*b | a*b*c | a*b*c*d |
# postfix: <- | a*b*c*d | b*c*d | c*d | d |

# res[i] = prefix[i - 1] * postfix[i + 1]
