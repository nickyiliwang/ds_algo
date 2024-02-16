#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (76.98%)
# Likes:    16475
# Dislikes: 255
# Total Accepted:    1.7M
# Total Submissions: 2.3M
# Testcase Example:  '[1,2,3]'
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


# 6/10 cases passed
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i, n in enumerate(nums):
            j = i
            while j <= len(nums):
                res.add(tuple(nums[i:j]))
                if j < len(nums) and i != j:
                    res.add(tuple((nums[i], nums[j])))
                j += 1

        return list([list(tup) for tup in res])


# @lc code=end

print(Solution().subsets([1, 2, 3]))
