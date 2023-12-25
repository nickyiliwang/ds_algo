#
# @lc app=leetcode id=540 lang=python
#
# [540] Single Element in a Sorted Array
#
# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
#
# algorithms
# Medium (59.02%)
# Likes:    10602
# Dislikes: 166
# Total Accepted:    567K
# Total Submissions: 961.1K
# Testcase Example:  '[1,1,2,3,3,4,4,8,8]'
#
# You are given a sorted array consisting of only integers where every element
# appears exactly twice, except for one element which appears exactly once.
#
# Return the single element that appears only once.
#
# Your solution must run in O(log n) time and O(1) space.
#
#
# Example 1:
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^5
#
#
#


# @lc code=start
class Solution(object):
    def singleNonDuplicate(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if (mid % 2 == 1 and nums[mid - 1] == nums[mid]) or (
                mid % 2 == 0 and nums[mid + 1] == nums[mid]
            ):
                left = mid + 1
            else:
                right = mid

        print(nums[left], nums[right])
        return nums[right]


# @lc code=end

print(Solution.singleNonDuplicate("", [3, 3, 7, 7, 10, 11, 11]))

# EXPLANATION:-
# first element takes even position and second element takes odd position

# l < r instead of l <= r to ensure that the loop terminates correctly when the single non-duplicate element is found

# when the loop terminates, left and right have converged to the same index

# Part 1:
#   because of indexing. [0,1,2,3] => even numbers odd index
# 	if mid is odd, then it's duplicate should be in previous index.
#   if mid is even, then it's duplicate should be in next index.
# 	if any of the conditions is satisfied then pattern is not missed

# Part 2
# 	so check in next half of the array. i.e, left = mid + 1
# 	if condition is not satisfied, then the pattern is missed.
# 	so, single number must be before mid.
# 	so, update end to mid.

# Result:
# when the loop terminates, left and right have converged to the same index
# return the nums[left] or nums[right] doesn't matter


# My working solution:
class Solution(object):
    def singleNonDuplicate(self, nums):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if mid - 1 >= 0 and nums[mid - 1] == nums[mid]:
                if len(nums[left : mid - 1]) % 2 == 1:
                    left, right = left, mid - 2
                else:
                    left, right = mid + 1, right

            elif mid + 1 < len(nums) and nums[mid + 1] == nums[mid]:
                if len(nums[left:mid]) % 2 == 1:
                    left, right = left, mid - 1
                else:
                    left, right = mid + 2, right
            else:
                return nums[mid]

        return nums[mid]
