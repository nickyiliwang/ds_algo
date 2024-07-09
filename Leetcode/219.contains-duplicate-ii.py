#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (45.72%)
# Likes:    6115
# Dislikes: 3092
# Total Accepted:    981.8K
# Total Submissions: 2.1M
# Testcase Example:  '[1,2,3,1]\n3'
#
# Given an integer array nums and an integer k, return true if there are two
# distinct indices i and j in the array such that nums[i] == nums[j] and abs(i
# - j) <= k.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1], k = 3
# Output: true
#
#
# Example 2:
#
#
# Input: nums = [1,0,1,1], k = 1
# Output: true
#
#
# Example 3:
#
#
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 0 <= k <= 10^5
#
#
#

from typing import List


# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited = {}
        res = False

        for i, n in enumerate(nums):
            if n not in visited:
                visited[n] = i
            else:
                if abs(i - visited[n]) <= k:
                    res = True
                else: # need to update dup position again even if the above condition failed
                    visited[n] = i
        return res


# @lc code=end
print(Solution().containsNearbyDuplicate([1, 0, 1, 1], 1))
