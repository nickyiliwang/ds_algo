#

# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# You are given an integer array nums. You are initially positioned at the
# array's first index, and each element in the array represents your maximum
# jump length at that position.
#
# Return true if you can reach the last index, or false otherwise.
#
#
# Example 1:
#
#
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#
# Example 2:
#
#
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
# jump length is 0, which makes it impossible to reach the last index.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^5
#
#
#

# Key:
# Greedy and moving the goal post

# @lc code=start
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False


# @lc code=end

print(Solution().canJump([2, 3, 1, 1, 4]))


# DP Solution
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False for _ in range(len(nums))]
        dp[0] = True

        for i in range(len(nums)):
            if dp[i]:
                for j in range(i + 1, i + nums[i] + 1):
                    if j < len(nums):
                        dp[j] = True
                    if j == len(nums) - 1:
                        return True

        return dp[len(nums) - 1]
