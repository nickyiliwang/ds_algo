from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    left, right = 0, len(matrix) - 1
    res = []

    while left <= right:
        mid = (left + right) // 2

        if matrix[mid][0] > target:
            right = mid - 1
        elif matrix[mid][-1] < target:
            left = mid + 1
        else:
            res = matrix[mid]
            break

    left, right = 0, len(res) - 1

    while left <= right:
        mid = (left + right) // 2

        if res[mid] > target:
            right = mid - 1
        elif res[mid] < target:
            left = mid + 1
        else:
            return True
    return False


print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))

# my old solution

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
