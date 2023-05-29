from typing import *
from collections import *
from math import *


# class Solution:
#     def findMedian(self, nums):
#         print(nums)
#         mid = (0 + len(nums) - 1) // 2

#         if len(nums) % 2 == 0:
#             return float((nums[mid] + nums[mid + 1]) / 2)

#         else:
#             return nums[mid]

#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         if not nums1:
#             return Solution.findMedian("", nums2)

#         if not nums2:
#             return Solution.findMedian("", nums1)

#         for n in nums2:
#             left, right = 0, len(nums1) - 1

#             while left <= right:
#                 mid = (left + right) // 2
#                 if nums1[mid] <= n < nums1[mid + 1]:
#                     nums1.insert(mid + 1, n)
#                     break
#                 elif nums1[mid] > n:
#                     right = mid - 1
#                 elif nums1[mid] < n:
#                     left = mid + 1

#         return Solution.findMedian("", nums1)

# from typing import List


# class Solution:
#     def findMedian(self, nums):
#         print(nums)
#         mid = (0 + len(nums) - 1) // 2

#         if len(nums) % 2 == 0:
#             return float((nums[mid] + nums[mid + 1]) / 2)
#         else:
#             return nums[mid]

#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         if not nums1:
#             return Solution.findMedian("", nums2)

#         if not nums2:
#             return Solution.findMedian("", nums1)

#         for n in nums2:
#             left, right = 0, len(nums1) - 1

#             while left <= right:
#                 mid = (left + right) // 2

#                 if nums1[mid] <= n < nums1[mid + 1] if mid + 1 < len(nums1) else float('inf'):
#                     nums1.insert(mid + 1, n)
#                     break
#                 elif nums1[mid] > n:
#                     right = mid - 1
#                 else:
#                     left = mid + 1

#         print(nums1)

#         return Solution.findMedian("", nums1)


# print(
#     Solution.findMedianSortedArrays("", [3], [-2, -1])
# )


# class TimeMap:

#     def __init__(self):
#         self.values = defaultdict(list)

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         self.values[key].append([timestamp, value])

#     def get(self, key: str, timestamp: int) -> str:
#         res = ""
#         left, right = 0, len(self.values[key]) - 1
#         while left <= right:
#             mid = (left + right) // 2

#             if self.values[key][mid][0] < timestamp:
#                 left = mid + 1
#                 res = self.values[key][mid][1]
#             elif self.values[key][mid][0] > timestamp:
#                 right = mid - 1
#             else:
#                 res = self.values[key][mid][1]
#                 break
#         print("res", res)
#         return res


# timeMap = TimeMap()
# # store the key "foo" and value "bar" along with timestamp = 1.
# timeMap.set("foo", "bar", 1)
# timeMap.get("foo", 1)         # return "bar"
# timeMap.get("foo", 3)         # return "bar"
# # store the key "foo" and value "bar2" along with timestamp = 4.
# timeMap.set("foo", "bar2", 4)
# timeMap.get("foo", 4)         # return "bar2"
# timeMap.get("foo", 5)         # return "bar2"


# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]

# Explanation
# TimeMap timeMap = new TimeMap();

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left, right = 0, len(nums) - 1

#         while left <= right:
#             mid = (left + right) // 2

#             if nums[mid] == target:
#                 return mid

#             if nums[left] <= nums[mid]:
#                 if nums[left] <= target <= nums[mid]:
#                     right = mid - 1
#                 else:
#                     left = mid + 1

#             else:
#                 if nums[mid] <= target <= nums[right]:
#                     left = mid + 1
#                 else:
#                     right = mid - 1

#         return -1

# print(Solution.search("", [4, 5, 6, 7, 0, 1, 2], 0))

# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         left, right = 0, len(nums) - 1
#         res = nums[0]

#         while left <= right:
#             mid = (left + right) // 2
#             res = min(res, nums[mid])

#             if nums[mid] > nums[right]:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return res

# print(
#     Solution.findMin("", [3, 4, 5, 1, 2])
# )

# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         left, right = 1, max(piles)
#         res = max(piles)

#         while left <= right:
#             totalHour = 0
#             mid = (left + right) // 2

#             for banana in piles:
#                 totalHour += ceil(banana / mid)

#             if totalHour <= h:
#                 res = min(res, mid)
#                 right = mid - 1
#             elif totalHour > h:
#                 left = mid + 1

#         return res

# print(
#     Solution.minEatingSpeed("", [3,6,7,11], 8)
# )

# # Monotonic Decreasing Stack

# def largestRectangleArea(heights):
#     # The 0 will clear the stack (because 0 > -1) after the heights are iterated
#     heights.append(0)
#     stack = [-1]
#     res = 0

#     for i, curr in enumerate(heights):
#         # At each iteration, it checks if the current heights is less than the heights at the top of the stack.
#         while heights[stack[-1]] > curr:
#             # If it is, it pops the heights at the top of the stack and calculates the area of the rectangle represented by that heights and the width of the rectangle (which is the difference between the current index and the index at the top of the stack).
#             h = heights[stack.pop()]

