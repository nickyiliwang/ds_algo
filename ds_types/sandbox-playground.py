num = "-12"

print(type(int("=") == int))
print(type(-12) == int)

# def fib(n, memo={}):
#     if n in memo:
#         return memo[n]
#     if n <= 2:
#         return 1

#     memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
#     return memo[n]


# print(fib(50))

# print(3 // 2)

# hey = {}

# hey["hi"] = 1

# print(hey)

# from linked_list import LinkedList


# def function():
#     linked_list = LinkedList()

#     linked_list.append(1)
#     linked_list.append(2)
#     linked_list.append(3)
#     linked_list.append(4)
#     linked_list.append(5)

#     curr = linked_list.head.next
#     while curr.next:
#         if curr.next.val == 6:
#             curr.next = curr.next.next
#             linked_list.display()
#             return
#         curr = curr.next


# function()

# print(100004 % 1000)

# print(len([1, 2, 3, 4, 5, 6, 7, 8]) - 1 // 2)

# while True:
#     print('1')
#     break

# def search(nums, target):
#     left, right = 0, len(nums) - 1

#     def bs(left, right):
#         while left <= right:
#             mid = (left + right) // 2

#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] > target:
#                 right = right - 1
#             else:
#                 left = left + 1

#         return -1

#     # no rotation
#     if nums[left] < nums[right]:
#         return bs(left, right)

#     while left <= right:
#         mid = (left + right) // 2

#         if nums[mid] == target:
#             return mid
#         elif nums[mid] > nums[right]:
#             left = mid + 1
#             return bs(left, right)
#         else:
#             right = mid - 1
#             return bs(left, right)


# print(search([3, 5, 1], 3))

# from typing import List

# def searchMatrix(matrix: List[List[int]], target: int) -> bool:
#     left, right = 0, len(matrix) - 1
#     res = []

#     while left <= right:
#         mid = (left + right) // 2

#         if matrix[mid][0] > target:
#             right = mid - 1
#         elif matrix[mid][-1] < target:
#             left = mid + 1
#         else:
#             res = matrix[mid]
#             break

#     left, right = 0, len(res) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if res[mid] > target:
#             right = mid - 1
#         elif res[mid] < target:
#             left = mid + 1
#         else:
#             return True
#     return False

# print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))

# def largestRectangleArea(heights):
#     heights.append(0)
#     stack = [-1]
#     res = 0
#     print(heights[-1])

#     for i, curr in enumerate(heights):
#         while heights[stack[-1]] > curr:
#             h = heights[stack.pop()]
#             w = i - stack[-1] - 1
#             res = max(res, h * w)

#         stack.append(i)

#     return res

# At each iteration, it checks if the current heights is less than the heights at the top of the stack.

# If it is, it pops the heights at the top of the stack and calculates the area of the rectangle represented by that heights and the width of the rectangle (which is the difference between the current index and the index at the top of the stack).

# It then updates the maximum area if the calculated area is greater than the previous maximum.

# Finally, it appends the current index to the stack and continues to the next iteration.

# The heights of 0 is appended to the end of the heights list to handle the case where the stack is not empty after the iterations.

# print(largestRectangleArea([1]))

# from collections import deque

# def dailyTemperatures(temperatures):
#     stack = deque()

#     res = [0] * len(temperatures)

#     for i, t in enumerate(temperatures):
#         while stack and temperatures[stack[-1]] < t:
#             position = stack.pop()
#             res[position] = i - position
#         stack.append(i)

#     return res

# dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])

# stack = deque([1, 2, 3, 4, 5])
# item = stack[-1]
# print(item)

# cut = nums[0:3]
# print(cut)

# nums = [1, 2, 3, 4, 5]

# print(nums[len(nums) - 1])

# for i in range(len(nums) - 1, -1, -1):
#     print(nums[i])

# for i in range(len(nums)):
# print(nums[i])

# count = [0] * 26
# print(count)

# if (0 > -1):
#     print("0 is bigger than -1")

# def minWindow(s, t):
#     if len(t) > len(s):
#         return ""

#     if t == "":
#         return ""

#     window, countT = {}, {}

#     for c in t:
#         countT[c] = countT.get(c, 0) + 1

#     have, need = 0, len(countT)

#     res, resLength = [-1, -1], float("inf")
#     left = 0

#     for right in range(len(s)):
#         c = s[right]
#         window[c] = window.get(c, 0) + 1

#         if c in countT and window[c] == countT[c]:
#             have += 1

#         while have == need:
#             if (right - left + 1) < resLength:
#                 res = [left, right]
#                 resLength = (right - left + 1)

#             window[s[left]] -= 1
#             if s[left] in counT and window[s[left]] < countT[s[left]]:
#                 have -= 1

#             left += 1

#     left, right = res
#     return s[left:right+1] if resLength != float("inf") else ""

# s = "ADOBECODEBANC"
# t = "ABC"
# minWindow(s, t)

# def generateParenthesis(n):
#     res = []

#     def backtracking(leftN, rightN, path):
#         # result and append
#         if leftN == n and rightN == n:
#             res.append(path)

#         # if left is higher than right we can add a right
#         if leftN > rightN:
#             backtracking(leftN, rightN + 1, path + ")")

#         if leftN < n:
#             backtracking(leftN + 1, rightN, path + "(")

#     backtracking(0, 0, "")

#     print(res)
#     return res

# generateParenthesis(3)
