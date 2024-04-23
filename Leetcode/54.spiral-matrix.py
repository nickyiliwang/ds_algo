#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
# 
# 
#
from typing import List

# Key:
# by keeping a directional while going a spiral
# before we get all the result, in this case the res will be the same as the number of numbers in the grid
# each while iteration goes deeper into the grid
# top + 1, right ↓, bottom ↑, left + 1
# m[direction][i] means row bound ops, m[i][direction] colBound

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, row - 1, 0, col - 1
        result = []
        
        while len(result) < row * col:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
                
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])    
                left += 1
        
        return result
            
            
        
# @lc code=end

print(
    Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
)