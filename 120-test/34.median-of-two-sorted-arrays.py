#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
#
#
# Example 1:
#
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#
#
# Example 2:
#
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
#
#
# Constraints:
#
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
#
#
#

from typing import *
from collections import *

# Time:
# Space:

# Key:
# start with the shorter arr for optimization
# find mid2 with: total // 2 - 2 - mid1
# find the left and right partition in the arr
#       n1Max = n1[mid1] if mid1 >= 0 else float("-inf")
#       n1Min = n1[mid1 + 1] if mid1 < l1 - 1 else float("inf")
# correct partition looks like:
#       n1Max <= n2Min and n2Max <= n1Min
# fix it by using n1Max > n2Min and adjusting the right pointer with mid1

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

# @lc code=end

print(Solution().findMedianSortedArrays([1, 3], [2]))
