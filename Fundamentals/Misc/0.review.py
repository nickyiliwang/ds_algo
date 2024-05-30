from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [i for i in range(n)]

        def find(i):
            if par[i] == i:
                return i
            else:
                return find(par[i])

        def union(x, y):
            px, py = find(x), find(y)

            if px == py:
                return 0

            if rank[px] > rank[py]:
                par[px] = par[py]
            else:
                par[px] = py
                rank[py] += 1

            return 1

        res = n

        for x, y in edges:
            res -= union(x, y)

        return res


# from typing import List
# from collections import deque

# # -1 - Wall or an obstacle
# # 0 - A Gate
# # INF - Empty room, 2147483647 represents it.

# # Fill each land cell with the distance to its nearest gate. If a land cell cannot reach a treasure chest than the value should remain INF.


# # Assume the grid can only be traversed up, down, left, or right.
# class Solution:
#     def islandsAndTreasure(self, grid: List[List[int]]) -> None:
#         row, col = len(grid), len(grid[0])
#         rowB, colB = range(row), range(col)
#         visited = set()
#         q = deque()
#         dist = 0

#         for r in rowB:
#             for c in colB:
#                 if grid[r][c] == 0:
#                     q.append((r, c))
#                     visited.add((r, c))

#         def mod(r, c):
#             if r not in rowB or c not in colB or (r, c) in visited or grid[r][c] == -1:
#                 return

#             visited.add((r, c))
#             q.append((r, c))

#         while q:
#             for _ in range(len(q)):
#                 r, c = q.popleft()
#                 grid[r][c] = dist

#                 mod(r + 1, c)
#                 mod(r - 1, c)
#                 mod(r, c + 1)
#                 mod(r, c - 1)
#             dist += 1


# print(
#     Solution().islandsAndTreasure(
#         [
#             [2147483647, -1, 0, 2147483647],
#             [2147483647, 2147483647, 2147483647, -1],
#             [2147483647, -1, 2147483647, -1],
#             [0, -1, 2147483647, 2147483647],
#         ]
#     )
# )

# from typing import List


# class Solution:
#     def encode(self, l):
#         res = ""
#         for w in l:
#             res += str(len(w)) + "#" + w

#         return res

#     def decode(self, s):
#         res = []
#         pointer = 0

#         while pointer < len(s):
#             if s[pointer] != "#":
#                 pointer += 1
#             else:
#                 tmp = pointer
#                 length = pointer
#                 res.append(s[pointer + 1 : tmp + 1 + length])
#                 pointer = tmp + 1 + length
#         return res


# coded = Solution().encode(["I", "Love", "You"])
# print(Solution().decode(coded))
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         res, far, end = 0, 0, 0
#         n = len(nums)

#         for i in range(n - 1):
#             far = max(far, i + nums[i])

#             if far >= n - 1:
#                 res += 1
#                 break

#             if i == end:
#                 res += 1
#                 end = far

#         return res


# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         res, far, end = 0, 0, 0
#         n = len(nums)
#         for i in range(n - 1):
#             far = max(far, i + nums[i])
#             if far >= n - 1:
#                 res += 1
#                 break
#             if i == end:
#                 res += 1
#                 end = far
#         return res


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         maxSum = currSum = nums[0]

#         for n in nums[1:]:
#             currSum = max(n, currSum + n)
#             maxSum = max(maxSum, currSum)

#         return maxSum

# def something(str):
#     print('hello world ' + str)

# something('nick')

# from typing import List


# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         cache = {}

#         def dfs(i, t):
#             if i == len(nums):
#                 return 1 if t == target else 0
#             if (i, t) in cache:
#                 return cache[(i, t)]

#             cache[(i, t)] = dfs(i + 1, t + nums[i]) + dfs(i + 1, t - nums[i])
#             return cache[(i, t)]

#         return dfs(0, 0)


# print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))

# from typing import List

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         dp = {}
#         def dfs(i, buying):
#             if i >= len(prices):
#                 return 0
#             if (i, buying) in dp:
#                 return dp[(i, buying)]
#             if buying:
#                 buy = dfs(i + 1, not buying) - prices[i]
#                 cooldown = dfs(i + 1, buying)
#                 dp[(i, buying)] = max(buy, cooldown)
#             else:
#                 selling = dfs(i + 2, not buying) + prices[i]
#                 cooldown = dfs(i + 1, buying)
#                 dp[(i, buying)] = max(selling, cooldown)

