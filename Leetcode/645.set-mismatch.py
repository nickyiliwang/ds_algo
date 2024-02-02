#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#
# https://leetcode.com/problems/set-mismatch/description/
#
# algorithms
# Easy (44.58%)
# Likes:    4559
# Dislikes: 1119
# Total Accepted:    420.7K
# Total Submissions: 943.1K
# Testcase Example:  '[1,2,2,4]'
#
# You have a set of integers s, which originally contains all the numbers from
# 1 to n. Unfortunately, due to some error, one of the numbers in s got
# duplicated to another number in the set, which results in repetition of one
# number and loss of another number.
#
# You are given an integer array nums representing the data status of this set
# after the error.
#
# Find the number that occurs twice and the number that is missing and return
# them in the form of an array.
#
#
# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:
# Input: nums = [1,1]
# Output: [1,2]
#
#
# Constraints:
#
#
# 2 <= nums.length <= 10^4
# 1 <= nums[i] <= 10^4
#
#
#
from typing import *

# WIP
# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        pointer = 1
        while pointer <= len(nums):
            number = nums[pointer - 1]

            if number > pointer:
                nums = [pointer - 1, pointer]
            else:
                nums = [pointer, pointer - 1]

            pointer += 1
        return nums


# @lc code=end

# Input: nums = [1,1]
# Output: [1,2]
print(Solution.findErrorNums("", [1, 2, 2, 4]))
