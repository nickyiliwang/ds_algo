#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sum to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note: The solution set must not contain duplicate combinations.
#
#
# Example 1:
#
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,5,2,1,2], target = 5
# Output:
# [
# [1,2,2],
# [5]
# ]
#
#
#
# Constraints:
#
#
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
#
#
#

from typing import List

# Key:
# same as subset II, we don't want duplicated numbers in the recursion
# if j > i and candidates[j] == candidates[j - 1]:
# will skip all duplicate numbers


# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, subset, total):
            if total == target:
                res.append(subset)
                return
            elif total > target:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                dfs(j + 1, subset + [candidates[j]], total + candidates[j])

        dfs(0, [], 0)

        return res


# @lc code=end
