node = None
print(
    node.val
)

# data = [None, None, None]

# for data

# flip = True
# flip = not flip

# print(
#     flip
# )

# data = [1,2,3,4,5,6,7,8,9,10]
# res, idx  = float("inf"), 0

# while idx + 1 < len(data):
#     res = min(res, data[idx + 1] - data[idx])
#     idx += 1

# print(res)

# print(5**2)
# print(None + None)

# thing = []
# thing.append("haha")
# print(thing)

# cache = {
#     1: "hello",
#     2: "nick",
#     3: "wang",
# }

# del cache[1]


# print(cache)


# data = [1, 2, 3, 4]

# data.append([5, 5, 5, 5, 5, 5])
# data
# print(data + [5, 5, 5, 5, 5, 5])

# [1, 2, 3, 4, [5, 5, 5, 5, 5, 5], 5, 5, 5, 5, 5, 5]
# for i in range(len(data) - 1):
#     print(data[i], i)

# print(data[len(data)])
# length = len("123456")
# print(length)
# rangeBound = range(length)

# if 5 in rangeBound:
#     print("hi")

# print(range(5))

# dp = [True, False, True, False, False]

# dp[1] = dp[1] or dp[2]

# print(dp)

# data = "abcdefg"

# bound = range(len(data))

# print(len(data))
# print(bound)

# word = "hitman"

# print(word[:0] + "*" + word[0 + 1 :])

# from collections import deque
# from typing import List


# class Solution:
#     def walls_and_gates(self, rooms: List[List[int]]):
#         ROWS, COLS = len(rooms), len(rooms[0])
#         visit = set()
#         q = deque()

#         def addRooms(r, c):
#             if (
#                 min(r, c) < 0
#                 or r == ROWS
#                 or c == COLS
#                 or (r, c) in visit
#                 or rooms[r][c] == -1
#             ):
#                 return
#             visit.add((r, c))
#             q.append([r, c])

#         for r in range(ROWS):
#             for c in range(COLS):
#                 if rooms[r][c] == 0:
#                     q.append([r, c])
#                     visit.add((r, c))

#         dist = 0
#         while q:
#             for i in range(len(q)):
#                 r, c = q.popleft()
#                 rooms[r][c] = dist
#                 addRooms(r + 1, c)
#                 addRooms(r - 1, c)
#                 addRooms(r, c + 1)
#                 addRooms(r, c - 1)
#             dist += 1

#         return rooms


# print(
#     Solution().walls_and_gates(
#         [
#             [2147483647, -1, 0, 2147483647],
#             [2147483647, 2147483647, 2147483647, -1],
#             [2147483647, -1, 2147483647, -1],
#             [0, -1, 2147483647, 2147483647],
#         ]
#     )
# )


# stuff = [-8, -3, 2]


# def recur(i, lst):
#     if i == len(lst):
#         return None

#     value = recur(i + 1, lst)

#     if lst[i] % 2 != 0:
#         return value
#     if value == None:
#         return lst[i]

#     return lst[i] * value


# print(recur(0, stuff))


# n = 4
# res = "...."

# def dfs(i, r):
#     if i == n - 1:


# string = "abc"
# res = ""

# for n in range(len(string) - 1, -1, -1):
#     res += string[n]

# print(res)

# import heapq

# minHeap = [14, 35, 23, 523, 52, 5, 3, 2, 3, 4, 5]

# heapq.heapify(minHeap)

# print(3 % 2)

# data = set([1, 2, 3, 4, 5])

# data.add(1)
# data.remove(4)

# print(data)
# import heapq

# n = 2
# points = [8, 2, 21, 2, 23, 4, 1, 413, 3, 55, 4]

# heapq.heapify(points)

# res = []

# while len(points) > 0:
#     temp = []

#     for _ in range(n):
#         if len(points) > 0:
#             high = heapq.heappop(points)
#             high -= 1
#             if high != 0:
#                 temp.append(high)
#             res.append(high)
#         else:
#             res.append("idle")

#     for item in temp:
#         heapq.heappush(points, item)

# print(res)

# points = list(map(lambda n: n**2, points))

# print(points)

# heapq.heapify(nums)

# print(nums)

# print(31 // 4)
# print((31 - 1) // 4)

# nums = [17, 18, 19, 20, 21, 22, 23, 25, 26, 29]
# length = 3
# res = 0


# def xor_of_sequence(first, last):
#     if first % 2 == 0:
#         xor_pattern = [last, 1, last + 1, 0]
#     else:
#         xor_pattern = [first, first ^ last, first - 1, (first - 1) ^ last]

#     return xor_pattern[(last - first) % 4]


# for security_id in range(length):  # treat each 'row' as a sequence of numbers
#     first = 0 + (length * security_id)  # the first number in the row / sequence
#     last = first + (length - security_id) - 1  # the last number in the row / sequence
#     print(first, last)
#     res ^= xor_of_sequence(first, last)

# print(res)
# nums = [17, 18, "/", 19, 20, 21, 22, 23, 25, 26, 29]
# res = 0

# for n in nums:
#     res ^= n

# print(res)


# 17 18 19 20 /


# num = 20
# loop = 0

# print(loop, num >> 2)

# def recursive_function(value):
#     # Base case
#     if value == 0:
#         return 0

#     # Recursive case
#     print(value)  # Print the current value
#     return recursive_function(value - 1) + 1


# # Call the recursive function with an initial value of 5
# result = recursive_function(5)
# print(result)


# bucket = ["1", "2", "3"]
# # bucket = {"1": "value1", "2": "value2"}

# print(bucket.index("1"))

# num = int("10000", 3)

# print(num)

# s = "aaaaaaab"
# unique = set()
# for char in s:
#     unique.add(char)

# print("".join(list(unique)))

# class Solution:
#     def __init__(self):
#         self.root = "1"

#     def addWords(self, word):
#         curr = self
#         curr.root = word

#     def findWords(self, board, words):
#         self.addWords("word")
#         return "result"


# solution = Solution()
# print(solution.findWords("board", "words"))

# word = "HelLo"
# i = 3

# print(word[: i + 1])

# stuff = set([(0, 0), (1, 1)])

# stuff.add((2, 2))

# for r, l in stuff:
#     print(r, l)

# stuff = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
#     "d": 4,
#     "e": 5,
# }

# items = stuff.items()

# print(items) # dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])


# print(type(("toys", "books")))

# stuff = set()
# stuff.add(("toys", "books"))

# print(stuff)

# list = [1, 2, 3, 4, 5]
# left, right = 0, len(list) - 1
# sums = []

# while left < right:
#     sum = list[left] + list[right]
#     sums.append(sum)
#     left += 1
#     right -= 1

# print(sums)
# num = "-12"

# print(type(int("=") == int))
# print(type(-12) == int)

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
