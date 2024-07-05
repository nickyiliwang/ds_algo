#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# You are given an m x n integer matrix matrix with the following two
# properties:
#
#
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the
# previous row.
#
#
# Given an integer target, return true if target is in matrix or false
# otherwise.
#
# You must write a solution in O(log(m * n)) time complexity.
#
#
# Example 1:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#
#
# Example 2:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4
#
#
#
from typing import List

# Key:
# you want the largest in the list to compare and adjust left, matrix[m][-1]
# and the smallest in the list to adjust for right, matrix[m][0]

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        nums = []

        while l <= r:
            m = (l + r) // 2

            if matrix[m][-1] < target:
                l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
            else:
                nums = matrix[m]
                break

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return True

        return False


# @lc code=end

