#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (77.95%)
# Likes:    18560
# Dislikes: 311
# Total Accepted:    2M
# Total Submissions: 2.5M
# Testcase Example:  '[1,2,3]'
#
# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.
#
#
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
#
#
#

from typing import List


# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        maxLength = len(nums)

        def dfs(i, subset):
            if len(subset) == maxLength:
                res.append(subset.copy())
                return

            for n in nums:
                if n in subset:
                    continue
                subset.append(n)
                dfs(i, subset)
                subset.pop()

        dfs(0, [])

        return res


# @lc code=end
print(Solution().permute([1, 2, 3]))
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
