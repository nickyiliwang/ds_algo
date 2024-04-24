#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# Given an m x n integer matrix matrix, if an element is 0, set its entire row
# and column to 0's.
#
# You must do it in place.
#
#
# Example 1:
#
#
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
#
#
# Example 2:
#
#
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -2^31 <= matrix[i][j] <= 2^31 - 1
#
#
#
# Follow up:
#
#
# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best
# solution.
# Could you devise a constant space solution?
#
#
#
from typing import List


# Key:
# Keeping the row and col zero tracking array in the matrix
# to avoid overlap we need O(1) space to know if the firstRow is Zero
#


# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix[0])
        rowBound, colBound = range(row), range(col)
        firstRowZero = False

        for r in rowBound:
            for c in colBound:
                if matrix[r][c] == 0:
                    # Rows
                    if r == 0:
                        firstRowZero = True
                    else:
                        matrix[r][0] = 0

                    # Cols
                    matrix[0][c] = 0

        # fix (1 , 1) and beyond
        for r in range(1, row):
            for c in range(1, col):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # fix (0, 0)
        if matrix[0][0] == 0:
            for r in rowBound:
                matrix[r][0] = 0

        if firstRowZero:
            for c in colBound:
                matrix[0][c] = 0


# @lc code=end


# intuitive but less efficient
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowBound, colBound = range(len(matrix)), range(len(matrix[0]))
        q = []

        def makeZeros(r, c):
            for i in rowBound:
                matrix[i][c] = 0

            for j in colBound:
                matrix[r][j] = 0

        for r in rowBound:
            for c in colBound:
                if matrix[r][c] == 0:
                    q.append((r, c))

        for r, c in q:
            makeZeros(r, c)
