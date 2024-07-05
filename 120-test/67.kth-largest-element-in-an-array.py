#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
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

from typing import List
import heapq

# min heap
# add/pop logN
# min val in O(1)

# Add: m * logN


# min heap of size k

# k = 2
# minHeap = [1,2,3,4,5,6]
# keep popping the lowest val till len(minHeap) == k
# minHeap = [5,6]
# 5 is lowest currently


# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = nums
        heapq.heapify(minHeap)
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        return minHeap[0]


# @lc code=end
