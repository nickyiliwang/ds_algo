#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# Given an integer array nums, return the length of the longest strictly
# increasing subsequence.
#
#
# Example 1:
#
#
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4.
#
#
# Example 2:
#
#
# Input: nums = [0,1,0,3,2,3]
# Output: 4
#
#
# Example 3:
#
#
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4
#
#
#
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time
# complexity?
#
#

from typing import List

# Key
# If nums[i] is bigger than any nums[j] (all previous numbers)
# We need to update dp[i], while comparing to dp[j] + 1

# Time: O(n ^ 2) Space: O(n)
# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


# @lc code=end

print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
# Output: 4


# Can detect continuous increasing sub-array
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        bound = range(len(nums))
        i = 0
        res = 0

        while i in bound:
            j = i + 1
            temp = 1
            tempMax = nums[i]
            while j in bound and nums[j] > tempMax:
                temp += 1
                tempMax = nums[j]
                j += 1
            i = j
            res = max(res, temp)

        return res
