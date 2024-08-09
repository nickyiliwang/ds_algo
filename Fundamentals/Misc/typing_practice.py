from typing import *
from collections import *
from math import *
import heapq

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


# 1
def containsDuplicate(nums):
    validator = set()
    for n in nums:
        if n in validator:
            return True
        else:
            validator.add(n)


# 2
def isAnagram(s, t):
    if len(s) != len(t):
        return False

    cS, cT = Counter(s), Counter(t)

    for char in s:
        if cS[char] != cT[char]:
            return False

        return True


# 3
def twoSum(nums, target):
    cache = {}
    for i, n in enumerate(nums):
        if n in cache:
            return [cache[n], i]
        else:
            cache[target - n] = i


# 4
def groupAnagrams(strs):
    res = defaultdict(list)

    for w in strs:
        alpha = [0] * 26
        for c in w:
            alpha[ord(c) - ord("a")] += 1
        res[tuple(alpha)].append(w)

    return res.values()


# 5
def topKFrequent(nums, k):
    bucket = [[] for _ in range(len(nums))]
    counters = Counter(nums)
    res = []

    for num, count in counters.items():
        bucket[count - 1].append(num)

    for i in range(len(bucket) - 1, -1, -1):
        for n in bucket[i]:
            res.append(n)
            if len(res) == k:
                return res


# 6
def productExceptSelf(nums):
    n = len(nums)
    res = [0] * n
    prefix = 1

    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res


