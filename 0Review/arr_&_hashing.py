from typing import *
from collections import *


# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         rows = defaultdict(set)
#         cols = defaultdict(set)
#         squares = defaultdict(set)

#         for r in range(9):
#             for c in range(9):
#                 if board[r][c] == ".":
#                     continue
#                 if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]:
#                     return False

#                 rows[r].add(board[r][c])
#                 cols[c].add(board[r][c])
#                 squares[(r // 3, c // 3)].add(board[r][c])

#         return True


# board = [[".", ".", "4", ".", ".", ".", "6", "3", "."],
#          [".", ".", ".", ".", ".", ".", ".", ".", "."],
#          ["5", ".", ".", ".", ".", ".", ".", "9", "."],
#          [".", ".", ".", "5", "6", ".", ".", ".", "."],
#          ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
#          [".", ".", ".", "7", ".", ".", ".", ".", "."],
#          [".", ".", ".", "5", ".", ".", ".", ".", "."],
#          [".", ".", ".", ".", ".", ".", ".", ".", "."],
#          [".", ".", ".", ".", ".", ".", ".", ".", "."]]
# # expected to be true
# print(Solution.isValidSudoku("", board)
#       )

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         res = [1] * len(nums)
#         prefix = 1

#         # not this
#         # for i, n in enumerate(nums):
#         #     res[i] = n * prefix
#         #     prefix *= n

#         for i in range(len(nums)):
#             res[i] = prefix
#             prefix *= nums[i]

#         # res/prefix is [1, 1, 2, 6]

#         suffix = 1
#         for i in range(len(nums) - 1, -1, -1):
#             res[i] = suffix * res[i]
#             suffix *= nums[i]

#         return res


# print(
#     Solution.productExceptSelf("", [1, 2, 3, 4])
# )


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         c = Counter()
#         freq = [[] for i in range(len(nums) + 1)]
#         res = []

#         for n in nums:
#             c[n] += 1

#         for num, count in c.items():
#             freq[count].append(num)

#         for numbers in reversed(freq):
#             for n in numbers:
#                 res.append(n)
#                 if (len(res) == k):
#                     return res


# print(
#     Solution.topKFrequent("", [1, 1, 1, 2, 2, 3], 2)
# )

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = defaultdict(list)

#         for s in strs:
#             count = [0] * 26

#             for c in s:
#                 count[ord(c) - ord("a")] += 1

#             res[tuple(count)].append(s)
#         return res.values()


# print(
#     Solution.groupAnagrams("", ["eat", "tea", "tan", "ate", "nat", "bat"])
# )

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         hash = {}
#         for n in nums:
#             if hash.get(n) is not None:
#                 return True
#             else:
#                 hash[n] = 1
#         return False


# print(Solution.containsDuplicate("", [1, 2, 3, 1]))

# from collections import Counter

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         a, b = Counter(), Counter()

#         for c in s:
#             a[c] += 1

#         for c in t:
#             b[c] += 1

#         if a == b:
#             return True
#         else:
#             return False


# print(
#     Solution.isAnagram("", "anagram", "nagaram")
# )

# # Input: nums = [2,7,11,15], target = 9
# # Output: [0,1]
# # Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


# def two_sum(arr, tar):
#     hash = {}
#     res = []
#     for i, n in enumerate(arr):
#         if hash.get(tar - n) is not None:
#             res = [i, hash[tar - n]]
#         else:
#             hash[n] = i
#     return res


# print(two_sum([2, 7, 11, 15], 9))
