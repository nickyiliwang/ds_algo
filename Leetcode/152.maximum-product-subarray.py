#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (34.99%)
# Likes:    18102
# Dislikes: 591
# Total Accepted:    1.2M
# Total Submissions: 3.5M
# Testcase Example:  '[2,3,-2,4]'
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
#
from typing import List


# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax, currMin = 1, 1

        for n in nums:
            # we want pre mutated val
            tempMax = currMax * n

            currMax = max(n, n * currMax, n * currMin)
            currMin = min(n, tempMax, n * currMin)
            res = max(res, currMax, currMin)

        return res


# @lc code=end

print(Solution().maxProduct([-2, 3, 4]))


# 109/190 cases passed (N/A)
# not considering 2 negative numbers becoming pos
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = [1] + nums
        res = float("-inf")
        for i in range(1, len(nums)):
            temp = nums[i - 1] * nums[i]
            nums[i] = max(temp, nums[i])
            res = max(res, nums[i])

        return res
