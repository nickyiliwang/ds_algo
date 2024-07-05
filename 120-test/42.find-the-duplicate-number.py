#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number/description/
#
# Given an array of integers nums containing n + 1 integers where each integer
# is in the range [1, n] inclusive.
#
# There is only one repeated number in nums, return this repeated number.
#
# You must solve the problem without modifying the array nums and uses only
# constant extra space.
#
#
# Example 1:
#
#
# Input: nums = [1,3,4,2,2]
# Output: 2
#
#
# Example 2:
#
#
# Input: nums = [3,1,3,4,2]
# Output: 3
#
#
# Example 3:
#
#
# Input: nums = [3,3,3,3,3]
# Output: 3
#
#
# Constraints:
#
#
# 1 <= n <= 10^5
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer
# which appears two or more times.
#
#
#
# Follow up:
#
#
# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem in linear runtime complexity?
#
#
#
from typing import List

# Key:
# Using slow and fast pointer to find the node before the beginning of the loop, which is somewhere slow and fast intersect
# Using another slow2 pointer to find the point of loop


# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow


# @lc code=end