# 7
def isValidSudoku(board):
    row, col, sqr = set(), set(), set()

    def dfs(r, c):
        curr = board[r][c]
        if curr == ".":
            return
        if (r, curr) in row or (c, curr) in col or (r // 3, c // 3, curr) in sqr:
            return False

        row.add((r, curr))
        col.add((c, curr))
        sqr.add((r // 3, c // 3, curr))

        return True

    for r in range(len(board)):
        for c in range(len(board[0])):
            if not dfs(r, c):
                return False

    return True


# 8
def encode(strs):
    res = ""
    for word in strs:
        res += str(len(word)) + "#" + word

    return res


def decode(str):
    res = []
    i = 0

    while i < len(str):
        j = i

        while str[j] != "#":
            j += 1

        charLen = int(str[i:j])
        res.append(str[j + 1 : j + 1 + charLen])

        i = j + 1 + charLen
    return res


# 9
def longestConsecutive(nums):
    numSet = set(nums)
    res = 0

    for n in nums:
        if (n - 1) not in numSet:
            length = 0

            while (n + length) in numSet:
                length += 1
            res = max(res, length)
    return res


# 10
def isPalindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1

    return True


# 11
def twoSumSorted(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        currSum = nums[l] + nums[r]
        if currSum < target:
            l += 1
        elif currSum > target:
            r -= 1
        else:
            return [l + 1, r + 1]


# 12
def threeSum(nums):
    res = []
    nums.sort()

    for i, n in enumerate(nums):
        if i > 0 and n == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1

        while l < r:
            currSum = n + nums[l] + nums[r]
            if currSum < 0:
                l += 1
            elif currSum > 0:
                r -= 1
            else:
                res.append([n, nums[l], nums[r]])
                l += 1

                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return res


# 13
def maxArea(height):
    res = 0
    l, r = 0, len(height) - 1

    while l < r:
        length = r - l
        area = min(height[l], height[r]) * length
        res = max(res, area)

        if height <= height[r]:
            l += 1
        else:
            r += 1
    return res


# 14
def trap(height):
    l_max, r_max, res = 0, 0, 0
    l, r = 0, len(height) - 1

    while l < r:
        l_max = max(l_max, height[l])
        r_max = max(r_max, height[r])

        if l_max < r_max:
            res += l_max - height[l]
            l += 1
        else:
            res += r_max - height[r]
            r -= 1

    return res


# 15
def maxProfit(prices):
    res = 0
    l, r = 0, 1
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            res = max(res, profit)
        else:
            l = r
        r += 1
    return res


# 16
def lengthOfLongestSubstring(s):
    validator = set()
    res, l = 0, 0

    for r in s:
        while r in validator:
            validator.remove(s[l])
            l += 1

        validator.add(r)
        res = max(res, len(validator))
    return res


# 17
def characterReplacement(s, k):
    res, l = 0, 0
    counter = Counter()

    for r in range(len(s)):
        counter[s[r]] += 1

        while (r - l + 1) - max(counter.values()) > k:
            counter[s[l]] -= 1
            l += 1

        res = max(res, (r - l + 1))

    return res


# 18
def findAnagrams(s, p):
    if len(s) < len(p):
        return []

    c1 = Counter(p)
    c2 = Counter()
    res = []
    window = len(p)

    for i in range(len(s)):
        if i < window:
            c2[s[i]] += 1
        else:
            c2[s[i - window]] -= 1
            c2[s[i]] += 1

        if c1 == c2:
            res.append(i - window + 1)

    return res


# 19
def checkInclusion(s1, s2):
    c1, c2 = Counter(s1), Counter()
    window = len(s1)

    for i in range(len(s2)):
        if i < window:
            c2[s2[i]] += 1
        else:
            c2[s2[i - window]] -= 1
            c2[s2[i]] += 1

        if c1 == c2:
            return True
    return False


# 20
def minWindow(s, t):
    haveC, needC = Counter(), Counter(t)
    haveLen, needLen = 0, len(t)
    res, resLen = "", float("inf")

    left = 0

    for right in range(len(s)):
        haveC[s[right]] += 1

        if haveC[s[right]] <= needC[s[right]]:
            haveLen += 1

        while haveLen == needLen:
            currLen = right - left + 1
            if currLen < resLen:
                res = s[left : right + 1]
                resLen = currLen

            haveC[s[left]] -= 1
            if haveC[s[left]] < needC[s[left]]:
                haveLen -= 1
            left += 1

    return res


# 21
def maxSlidingWindow(nums, k):
    left = 0
    res = []
    q = deque()

    for right, rightVal in enumerate(nums):
        while q and nums[q[-1]] <= rightVal:
            q.pop()
        q.append(right)

        if left > q[0]:
            q.popleft()

        if right - left + 1 == k:
            res.append(nums[q[0]])
            left += 1

    return res


# 22
def isValid(s):
    stack = []
    validator = {")": "(", "]": "[", "}": "{"}

    for p in s:
        if p in validator:
            if not stack or stack.pop() != validator[p]:
                return False
            else:
                stack.append(p)

    if len(stack) > 0:
        return False

    return True


# 23
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)

        if self.minStack:
            val = min(val, self.minStack[-1])
        self.minStack.append(val)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]


# 24
def evalRPN(tokens):
    stack = []

    for c in tokens:
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif c == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(c))

    return stack[0]


# 25
def generateParenthesis(n):
    res = []

    def backtracking(open, closed, paren):
        if open == closed == n:
            res.append(paren)

        if open < n:
            backtracking(open + 1, closed, paren + "(")

        if closed < open:
            backtracking(open, closed + 1, paren + ")")

    backtracking(0, 0, "")

    return res


# 26
def dailyTemperatures(temps):
    res = [0] * len(temps)
    stack = []

    for i, tmp in enumerate(temps):
        while stack and temps[stack[-1]] < tmp:
            pos = stack.pop()
            res[pos] = i - pos
        stack.append(i)

    return res


# 27
def largestRectangleArea(heights):
    heights.append(0)
    stack = [-1]
    res = 0

    for i, height in enumerate(heights):
        while stack and heights[stack[-1]] > height:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            res = max(res, h * w)

        stack.append(i)

    return res


# 28
def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2

        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            return mid
    return -1


# 29
def searchMatrix(matrix, target):
    l, r = 0, len(matrix) - 1
    nums = []

    while l <= r:
        m = (l + r) // 2

        if matrix[m][-1] < target:
            l = m + 1
        elif matrix[m][0] > target:
            r = m - 1
        else:
            nums = matrix[m]
            break

    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            return True

    return False


# 30
def minEatingSpeed(piles, h):
    l, r = 1, max(piles)
    res = max(piles)
    totalTime = 0

    while l <= r:
        totalTime = 0
        m = (l + r) // 2
        for b in piles:
            totalTime += ceil(b / m)
            if totalTime > h:
                break
        if totalTime <= h:
            res = min(res, m)
            r = m - 1
        else:
            l = m + 1

    return res


# 31
def findMin(nums):
    l, r = 0, len(nums) - 1
    res = float("inf")

    while l <= r:
        m = (l + r) // 2
        res = min(res, nums[m])
        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m - 1
    return res


# 32
def search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m

        if nums[l] <= nums[m]:
            if nums[l] <= target <= nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            if nums[m] <= target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    return -1


# 33
class TimeMap:
    def __init__(self):
        self.values = defaultdict(list)

    def set(self, key, value, timestamp):
        self.values[key].append([timestamp, value])

    def get(self, key, timestamp):
        data = self.values[key]
        l, r = 0, len(data) - 1
        res = ""

        while l <= r:
            m = (l + r) // 2
            if data[m][0] < timestamp:
                res = data[m][1]
                l = m + 1
            elif data[m][0] > timestamp:
                r = m - 1
            else:
                res = data[m][1]
                break
        return res


# 34
def findMedianSortedArrays(nums1, nums2):
    merged = []
    i, j = 0, 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    while i < len(nums1):
        merged.append(nums1[i])
        i += 1

    while j < len(nums2):
        merged.append(nums2[j])
        j += 1

    mid = len(merged) // 2
    if len(merged) % 2 == 0:
        return (merged[mid - 1] + merged[mid]) / 2
    else:
        return merged[mid]


# 35
def reverseList(head):
    prev, curr = None, head
    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode

    return prev


def reverseList(head):
    if not head:
        return None

    newHead = head
    if head.next:
        newHead = reverseList(head.next)
        head.next.next = head
    head.next = None

    return newHead


# 36
def mergeTwoLists(list1, list2):
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

    if list1:
        tail.next = list1
    else:
        tail.next = list2

    return dummy.next


# 37
def reorderList(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev, curr = None, slow
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    first, second = head, prev
    while second.next:
        tmp = first.next
        first.next = second
        first = tmp

        tmp = second.next
        second.next = first
        second = tmp


# 38
def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)

    slow, fast = dummy, head
    for _ in range(n):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next


# 39
def copyRandomList(head):
    db = {None: None}

    curr = head
    while curr:
        n = Node(curr.val)
        db[curr] = n
        curr = curr.next

    curr = head
    while curr:
        n = db[curr]
        n.next = db[curr.next]
        n.random = db[curr.random]
        curr = curr.next

    return db[head]


# 40
def addTwoNumbers(l1, l2):
    l1str = l2str = ""

    while l1:
        l1str = str(l1.val) + l1str
        l1 = l1.next
    while l2:
        l2str = str(l2.val) + l2str
        l2 = l2.next

    sum = str(int(l1str) + int(l2str))

    dummy = ListNode()
    curr = dummy

    for n in reversed(sum):
        curr.next = ListNode(n)
        curr = curr.next

    return dummy.next


# 41
def hasCycle(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# 42
def findDuplicate(nums):
    slow, fast = 0, 0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break
    slow2 = 0

    while True:
        slow = nums[slow]
        slow2 = nums[slow2]

        if slow == slow2:
            return slow


# 43
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru]


# 44
def mergeLists(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next
    if l1:
        tail.next = l1
    else:
        tail.next = l2

    return dummy.next


def mergeKLists(lists):
    if not lists:
        return None

    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if len(lists) > (i + 1) else None

            merged.append(mergeLists(l1, l2))
        lists = merged
    return lists[0]


# 45
def reverseKGroup(head, k):
    curr = head
    for _ in range(k):
        if not curr:
            return head
        curr = curr.next

    prev, curr = None, head

    for _ in range(k):
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    head.next = reverseKGroup(curr, k)
    return prev


# 46
def invertTree(root):
    if not root:
        return

    root.left, root.right = invertTree(root.right), invertTree(root.left)

    return root


# 47
def maxDepth(root):
    if not root:
        return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))


