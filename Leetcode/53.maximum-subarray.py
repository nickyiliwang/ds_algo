#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Medium (50.57%)
# Likes:    33139
# Dislikes: 1391
# Total Accepted:    3.7M
# Total Submissions: 7.3M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the subarray with the largest sum, and
# return its sum.
#
#
# Example 1:
#
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
#
#
# Example 2:
#
#
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
#
#
# Example 3:
#
#
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#
# Follow up: If you have figured out the O(n) solution, try coding another
# solution using the divide and conquer approach, which is more subtle.
#
#
from typing import List


# @lc code=start
# O(N)
# Think of as sliding window
# Left will reset to the right pointer if there is a negative number
# left is the current sum
# res is the max sum


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        left = 0

        for right in nums:
            if left < 0:
                left = 0

            left += right

            res = max(res, left)

        return res


# @lc code=end

# Explanation
# Doing this we can go from O(n ^ 3) to calculate every sub array's max sum

# But doing this we can ignore any current sum that results in a negative number. the first number as the result will help filter out any current number that's not bigger than result. (using max)

print(Solution().maxSubArray([5, 4, -1, 7, 8]))