#             # By subtracting 1 from the difference (i - stack[-1]), we exclude the current element (curr) from the width calculation, as the width is determined by the elements to the left of the current element.

#             # [2,1,5,6,2,3]
#             print("height", h, "width", i, stack[-1])
#             # height 6 width 4 2
#             # height 5 width 4 1
#             w = i - stack[-1] - 1
#             res = max(res, h * w)

#         stack.append(i)

#     return res

# largestRectangleArea([2, 1, 5, 6, 2, 3])

# class Solution(object):
#     def min_window(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         # Struggled with this problem for a long while.
#         # Idea: Two pointers: moving end forward to find a valid window,
#         #                     moving start forward to find a smaller window
#         #                     counter and hash_map to determine if the window is valid or not

#         # Count the frequencies for chars in t
#         hash_map = dict()
#         for c in t:
#             if c in hash_map:
#                 hash_map[c] += 1
#             else:
#                 hash_map[c] = 1

#         start, end = 0, 0

#         # If the minimal length doesn't change, it means there's no valid window
#         min_window_length = len(s) + 1

#         # Start point of the minimal window
#         min_window_start = 0

#         # Works as a counter of how many chars still need to be included in a window
#         num_of_chars_to_be_included = len(t)

#         while end < len(s):
#             # If the current char is desired
#             if s[end] in hash_map:
#                 # Then we decreased the counter, if this char is a "must-have" now, in a sense of critical value
#                 if hash_map[s[end]] > 0:
#                     num_of_chars_to_be_included -= 1
#                 # And we decrease the hash_map value
#                 hash_map[s[end]] -= 1

#             # If the current window has all the desired chars
#             while num_of_chars_to_be_included == 0:
#                 # See if this window is smaller
#                 if end - start + 1 < min_window_length:
#                     min_window_length = end - start + 1
#                     min_window_start = start

#                 # if s[start] is desired, we need to update the hash_map value and the counter
#                 if s[start] in hash_map:
#                     hash_map[s[start]] += 1
#                     # Still, update the counter only if the current char is "critical"
#                     if hash_map[s[start]] > 0:
#                         num_of_chars_to_be_included += 1

#                 # Move start forward to find a smaller window
#                 start += 1

#             # Move end forward to find another valid window
#             end += 1

#         if min_window_length == len(s) + 1:
#             return ""
#         else:
#             return s[min_window_start:min_window_start + min_window_length]

# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         left, right = 0, len(matrix) - 1
#         numbers = []

#         while left <= right:
#             mid = (left + right) // 2

#             if matrix[mid][0] > target:
#                 right = mid - 1
#             elif matrix[mid][-1] < target:
#                 left = mid + 1
#             else:
#                 numbers = matrix[mid]
#                 break

#         left, right = 0, len(numbers) - 1

#         while left <= right:
#             mid = (left + right) // 2
#             if numbers[mid] < target:
#                 left = mid + 1
#             elif numbers[mid] > target:
#                 right = mid - 1
#             else:
#                 return True

#         return False

# print(Solution.searchMatrix(""), [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left = 0
#         right = len(nums) - 1

#         while left <= right:
#             middle = (left + right) // 2

#             if nums[middle] < target:
#                 left = middle + 1
#             elif nums[middle] > target:
#                 right = middle - 1
#             elif nums[middle] == target:
#                 return middle

#         return -1

# print(Solution.search("", [-1, 0, 3, 5, 9, 12], 9))

# # Mono decreasing stack
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         res = [0] * len(temperatures)
#         stack = []
#         for i, temp in enumerate(temperatures):
#             while stack and temperatures[stack[-1]] < temp:
#                 position = stack.pop()
#                 res[position] = i - position
#             stack.append(i)
#         return res

# print(
#     Solution.dailyTemperatures("", [73, 74, 75, 71, 69, 72, 76, 73])
# )

# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         res = []

#         def backtracking(open, close, variation):
#             if open == close == n:
#                 res.append(variation)
#                 return

#             if open < n:
#                 backtracking(open + 1, close, variation + "(")

#             if close < open:
#                 backtracking(open, close + 1, variation + ")")

#         backtracking(0, 0, "")

#         return res

# print(Solution.generateParenthesis("", 3))

# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         stack = []
#         for char in tokens:
#             if char == "+":
#                 right = stack.pop()
#                 left = stack.pop()
#                 stack.append(left + right)
#             elif char == "-":
#                 right = stack.pop()
#                 left = stack.pop()
#                 stack.append(left - right)
#             elif char == "*":
#                 right = stack.pop()
#                 left = stack.pop()
#                 stack.append(left * right)
#             elif char == "/":
#                 right = stack.pop()
#                 left = stack.pop()
#                 stack.append(int(left / right))
#             else:
#                 stack.append(int(char))

#         return stack[0]

# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
# print(
#     Solution.evalRPN("", ["10", "6", "9", "3", "+", "-11",
#                      "*", "/", "*", "17", "+", "5", "+"])
# )

# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.minStack = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         if not self.minStack:
#             self.minStack.append(val)
#         else:
#             self.minStack.append(min(self.minStack[-1], val))

#     def pop(self) -> None:
#         self.stack.pop()
#         self.minStack.pop()

#     def top(self) -> int:
#         if not self.stack:
#             return []

#         return self.stack[-1]

#     def getMin(self) -> int:
#         return self.minStack[-1]

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []

#         validator = {
#             ")": "(",
#             "]": "[",
#             "}": "{"
#         }

#         for p in s:
#             if p in validator:
#                 if not stack or stack.pop() != validator[p]:
#                     return False
#             else:
#                 stack.append(p)

#         if len(stack) > 0:
#             return False

#         return True

# print(Solution.isValid("", "()"))

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         res, left, q = [], 0, deque()

#         for right, n in enumerate(nums):
#             while q and nums[q[-1]] <= n:
#                 q.pop()

#             q.append(right)

#             if left > q[0]:
#                 q.popleft()

#             if right - left + 1 == k:
#                 res.append(nums[q[0]])
#                 left += 1

#         return res

# print(
#     Solution.maxSlidingWindow("", [1, 3, -1, -3, 5, 3, 6, 7], 3)
# )

# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         count1, count2 = Counter(s1), Counter()
#         window = len(s1)

#         for i in range(len(s2)):
#             if (i < window):
#                 count2[s2[i]] += 1
#             else:
#                 count2[s2[window - i]] -= 1
#                 count2[s2[i]] += 1

#             if count1 == count2:
#                 return True

#         return False

# print(
#     Solution.checkInclusion("", "ab", "eidbaooo")
# )

# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         left, res, counter = 0, 0, Counter()

#         for right in range(len(s)):
#             counter[s[right]] += 1

#             while (right - left + 1) - max(counter.values()) > k:
#                 counter[s[left]] -= 1
#                 left += 1

#             res = max(res, right - left + 1)
#             return res

# print(Solution.characterReplacement("", "ABAB", 2))

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         validator = set()
#         left = 0
#         res = 0

#         for right in s:
#             while right in validator:
#                 validator.remove(s[left])
#                 left += 1
#             validator.add(right)
#             res = max(res, len(validator))

#         return res

# print(
#     Solution.lengthOfLongestSubstring("", "abcabcbb")
# )

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         res = 0
#         left, right = 0, 1

#         while right < len(prices):
#             if prices[left] < prices[right]:
#                 profit = prices[right] - prices[left]
#                 res = max(res, profit)
#             else:
#                 left = right
#             right += 1
#         return res

# print(Solution.maxProfit("", [7,1,5,3,6,4]))

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         left, right = 0, len(height) - 1
#         leftMax, rightMax, res = 0, 0, 0

#         while left < right:
#             leftMax = max(leftMax, height[left])
#             rightMax = max(rightMax, height[right])

#             if height[left] < height[right]:
#                 res += leftMax - height[left]
#                 left += 1

#             else:
#                 res += rightMax - height[right]
#                 right -= 1

#         return res

# print(Solution.trap("", [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         res = []
#         maxLeft = 0
#         maxRight = 0

#         maxLefts = []
#         maxRights = []

#         for n in height:
#             maxLefts.append(maxLeft)
#             maxLeft = max(maxLeft, n)

#         for n in reversed(height):
#             print("N", n)
#             maxRights.append(maxRight)
#             maxRight = max(maxRight, n)

#         maxRights.reverse()

#         for i in range(len(maxLefts)):
#             if min(maxLefts[i], maxRights[i]) > n:
#                 res.append(min(maxLefts[i], maxRights[i]) - n)

#         print(maxLefts, maxRights)
#         return sum(res)

#         print(maxLefts, maxRights)

# print(Solution.trap("", [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         res = 0
#         left, right = 0, len(height) - 1

#         while left < right:
#             area = min(height[left], height[right]) * (right - left)
#             res = max(res, area)

#             if (height[left] <= height[right]):
#                 left += 1
#             elif (height[left] > height[right]):
#                 right -= 1

#         return res

# print(
#     Solution.maxArea("", [1, 8, 6, 2, 5, 4, 8, 3, 7])
# )

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         res = []

#         for i, n in enumerate(nums):
#             if i > 0 and n == nums[i - 1]:
#                 continue

#             left, right = i + 1, len(nums) - 1

#             while left < right:
#                 threeSum = n + nums[left] + nums[right]

#                 if (threeSum < 0):
#                     left += 1

#                 elif (threeSum > 0):
#                     right -= 1

#                 else:
#                     res.append([n, nums[left], nums[right]])
#                     left += 1

#                     while left < right and nums[left] == nums[left - 1]:
#                         left += 1

#         return res

# print(
#     Solution.threeSum("", [-1, 0, 1, 2, -1, -4])
# )

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