#             return dp[(i, buying)]

#         return dfs(0, True)


# print(Solution().maxProfit([3, 3]))

# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         total = max(nums)
#         currMin = 0
#         currMax = 0

#         for n in nums:
#             tmp = currMax
#             currMax = max(n, n + currMax, n + currMin)
#             currMin = min(n, n + tmp, n + currMin)
#             total = max(total, currMax, currMin)

#         return total


# print(Solution().maxProduct([7,1,5,3,6,4]))

# Explanation: [2,3] has the largest product 6.


# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         row, col = len(text1), len(text2)
#         dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]

#         for r in range(row - 1, -1, -1):
#             for c in range(col - 1, -1, -1):
#                 if text1[r] == text2[c]:
#                     dp[r][c] = dp[r + 1][c + 1] + 1
#                 else:
#                     dp[r][c] = max(dp[r + 1][c], dp[r][c + 1])

#         return dp[0][0]


# def rob(nums):
#     twoBefore, oneBefore = 0, 0
#     for n in nums:
#         tmp = max(twoBefore + n, oneBefore)
#         twoBefore = oneBefore
#         oneBefore = tmp
#     return oneBefore


# print(rob([2, 7, 9, 3, 1]))
# # from typing import List


# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         dp = [1] * len(nums)

#         for i in range(len(nums)):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[i], dp[j] + 1)

#         return max(dp)


# print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))


# mid = (1 + 10) // 2

# res = (mid / 2) * (1 + mid)

# print(res)

# def houseRobber(nums):
#     oneAway, twoAway = 0, 0

#     for n in nums:
#         temp = max(n + twoAway, oneAway)
#         oneAway = temp
#         twoAway = oneAway

#     return oneAway


# data = [1, 2, 3, 4, 5, 6, 7, 8]
# print(data[1:])
# print(data[:-1])


# def houseRobber(nums):
#     oneAway, twoAway = 0, 0

#     for num in nums:
#         temp = max(twoAway + num, oneAway)
#         oneAway = temp
#         twoAway = oneAway

#     return oneAway


# def climbingStairs(n):
#     if n == 1:
#         return 1

#     oneAway = 1
#     twoAway = 1
#     total = 0

#     for _ in range(2, n + 1):
#         total = oneAway + twoAway
#         twoAway = oneAway
#         oneAway = total

#     return total


# print(climbingStairs(3))


# from typing import List
# from collections import defaultdict, deque


# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         if endWord not in wordList:
#             return 0

#         visited = set()
#         q = deque([beginWord])
#         nei = defaultdict(list)
#         wordList.append(beginWord)
#         res = 1
#         # adjList built
#         for word in wordList:
#             for i in range(len(beginWord)):
#                 pattern = word[:i] + "*" + word[i + 1 :]
#                 nei[pattern].append(word)

#         # DFS
#         while q:
#             for _ in range(len(q)):
#                 word = q.popleft()

#                 if word == endWord:
#                     return res

#                 for i in range(len(word)):
#                     pattern = word[:i] + "*" + word[i + 1 :]
#                     for neiWord in nei[pattern]:
#                         if neiWord not in visited:
#                             visited.add(neiWord)
#                             q.append(neiWord)
#             res += 1
#         return 0


# print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))


# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
#         parent = [i for i in range(len(edges) + 1)]
#         rank = [1] * (len(edges) + 1)

#         def find(i):
#             if parent[i] == i:
#                 return i
#             else:
#                 return find(parent[i])

#         def union(x, y):
#             pX, pY = find(x), find(y)

#             if pX == pY:
#                 return False

#             if parent[pX] < parent[pY]:
#                 parent[pY] = parent[pX]
#             elif parent[pX] > parent[pY]:
#                 parent[pX] = parent[pY]
#             else:
#                 parent[pX] = parent[pY]
#                 rank[pY] = rank[pX] + 1

#             return True

#         for x, y in edges:
#             if union(x, y) == False:
#                 return [x, y]


# from typing import List
# from collections import deque

# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         row, col = len(grid), len(grid[0])
#         rowBound, colBound = range(row), range(col)
#         time, fresh = 0, 0
#         q = deque()

