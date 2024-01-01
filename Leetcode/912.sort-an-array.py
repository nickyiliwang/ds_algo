#
# @lc app=leetcode id=912 lang=python
#
# [912] Sort an Array
#
# https://leetcode.com/problems/sort-an-array/description/
#
# algorithms
# Medium (57.35%)
# Likes:    5750
# Dislikes: 726
# Total Accepted:    544K
# Total Submissions: 949.1K
# Testcase Example:  '[5,2,3,1]'
#
# Given an array of integers nums, sort the array in ascending order and return
# it.
#
# You must solve the problem without using any built-in functions in O(nlog(n))
# time complexity and with the smallest space complexity possible.
#
#
# Example 1:
#
#
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not
# changed (for example, 2 and 3), while the positions of other numbers are
# changed (for example, 1 and 5).
#
#
# Example 2:
#
#
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5 * 10^4
# -5 * 10^4 <= nums[i] <= 5 * 10^4
#
#
#

# @lc code=start

from typing import *


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2
                left_arr = arr[:mid]
                right_arr = arr[mid:]

                mergeSort(left_arr)
                mergeSort(right_arr)

                # merging
                left_idx = 0
                right_idx = 0
                merged_idx = 0

                # Loop till one or both arr is empty
                while left_idx < len(left_arr) and right_idx < len(right_arr):
                    if left_arr[left_idx] < right_arr[right_idx]:
                        arr[merged_idx] = left_arr[left_idx]
                        left_idx += 1
                    else:
                        arr[merged_idx] = right_arr[right_idx]
                        right_idx += 1

                    merged_idx += 1

                while left_idx < len(left_arr):
                    arr[merged_idx] = left_arr[left_idx]
                    left_idx += 1
                    merged_idx += 1

                while right_idx < len(right_arr):
                    arr[merged_idx] = right_arr[right_idx]
                    right_idx += 1
                    merged_idx += 1

            return arr

        return mergeSort(nums)


# @lc code=end

print(Solution.sortArray("", [0]))
