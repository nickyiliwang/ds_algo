#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (66.83%)
# Likes:    16578
# Dislikes: 831
# Total Accepted:    2.1M
# Total Submissions: 3.2M
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
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val):
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]


# @lc code=end

solution = Solution(2, [3, 2, 1, 5, 6, 4])

print(solution.add(1))
