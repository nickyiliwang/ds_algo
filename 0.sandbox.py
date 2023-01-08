if (0 > -1):
    print("0 is bigger than -1")

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
