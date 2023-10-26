#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (37.99%)
# Likes:    26534
# Dislikes: 2912
# Total Accepted:    2.2M
# Total Submissions: 5.8M
# Testcase Example:  '[1,3]\n[2]'
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

# @lc code=start
from typing import *


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2 - 2

        if (len(A) > len(B)):
            A, B = nums2, nums1

        left, right = 0, len(A) - 1

        while True:
            A_Mid = (left + right) // 2
            B_Mid = half - A_Mid

            # ALeft -inf [{Left can be out}Mid{Right can be out of bound}] +inf A_Right
            A_Left = A[A_Mid] if A_Mid >= 0 else float("-inf")
            A_Right = A[A_Mid + 1] if A_Mid < len(A) - 1 else float("inf")

            B_Left = B[B_Mid] if B_Mid >= 0 else float("-inf")
            B_Right = B[B_Mid + 1] if B_Mid < len(B) - 1 else float("inf")

            if A_Left <= B_Right and B_Left <= A_Right:
                if (total % 2 == 0):
                    # A [Left[3]] [[5]Right]
                    # B [Left[4]] [[6]Right]
                    return (max(A_Left, B_Left) + min(A_Right, B_Right)) / 2
                else:
                    return min(A_Right, B_Right)
            elif (A_Left > B_Right):
                right = A_Mid - 1
            else:
                left = A_Mid + 1


nums1 = [1, 2, 3, 4]
nums2 = [3, 4, 4, 5, 5, 6, 7, 8]

print(Solution.findMedianSortedArrays("", nums1, nums2))
# @lc code=end
