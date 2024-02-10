#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (72.32%)
# Likes:    15979
# Dislikes: 679
# Total Accepted:    2.6M
# Total Submissions: 3.6M
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers nums, every element appears twice except
# for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only
# constant extra space.
#
#
# Example 1:
# Input: nums = [2,2,1]
# Output: 1
# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:
# Input: nums = [1]
# Output: 1
#
#
# Constraints:
#
#
# 1 <= nums.length <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^4
# Each element in the array appears twice except for one element which appears
# only once.
#
#
#
from typing import List


# ^ is the XOR operant in python

# XOR, short for Exclusive OR, is a logical operation that takes two binary inputs and returns true (1) if exactly one of the inputs is true, and false (0) otherwise. In other words, XOR returns true if the inputs are different, and false if they are the same.

# Input A	Input B	    Output
# 0	        0	        0
# 0	        1	        1
# 1	        0	        1
# 1	        1	        0


# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            res ^= n

        return res


# @lc code=end

print(Solution().singleNumber([2, 2, 1]))


# Non binary solution
def singleNumber(self, nums: List[int]) -> int:
    validator = set()

    for n in nums:
        if n in validator:
            validator.remove(n)
        else:
            validator.add(n)

    return list(validator)[0]
