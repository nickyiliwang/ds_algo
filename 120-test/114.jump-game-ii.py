#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# You are given a 0-indexed array of integers nums of length n. You are
# initially positioned at nums[0].
#
# Each element nums[i] represents the maximum length of a forward jump from
# index i. In other words, if you are at nums[i], you can jump to any nums[i +
# j] where:
#
#
# 0 <= j <= nums[i] and
# i + j < n
#
#
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are
# generated such that you can reach nums[n - 1].
#
#
# Example 1:
#
#
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1
# step from index 0 to 1, then 3 steps to the last index.
#
#
# Example 2:
#
#
# Input: nums = [2,3,0,1,4]
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].
#
#
#

from typing import List

# Key:
# Implicit DFS with Greedy
#
# len(nums) - 1 is very important here, this means we are not reaching the last number in the index in the loop
# minJump will not increment if there is only one element in the list

# end will always try to be the far in the queue


# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        res, far, end = 0, 0, 0

        for i in range(n - 1):
            far = max(far, i + nums[i])
            if far >= n - 1:
                res += 1
                break
            if i == end:  # visited current level
                res += 1
                end = far  # make the next queue

        return res


# @lc code=end

print(Solution().jump([0]))


# DFS solution
# O(n^2)
# Less optimal but more understandable
class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i >= len(nums) - 1:  # out of bounds
                return 0
            if i in memo:
                return memo[i]

            minVal = float("inf")

            for j in range(i + 1, i + nums[i] + 1):
                minVal = min(minVal, dfs(j) + 1)

            memo[i] = minVal

            return memo[i]

        return dfs(0) if dfs(0) != float("inf") else False
