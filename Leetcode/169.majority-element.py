#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (63.82%)
# Likes:    17713
# Dislikes: 538
# Total Accepted:    2.3M
# Total Submissions: 3.6M
# Testcase Example:  '[3,2,3]'
#
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You
# may assume that the majority element always exists in the array.
#
#
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
#
#
#
# Follow-up: Could you solve the problem in linear time and in O(1) space?
#


# @lc code=start


# O(n) Time O(1) Space
# Logic
# Increment if we meet the same number
# if count reach 0 we switch res to new number
# Decrement if the number we meet in the loop isn't the res
# Most repeated number eventually win out.
# Assuming that the majority element always exists.
class Solution(object):
    def majorityElement(self, nums):
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n

            count += 1 if n == res else -1

        return res


# @lc code=end

Solution.majorityElement("", [2, 2, 1, 1, 1, 2, 2])


# O(n) solution
class Solution(object):
    def majorityElement(self, nums):
        counter = {}
        max_num = None
        max_count = -1

        for n in nums:
            counter[n] = counter.get(n, 1) + 1

        for key in counter:
            if counter[key] > max_count:
                max_num = key
                max_count = counter[key]

        return max_num
