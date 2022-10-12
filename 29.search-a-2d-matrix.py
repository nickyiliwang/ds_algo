# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.


# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false


# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

from typing import List

# my solution
# Very good

# def searchMatrix(matrix: List[List[int]], target: int) -> bool:
#     # get the index as soon as you find a number that's bigger than the target, meaning this array might contain the number
#     def getIndex(m):
#         for i, l in enumerate(m):
#             if (l[-1] >= target):
#                 return i
#         return 0

#     # binary search with pointers
#     res = False
#     index = getIndex(matrix)
#     list = matrix[index]
#     left = 0
#     right = len(list) - 1
#     while left <= right:
#         middle = (left + right) // 2
#         if (list[middle] == target):
#             res = True
#         if (list[middle] < target):
#             left += 1
#         else:
#             right -= 1
#     print(res)
#     return res


# matrix = [[1], [3]]
# target = 3
# searchMatrix(matrix, target)

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    ROWS, COLS = len(matrix), len(matrix[0])
    top, bot = 0, ROWS - 1

    while top <= bot:
        # middle point
        row = (top + bot) // 2
        # if the target is bigger than the mid row's last number
        # need to increase the top pointer
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        # target falls into the current row
        # break out
        else:
            break

    row = (top + bot) // 2
    l, r = 0, COLS - 1
    while l <= r:
        m = (l + r) // 2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True
    return False


matrix = [[1], [3]]
target = 3
searchMatrix(matrix, target)
