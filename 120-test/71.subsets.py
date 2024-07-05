#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# Given an integer array nums of unique elements, return all possible subsets
# (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#
# Example 2:
#
#
# Input: nums = [0]
# Output: [[],[0]]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
#
#
#
from typing import List

# Key:
# base case is when the index is less than the len of nums
# use nums[i] appending
# shallow copy

# O(n * 2 ^ n)
# read: ds_algo\Fundamentals\subset-dryrun.py
# for details


# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, subset):
            res.append(subset.copy())

            for j in range(i, len(nums)):
                dfs(j + 1, subset + [nums[j]])

        dfs(0, [])

        return res


# @lc code=end

print(Solution().subsets([1, 2, 3]))


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, subset):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1, subset)

            subset.pop()
            dfs(i + 1, subset)

        dfs(0, [])
        return res
