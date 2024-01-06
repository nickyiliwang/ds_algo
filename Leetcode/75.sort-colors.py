#
# @lc app=leetcode id=75 lang=python
#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
#
# algorithms
# Medium (61.03%)
# Likes:    17261
# Dislikes: 602
# Total Accepted:    1.7M
# Total Submissions: 2.8M
# Testcase Example:  '[2,0,2,1,1,0]'
#
# Given an array nums with n objects colored red, white, or blue, sort them
# in-place so that objects of the same color are adjacent, with the colors in
# the order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the color red, white, and
# blue, respectively.
#
# You must solve this problem without using the library's sort function.
#
#
# Example 1:
#
#
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
#
#
# Example 2:
#
#
# Input: nums = [2,0,1]
# Output: [0,1,2]
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
#
#
#
# Follow up: Could you come up with a one-pass algorithm using only constant
# extra space?
#
#


# @lc code=start
class Solution(object):
    def sortColors(self, nums):
        l, r = 0, len(nums) - 1
        i = 0

        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                # moving i pointer here will introduce 0 into middle
            else:  # encountered 1
                i += 1


# @lc code=end

print(Solution.sortColors("", [2, 0, 2, 1, 1, 0]))

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# # Bucket Sort:
# def sortColors(self, nums):
#     buckets = [[] for i in range(3)]
#     for n in nums:
#         buckets[n].append(n)
#     return [n for bucket in buckets for n in bucket]


# Insertion sort
# class Solution(object):
#     def sortColors(self, nums):
#         for i in range(1, len(nums)):
#             curr = nums[i]
#             j = i - 1

#             while j >= 0 and nums[j] > curr:
#                 nums[j + 1] = nums[j]
#                 j -= 1

#             nums[j + 1] = curr

#         return nums


# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_arr, right_arr = arr[:mid], arr[mid:]

#         merge_sort(left_arr)
#         merge_sort(right_arr)

#         left_idx = 0
#         right_idx = 0
#         merged_idx = 0

#         while left_idx < len(left_arr) and right_idx < len(right_arr):
#             if left_arr[left_idx] < right_arr[right_idx]:
#                 arr[merged_idx] = left_arr[left_idx]
#                 left_idx += 1
#             else:
#                 arr[merged_idx] = right_arr[right_idx]
#                 right_idx += 1

#             merged_idx += 1

#         while left_idx < len(left_arr):
#             arr[merged_idx] = left_arr[left_idx]
#             left_idx += 1
#             merged_idx += 1

#         while right_idx < len(right_arr):
#             arr[merged_idx] = right_arr[right_idx]
#             right_idx += 1
#             merged_idx += 1

#     return arr