#         for r in rowBound:
#             for c in colBound:
#                 if grid[r][c] == "1":
#                     fresh += 1
#                 if grid[r][c] == "2":
#                    q.append([r, c])

#         direction = [[1,0],[-1,0],[0,1],[0,-1]]
#         while q or fresh > 0:
#             r, c = q.popleft()
#             for dr, dc in direction:
#                 row, col = dr+r, dc+c
#                 if (
#                     row not in rowBound or col not in colBound or grid[r][c] != 1
#                 ):
#                     continue

#                 grid[row][col] = 2
#                 q.append([row, col])
#                 fresh -= 1

#             time += 1
#         return time if fresh == 0 else -1


# from typing import *
# from collections import *
# from math import *
# from ds_types.linked_list import LinkedList, ListNode


# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_arr = arr[:mid]
#         right_arr = arr[mid:]

#         merge_sort(left_arr)
#         merge_sort(right_arr)

#         left_idx = 0
#         right_idx = 0
#         merged_idx = 0

#         while left_idx < len(left_arr) and right_idx < len(right_arr):
#             if left_arr[left_idx] < right_arr[right_idx]:
#                 arr[merged_idx] = left_arr[left_idx]
#                 left_idx += 1
#             else:
#                 arr[merged_idx] = right_arr[right_idx]
#                 right_idx += 1
#             merged_idx += 1

#         while left_idx < len(left_arr):
#             arr[merged_idx] = left_arr[left_idx]
#             left_idx += 1
#             merged_idx += 1

#         while right_idx < len(right_arr):
#             arr[merged_idx] = right_arr[right_idx]
#             right_idx += 1
#             merged_idx += 1

#     return arr


# print(merge_sort([3, 2, 1, 4, 5]))

# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         row, col = len(board), len(board[0])
#         path = set()

#         def dfs(r, c, i):
#             if i == len(word):
#                 return True

#             if (
#                 r < 0
#                 or c < 0
#                 or r >= row
#                 or c >= col
#                 or word[i] != board[r][c]
#                 or (r, c) in path
#             ):
#                 return False

#             path.add((r, c))
#             res = (
#                 dfs(r + 1, c, i + 1)
#                 or dfs(r - 1, c, i + 1)
#                 or dfs(r, c + 1, i + 1)
#                 or dfs(r, c - 1, i + 1)
#             )
#             path.remove((r, c))
#             return res

#         for r in range(row):
#             for c in range(col):
#                 if dfs(r, c, 0):
#                     return True

#         return False


# print(
#     Solution.exist(
#         "", [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"
#     )
# )


# class TriNode:
#     def __init__(self):
#         self.children = {}
#         self.isEnd = False


# class WordDictionary:
#     def __init__(self):
#         self.root = TriNode()

#     def addWord(self, word: str) -> None:
#         curr = self.root
#         for char in word:
#             if char not in curr.children:
#                 curr.children[char] = TriNode()

#             curr = curr.children[char]
#         curr.isEnd = True

#     def search(self, word: str) -> bool:
#         def dfs(index, root):
#             if index == len(word):
#                 return root.isEnd

#             curr = root
#             char = word[index]
#             if char == ".":
#                 for child in curr.children.values():
#                     if dfs(index + 1, child):
#                         return True

#             if char in root.children:
#                 return dfs(index + 1, root.children[char])

#             return False

#         return (0, self.root)


# def topK(nums, k):
#     freq = [[] for i in range(len(nums))]
#     res = []
#     counter = Counter()

#     for n in nums:
#         counter[n] += 1

#     for num, count in counter.items():
#         freq[count - 1].append(num)

#     for nums in reversed(freq):
#         for n in nums:
#             if len(res) != k:
#                 res.append(n)

#     return res


# topK([1], 1)


# def reverseString(str):
#     res = ""
#     for i in range(len(str) - 1, -1, -1):
#         res += str[i]

#     print(res)
#     return res


# reverseString("Hello World !")

# # Input: nums = [-1,0,3,5,9,12], target = 9
# # Output: 4
# # Explanation: 9 exists in nums and its index is 4


# def binarySearch(nums, target):
#     left, right = 0, len(nums) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] > target:
#             right = mid - 1
#         elif nums[mid] < target:
#             left = mid + 1
#         elif nums[mid] == target:
#             return mid

#     return -1