# 48
def diameterOfBinaryTree(root):
    diameter = 0

    def dfs(root):
        nonlocal diameter
        if root is None:
            return 0

        left, right = dfs(root.left), dfs(root.right)
        diameter = max(diameter, left + right)

        return 1 + max(left, right)

    dfs(root)
    return diameter


# 49
def isBalanced(root):
    isBalanced = True

    def dfs(root):
        nonlocal isBalanced

        if not root:
            return 0

        left, right = dfs(root.left), dfs(root.right)

        if abs(left - right) > 1:
            isBalanced = False

        return 1 + max(left, right)

    dfs(root)

    return isBalanced


# 50
def isSameTree(p, q):
    if not p and not q:
        return True

    if not p or not q or p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


def isSameTreeStack(p, q):
    stack = [[p, q]]

    while stack:
        p, q = stack.pop()

        if p and q and p.val == q.val:
            stack.append([p.left, q.left])
            stack.append([p.right, q.right])
        elif p or q:
            return False
    return True


# 51
def sameTree(p, q):
    if not p and not q:
        return True

    if not p or not q or p.val != q.vap:
        return False
    else:
        return sameTree(p.left, q.left) and sameTree(p.right, q.right)


def isSubtree(root, subRoot):
    if not subRoot:
        return True

    if not root:
        return False

    if sameTree(root, subRoot):
        return True

    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


