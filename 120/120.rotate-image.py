#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
# https://leetcode.com/problems/rotate-image/description/
#
# You are given an n x n 2D matrix representing an image, rotate the image by
# 90 degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the
# input 2D matrix directly. DO NOT allocate another 2D matrix and do the
# rotation.
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
#
#
# Example 2:
#
#
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
#
#
#
# Constraints:
#
#
# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000
#
#
#
from typing import List

# Transpose the matrix by swapping elements along the main diagonal, then symmetrically flip it for the desired rotation.

# 1  2  3             
# 4  5  6
# 7  8  9

# After swap, it will be swap(matrix[i][j], matrix[j][i])

# 1  4  7
# 2  5  8
# 3  6  9

# Then flip the matrix horizontally. (swap(matrix[i][j], matrix[i][matrix.length-1-j])
# 7  4  1
# 8  5  2
# 9  6  3

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        def swap(m):
            for r in range(n):
                for c in range(r):
                    m[r][c], m[c][r] = m[c][r], m[r][c]

        def reverse(m):
            for row in range(n):
                l, r = 0, n - 1

                while l < r:
                    m[row][l], m[row][r] = m[row][r], m[row][l]
                    l += 1
                    r -= 1

        swap(matrix)
        reverse(matrix)


# @lc code=end
print(
    Solution().rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
)
