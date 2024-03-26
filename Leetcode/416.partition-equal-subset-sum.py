#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (46.23%)
# Likes:    12006
# Dislikes: 235
# Total Accepted:    793.4K
# Total Submissions: 1.7M
# Testcase Example:  '[1,5,11,5]'
#
# Given an integer array nums, return true if you can partition the array into
# two subsets such that the sum of the elements in both subsets is equal or
# false otherwise.
#
#
# Example 1:
#
#
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
#
#
#

from typing import List

# O(n * sum(nums))

# Key
# 
# for j in range(target, n - 1, -1):
#     dp[j] = dp[j] or dp[j - n]
# we are finding if the sub problem of j - n can become 0
# if j - n is 0 let's say: 1 - 1, then dp[j] => dp[1] becomes True
# the next time if dp[6 - 5] (j - n) => dp[1] will be True, then dp[6] is also True 
# 
# # @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for n in nums:
            for j in range(target, n - 1, -1):
                dp[j] = dp[j] or dp[j - n]
        return dp[target]


# @lc code=end

print(Solution().canPartition([1, 5, 11, 5]))