# 52
def lowestCommonAncestor(root, p, q):
    while True:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root


# 53
def levelOrder(root):
    if not root:
        return []

    q = deque([root])
    res = []

    while q:
        tmp = []
        for _ in range(len(q)):
            node = q.popleft()
            if node:
                tmp.append(node.val)
                q.append(node.left)
                q.append(node.right)

        if len(tmp) > 0:
            res.append(tmp)
    return res


# 54
def rightSideView(root):
    if not root:
        return root

    q = deque([root])
    rightSide = []

    while q:
        tmp = []

        for _ in range(len(q)):
            node = q.popleft()

            if node:
                tmp.append(node.val)
                q.append(node.left)
                q.append(node.right)

        if len(tmp) > 0:
            rightSide.append(tmp[-1])

    return rightSide


# 55
def goodNodes(root):
    q = deque([root, root.val])
    res = 0

    while q:
        for _ in range(len(q)):
            node, maxVal = q.popleft()
            if node:
                if node.val >= maxVal:
                    res += 1
                maxVal = max(maxVal, node.val)
                q.append((node.left, maxVal))
                q.append((node.right, maxVal))
    return res


# 56
def isValidBST(root):
    def valid(node, low, high):
        if not node:
            return True

        if not (low < node.val < high):
            return False

        return valid(node.left, low, node.val) and valid(node.right, node.val, high)

    return valid(root, float("-inf"), float("inf"))


def isValidBSTStack(root):
    if root is None:
        return True

    q = deque([root, float("-inf"), float("inf")])
    while q:
        for _ in range(len(q)):
            node, low, high = q.popleft()

            if not low < node.val < high:
                return False

            if node.left:
                q.append((node.left, low, node.val))

            if node.right:
                q.append((node.right, node.val, high))

    return True


# 57
def kthSmallest(root, k):
    res = []

    def dfs(node):
        if not node:
            return

        dfs(node.left)
        if len(res) == k:
            return

        res.append(node.val)
        dfs(node.right)

    dfs(root)

    return res[-1]


