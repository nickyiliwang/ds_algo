#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (56.97%)
# Likes:    9431
# Dislikes: 286
# Total Accepted:    862.7K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,2]'
#
# Given an integer array nums that may contain duplicates, return all possible
# subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
#
#
# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
#
#
#

from typing import List


# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        def dfs(i, subset):
            res.append(subset.copy())

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                dfs(j + 1, subset + [nums[j]])

        dfs(0, [])

        return res


# @lc code=end
print(Solution().subsetsWithDup([4, 4, 4, 1, 4]))


# More understandable way
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)  # nlogn
        res = []

        def dfs(i, subset):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()

            # we gotta keep the right leaf free from duplicates in order to not produce duplicated base cases.
            j = i

            while j < len(nums) and nums[j] == nums[i]:
                j += 1

            dfs(j, subset)

        dfs(0, [])

        return res
