from collections import deque


def dailyTemperatures(temperatures):
    stack = deque()

    res = [0] * len(temperatures)

    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            position = stack.pop()
            res[position] = i - position
        stack.append(i)

    return res


dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])

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