# 58
def buildTree(preorder, inorder):
    inorderDict = {v: i for i, v in enumerate(inorder)}

    def builder(l, r):
        if l > r:
            return None

        root = TreeNode(preorder.pop(0))
        i = inorderDict[root.val]

        root.left = builder(l, i - 1)
        root.right = builder(i + 1, r)

        return root

    return builder(0, len(inorder) - 1)


# 59
def maxPathSum(root):
    maxPath = root.val

    def dfs(node):
        nonlocal maxPath
        if not node:
            return 0

        leftMax, rightMax = dfs(node.left), dfs(node.right)

        leftMax, rightMax = max(leftMax, 0), max(rightMax, 0)

        maxPath = max(maxPath, node.val + leftMax + rightMax)

        return node.val + max(leftMax, rightMax)

    dfs(root)
    return maxPath


# 60
class Codes:
    def serialize(self, root):
        serialize = []

        def dfs(root):
            nonlocal serialize
            if not root:
                serialize.append("None")
                return
            serialize.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            return root

        dfs(root)
        return ",".join(serialize)

    def deserialize(self, data):
        serial = data.split(",")
        index = 0

        def dfs():
            nonlocal index
            if serial[index] == "None":
                index += 1
                return None

            root = TreeNode(int(serial[index]))
            index += 1
            root.left = dfs()
            root.right = dfs()

            return root

        return dfs()


# 61
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.isEnd = True

    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.isEnd

    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


# 62
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]
        curr.isEnd = True

    def search(self, word):
        def dfs(i, root):
            if i == len(word):
                return root.isEnd

            c = word[i]
            if c == ".":
                for child in root.children.values():
                    if dfs(i + 1, child):
                        return True
            if c in root.children:
                return dfs(i + 1, root.children[c])

            return False

        return dfs(0, self.root)


# 63
class Solution:
    def __init__(self):
        self.root = TrieNode()

    def addWords(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.isEnd = True

    def findWords(self, board, words):
        row, col = len(board), len(board[0])
        rowBound, colBound = range(row), range(col)
        path = set()
        result = set()

        for word in words:
            self.addWords(word)

        def dfs(r, c, node, word):
            if (
                r not in rowBound
                or c not in colBound
                or (r, c) in path
                or board[r][c] not in node.children
            ):
                return

            path.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isEnd:
                result.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            path.remove((r, c))

        for r in rowBound:
            for c in colBound:
                dfs(r, c, self.root, "")

        return list(result)


# 64
def minPathSum(grid):
    row, col = len(grid), len(grid[0])
    rowBound, colBound = range(row), range(col)

    for r in rowBound:
        for c in colBound:
            if r > 0 and c > 0:
                grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])
            elif r > 0:
                grid[r][0] += grid[r - 1][0]
            elif c > 0:
                grid[0][c] += grid[0][c - 1]
    return grid[row - 1][col - 1]

# 65
def lastStoneWeight(stones):
    stones = [-abs(n) for n in stones]
    heapq.heapify(stones)

    while True:
        if len(stones) == 1:
            return abs(stones[0])
        elif len(stones) == 0:
            return 0
        else:
            x, y = heapq.heappop(stones), heapq.heappop(stones)
            heapq.heappush(stones, x - y)

# 66
def kClosest(points, k):
    minHeap = []
    res = []
    
    for x, y in points:
        dist = (x**2) + (y**2)
        heapq.heappush(minHeap, [dist, x, y])
    
    for _ in range(k):
        res.append(heapq.heappop(minHeap)[1:])
    
    return res

# 67
def findKthLargest(nums, k):
    minHeap = nums
    heapq.heapify(minHeap)
    while len(minHeap) > k:
        heapq.heappop(minHeap)
    return minHeap[0]

# 68

            
        
        
    