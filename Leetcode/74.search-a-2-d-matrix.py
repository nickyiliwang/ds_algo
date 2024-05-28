#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (50.20%)
# Likes:    15535
# Dislikes: 412
# Total Accepted:    1.8M
# Total Submissions: 3.6M
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3'
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


# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # bottom left start
        row, col = len(matrix) - 1, 0

        # since its sorted, we know that up will decrease the search and right will increase the value
        while row >= 0 and col < len(matrix[0]):
            if matrix[row][col] < target:
                col += 1
            elif matrix[row][col] > target:
                row -= 1
            else:
                return True
        return False


# @lc code=end
