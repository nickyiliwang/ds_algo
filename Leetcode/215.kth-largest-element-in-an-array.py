#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (66.76%)
# Likes:    16845
# Dislikes: 860
# Total Accepted:    2.3M
# Total Submissions: 3.4M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Given an integer array nums and an integer k, return the k^th largest element
# in the array.
#
# Note that it is the k^th largest element in the sorted order, not the k^th
# distinct element.
#
# Can you solve it without sorting?
#
#
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
#
#
# Constraints:
#
#
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#
import heapq


# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(arr, l, r):
            pivot = arr[r]  # last element in the arr usually
            i = l
            for j in range(l, r):
                if arr[j] <= pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            # final swap after partition is done
            arr[i], arr[r] = arr[r], arr[i]
            return i

        l, r = 0, len(nums) - 1
        pivot = partition(nums, l, r)

        if pivot == k - 1:
            return nums[pivot]

        if pivot > k - 1:
            return self.findKthLargest(nums, l, pivot - 1, k)
        else:
            return self.findKthLargest(nums, l, pivot + 1, k)


# @lc code=end