# print(binarySearch([-1, 0, 3, 5, 9, 12], 13))

# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         print(lists)


# list = []
# linked_list_1 = LinkedList()
# linked_list_1.append(1)
# linked_list_1.append(4)
# linked_list_1.append(5)
# linked_list_2 = LinkedList()
# linked_list_2.append(1)
# linked_list_2.append(3)
# linked_list_2.append(4)
# linked_list_3 = LinkedList()
# linked_list_3.append(2)
# linked_list_3.append(6)
# linked_list_1.display()
# linked_list_2.display()
# linked_list_3.display()
# list.append(linked_list_1.head)
# list.append(linked_list_2.head)
# list.append(linked_list_3.head)

# mergeKListsInstance = Solution()

# newList = mergeKListsInstance.mergeKLists(list)

# while newList:
#     print(newList.val)
#     newList = newList.next
#     # @lc code=end


# class Solution(object):
#     def findDuplicate(self, nums):
#         res = None
#         validator = set()
#         for n in nums:
#             if n not in validator:
#                 validator.add(n)
#             else:
#                 res = n
#         return res
# print(
#     Solution.findDuplicate("", [1,3,4,2,2])
# )

# curr = list1.head.next
# while curr:
#     print(curr.random_index)
#     curr = curr.next

# Solution.copyRandomList("", list1.head.next)


# class Solution(object):
#     def removeNthFromEnd(self, head, n):
#         slow, fast = head, head

#         while fast and fast.next and n > 0:
#             fast = fast.next
#             n -= 1

#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next

#         slow.next = slow.next.next

# list1 = LinkedList()
# list1.append(1)
# list1.append(2)
# list1.append(4)
# list1.append(1)
# list1.append(3) # <= 2
# list1.append(4)
# Solution.removeNthFromEnd("", list1.head, 2)
# list1.display()

# class Solution(object):
#     def reorderList(self, head):
#         slow, fast = head, head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next

#         prev, curr = None, slow
#         while curr:
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp

#         first, second = head, prev
#         while second.next:
#             temp = first.next
#             first.next = second
#             first = temp

#             temp = second.next
#             second.next = first
#             second = temp

# list1 = LinkedList()
# list1.append(1)
# list1.append(2)
# list1.append(3)
# list1.append(4)
# list1.append(5)


# # current = list1.head
# # while current is not None:
# #     print(current.val)  # Do something with the value
# #     current = current.next

# # 1234 => 12 43 => 14 23

# # Starting at 1 instead of 0 with list1.head.next
# Solution.reorderList("", list1.head.next)

# # while list1.head.next:
# #     print(list1.head.next.val)
# #     list1.head = list1.head.next

# current = list1.head
# while current is not None:
#     print(current.val)  # Do something with the value
#     current = current.next

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         list1 = []
#         list2 = []

#         while l1:
#             list1.append(l1.val)
#             l1 = l1.next

#         while l2:
#             list2.append(l2.val)
#             l2 = l2.next

#         str1 = ""
#         str2 = ""

#         for n in reversed(list1):
#             str1 = str1 + str(n)

#         for n in reversed(list2):
#             str2 = str2 + str(n)

#         sum = int(str1) + int(str2)

#         resList = LinkedList()

#         for n in reversed(str(sum)):
#             resList.append(int(n))

#         return resList.head.next


# list1 = LinkedList()
# list1.append(2)
# list1.append(4)
# list1.append(3)

# list2 = LinkedList()
# list2.append(5)
# list2.append(6)
# list2.append(4)

# print(
#     Solution.addTwoNumbers("", list1.head.next, list2.head.next)
# )


# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode()
#         tail = dummy

#         while list1 and list2:
#             if (list1.val < list2.val):
#                 tail.next = list1
#                 list1 = list1.next
#             else:
#                 tail.next = list2
#                 list2 = list2.next

#             tail = tail.next

#         if list1:
#             tail.next = list1

#         if list2:
#             tail.next = list2

#         return dummy.next


# list1 = LinkedList()
# list1.append(1)
# list1.append(2)
# list1.append(4)

# list2 = LinkedList()
# list2.append(1)
# list2.append(3)
# list2.append(4)


# def traverse(head):
#     while head.next:
#         print(head.val)
#         head = head.next


# traverse(Solution.mergeTwoLists("", list1.head, list2.head))


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
