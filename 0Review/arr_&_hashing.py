from typing import *
from collections import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                threeSum = n + nums[left] + nums[right]

                if (threeSum < 0):
                    left += 1

                elif (threeSum > 0):
                    right -= 1

                else:
                    res.append([n, nums[left], nums[right]])
                    left += 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return res


print(
    Solution.threeSum("", [-1, 0, 1, 2, -1, -4])
)

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         left, right = 0, len(numbers) - 1
#         while left < right:
#             curr = numbers[left] + numbers[right]
#             if (target > curr):
#                 left += 1
#             elif (target < curr):
#                 right -= 1
#             else:
#                 return [left + 1, right + 1]


# print(Solution.twoSum("", [2, 7, 11, 15], 9))

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         left, right = 0, len(s) - 1

#         while left < right:
#             while left < right and not s[left].isalnum():
#                 left += 1

#             while right > left and not s[right].isalnum():
#                 right -= 1

#             if s[left].lower() != s[right].lower():
#                 return False

#             left += 1
#             right -= 1

#         return True


# print(
#     Solution.isPalindrome("", "A man, a plan, a canal: Panama")
# )

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         numsSet = set(nums)
#         res = 0

#         for n in nums:
#             if (n-1) not in numsSet:
#                 length = 0
#                 while (n + length) in numsSet:
#                     length += 1
#                 res = max(res, length)
#         return res


# print(
#     Solution.longestConsecutive("", [100, 4, 200, 1, 3, 2])
# )
# class Solution:
#     def encode(self, strs):
#         encoded = ""
#         for w in strs:
#             encoded += str(len(w)) + "#" + w

#         return encoded

#     def decode(self, str):
#         # 4#lint4#code4#love3#you
#         decoded = []

#         i = 0

#         while i < len(str):
#             j = i

#             while str[j] != "#":
#                 j += 1

#             length = int(str[i:j])

#             decoded.append(str[j+1: j+1+length])

#             i = j+1+length
#         return decoded


# print(
#     # Solution.encode("", ["lint", "code", "love", "you"])
#     Solution.decode("", "10#asdfghjkli4#code4#love3#you")
# )


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
