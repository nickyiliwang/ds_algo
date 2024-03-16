#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Medium (50.88%)
# Likes:    20568
# Dislikes: 407
# Total Accepted:    2.1M
# Total Submissions: 4.2M
# Testcase Example:  '[1,2,3,1]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security systems
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the
# police.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
#
#
# Example 2:
#
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400
#
#
#
from typing import List


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        oneAway, twoAway = 0, 0

        for n in nums:
            temp = max(twoAway + n, oneAway)
            twoAway = oneAway
            oneAway = temp

        return oneAway


# @lc code=end

# print(Solution().rob([1, 2, 3, 1]))
print(Solution().rob([2, 7, 9, 3, 1]))

# You can't do this like min climbing stairs
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         for i in range(len(nums) - 3, -1, -1):
#             nums[i] += max(nums[i + 1], nums[i + 2])

#         return max(nums[0], nums[1])
