#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# Given an integer array nums, find a subarray that has the largest product,
# and return the product.
#
# The test cases are generated so that the answer will fit in a 32-bit
# integer.
#
#
# Example 1:
#
#
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
#
# Example 2:
#
#
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
#
#

# Key
# keep a max and min
# during the loop update the max/min/res
# need a tmp to keep max in memory

from typing import List


# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax, currMin = 1, 1

        for n in nums:
            tmp = currMax

            currMax = max(n, n * currMax, n * currMin)
            currMin = min(n, n * tmp, n * currMin)
            res = max(res, currMax, currMin)

        return res


# @lc code=end

print(Solution().maxProduct([-2, 3, 4]))
