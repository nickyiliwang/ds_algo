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
def leastInterval(tasks, n):
    maxHeap = [[-val, key] for key, val in Counter(tasks).items()]
    heapq.heapify(maxHeap)
    res = []

    while maxHeap:
        temp = []
        for _ in range(n + 1):
            if maxHeap:
                task = heapq.heappop(maxHeap)
                task[0] += 1
                if task[0]:
                    temp.append(task)
                    res.append(task[1])
                else:
                    res.append("idle")
        for task in temp:
            heapq.heappush(maxHeap, task)

    while res[-1] == "idle":
        res.pop()

    return len(res)


# 69
class Twitter:
    def __init__(self):
        self.followDB = defaultdict(set)
        self.feed = deque([])

    def postTweet(self, userId, tweetId):
        self.feed.appendleft([userId, tweetId])

    def getNewsFeed(self, userId):
        res = []

        self.followDB[userId].add(userId)
        for tweet in self.feed:
            if tweet[0] in self.followDB[userId] and len(res) < 10:
                res.append(tweet[1])

        return res

    def follow(self, followerId, followeeId):
        self.followDB[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.followDB[followerId].discard(followeeId)


# 70
class MedianFinder:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        self.count = 0
        heapq.heapify(self.maxHeap)
        heapq.heapify(self.minHeap)

    def addNum(self, num):
        heapq.heappush(self.maxHeap, -num)

        if self.maxHeap and self.minHeap and (-self.maxHeap[0] > self.minHeap[0]):
            largestLeft = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, largestLeft)

        if len(self.maxHeap) - len(self.minHeap) > 1:
            largestLeft = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, largestLeft)

        if len(self.minHeap) - len(self.maxHeap) > 1:
            smallestRight = -heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, smallestRight)

        self.count += 1

    def findMedian(self):
        if self.count % 2 == 1:
            if len(self.maxHeap) > len(self.minHeap):
                return -self.maxHeap[0]
            else:
                return self.minHeap[0]
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2


# 71
def subsets(nums):
    res = []

    def dfs(i, subset):
        res.append(subset.copy())

        for j in range(i, len(nums)):
            dfs(j + 1, subset + [nums[j]])

    dfs(0, [])

    return res


# 72
def combinationSum(candidates, target):
    res = []

    def dfs(i, subset, total):
        if total == target:
            res.append(subset.copy())
            return
        elif total > target:
            return

        for j in range(i, len(candidates)):
            dfs(j, subset + [candidates[j]], total + candidates[j])

    dfs(0, [], 0)

    return res


# 73
def permute(nums):
    res = []

    def dfs(subset):
        if len(subset) == len(nums):
            res.append(subset.copy())
            return

        for n in nums:
            if n in subset:
                continue
            dfs(subset + [n])

        dfs([])

        return res


# 74
def subsetsWithDup(nums):
    res = []
    nums.sort()

    def backtrack(i, subset):
        res.append(subset.copy())

        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j - 1]:
                continue

            backtrack(j + 1, subset + [nums[j]])

    backtrack(0, [])

    return res


# 75
def combinationSum2(candidates, target):
    candidates.sort()
    res = []

    def dfs(i, subset, total):
        if total == target:
            res.append(subset)
            return
        elif total > target:
            return

        for j in range(i, len(candidates)):
            if j > i and candidates[j] == candidates[j - 1]:
                continue

            dfs(j + 1, subset + [candidates[j]], total + candidates[j])

        dfs(0, [], 0)

        return res


# 76
def exist(board, word):
    row, col = len(board), len(board[0])
    rowBound, colBound = range(row), range(col)
    path = set()

    def dfs(r, c, i):
        if i == len(word):
            return True

        if (
            r not in rowBound
            or c not in colBound
            or (r, c) in path
            or word[i] != board[r][c]
        ):
            return False

        path.add((r, c))
        res = (
            dfs(r - 1, c, i + 1)
            or dfs(r + 1, c, i + 1)
            or dfs(r, c - 1, i + 1)
            or dfs(r, c + 1, i + 1)
        )
        path.remove((r, c))

        return res

    for r in rowBound:
        for c in colBound:
            if dfs(r, c, 0):
                return True

    return False


# 77
def isPali(a):
    l, r = 0, len(a) - 1
    while l < r:
        if a[l] != a[r]:
            return False
        l += 1
        r -= 1

    return True


def partition(s):
    res = []

    def dfs(i, subset):
        if i >= len(s):
            res.append(subset.copy())
            return

        for j in range(i, len(s)):
            potential = s[i : j + 1]
            if isPali(potential):
                dfs(j + 1, subset + [potential])

    dfs(0, [])

    return res


# 78
def letterCombinations(digits):
    digDict = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    res = []

    def backtrack(i, str):
        if i == len(digits):
            res.append(str)
            return

        for char in digDict[digits[i]]:
            backtrack(i + 1, str + char)

    if digits:
        backtrack(0, "")

    return res


# 79
def solveNQueens(n):
    board = [["." for _ in range(n)] for _ in range(n)]
    res = []
    colPath = set()
    downRightDiagonal = set()
    upRightDiagonal = set()

    def backtrack(r):
        if r == n:
            formatted = ["".join(row) for row in board]
            res.append(formatted)
            return

        for c in range(n):
            if (
                c in colPath
                or (r + c) in upRightDiagonal
                or (r - c) in downRightDiagonal
            ):
                continue

            colPath.add(c)
            downRightDiagonal.add((r - c))
            upRightDiagonal.add((r + c))
            board[r][c] = "Q"
            backtrack(r + 1)
            colPath.remove(c)
            downRightDiagonal.remove((r - c))
            upRightDiagonal.remove((r + c))
            board[r][c] = "."

        backtrack(0)
        return res


# 80
def numIslands(grid):
    row, col = len(grid), len(grid[0])
    rowBound, colBound = range(row), range(col)
    visited = set()
    islands = 0

    def dfs(r, c):
        if (
            r not in rowBound
            or c not in colBound
            or grid[r][c] == "0"
            or (r, c) in visited
        ):
            return

        visited.add((r, c))
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

    for r in rowBound:
        for c in colBound:
            if grid[r][c] == "1" and (r, c) not in visited:
                islands += 1
                dfs(r, c)

    return islands


# 81
def cloneGraph(node):
    db = {}

    def dfs(node):
        if node in db:
            return db[node]

        clone = Node(node.val)
        db[node] = clone

        for n in node.neighbors:
            clone.neighbors.append(dfs(n))

        return clone

    return dfs(node) if node else None


# 82
def maxAreaOfIsland(grid):
    row, col = len(grid), len(grid[0])
    rowBound, colBound = range(row), range(col)
    visited = set()
    maxArea = 0

    def dfs(r, c):
        if (
            r not in rowBound
            or c not in colBound
            or (r, c) in visited
            or grid[r][c] == 0
        ):
            return 0

        visited.add((r, c))

        return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)

    for r in rowBound:
        for c in colBound:
            maxArea = max(maxArea, dfs(r, c))

    return maxArea


# 83
def pacificAtlantic(heights):
    row, col = len(heights), len(heights[0])
    rowBound, colBound = range(row), range(col)
    pacific, atlantic = set(), set()
    res = []

    def dfs(r, c, visited, prevHeight):
        if (
            r not in rowBound
            or c not in colBound
            or (r, c) in visited
            or heights[r][c] < prevHeight
        ):
            return

        visited.add((r, c))
        dfs(r - 1, c, visited, heights[r][c])
        dfs(r + 1, c, visited, heights[r][c])
        dfs(r, c - 1, visited, heights[r][c])
        dfs(r, c + 1, visited, heights[r][c])

    for r in rowBound:
        dfs(r, 0, pacific, heights[r][0])
        dfs(r, col - 1, atlantic, heights[r][col - 1])

    for c in colBound:
        dfs(0, c, pacific, heights[0][c])
        dfs(row - 1, c, atlantic, heights[row - 1][c])

    for r in rowBound:
        for c in colBound:
            if (r, c) in atlantic and (r, c) in pacific:
                res.append([r, c])

    return res


# 84
def solve(board):
    row, col = len(board), len(board[0])
    rowBound, colBound = range(row), range(col)

    def dfs(r, c):
        if r not in rowBound or c not in colBound or board[r][c] != "O":
            return

        board[r][c] = "T"

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

    for r in rowBound:
        dfs(r, 0)
        dfs(r, col - 1)

    for c in colBound:
        dfs(0, c)
        dfs(row - 1, c)

    for r in rowBound:
        for c in colBound:
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "T":
                board[r][c] = "O"


# 85
def orangesRotting(grid):
    row, col = len(grid), len(grid[0])
    rowBound, colBound = range(row), range(col)
    time, fresh = 0, 0
    q = deque()

    for r in rowBound:
        for c in colBound:
            if grid[r][c] == 1:
                fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])

    def rot(r, c):
        nonlocal fresh
        if r not in rowBound or c not in colBound or grid[r][c] != 1:
            return

        grid[r][c] = 2
        fresh -= 1
        q.append([r, c])

    while q and fresh:
        for _ in range(len(q)):
            r, c = q.popleft()

            rot(r - 1, c)
            rot(r + 1, c)
            rot(r, c - 1)
            rot(r, c + 1)

        time += 1


# 86
def islandsAndTreasure(grid):
    row, col = len(grid), len(grid[0])
    rowBound, colBound = range(row), range(col)
    q = deque()
    visited = set()
    dist = 0

    for r in rowBound:
        for c in colBound:
            if grid[r][c] == 0:
                q.append([r, c])
                visited.add((r, c))

    def mod(r, c):
        if (
            r not in rowBound
            or c not in colBound
            or (r, c) in visited
            or grid[r][c] == -1
        ):
            return

        visited.add((r, c))
        q.append([r, c])

    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            grid[r][c] = dist
            mod(r - 1, c)
            mod(r + 1, c)
            mod(r, c - 1)
            mod(r, c + 1)

        dist += 1


# 87
def canFinish(numCourses, prerequisites):
    graph = defaultdict(list)
    visited, cycle = set(), set()

    for crs, pre in prerequisites:
        graph[crs].append(pre)

    def dfs(crs):
        if crs in cycle:
            return False

        if crs in visited:
            return True

        cycle.add(crs)
        for pre in graph[crs]:
            if not dfs(pre):
                return False
        cycle.remove(crs)

        visited.add(crs)
        return True

    for c in range(numCourses):
        if not dfs(c):
            return False

    return True


# 88
def findOrder(numCourses, prerequisites):
    graph = defaultdict(list)
    cycle, visited = set(), set()
    res = []

    for crs, pre in prerequisites:
        graph[crs].append(pre)

    def dfs(crs):
        if crs in cycle:
            return False

        if crs in visited:
            return True

        cycle.add(crs)
        for pre in graph[crs]:
            if not dfs(pre):
                return False
        cycle.remove(crs)

        visited.add(crs)
        res.append(crs)
        return True

    for crs in range(numCourses):
        if not dfs(crs):
            return []

    return res


# 89
def findRedundantConnect(edges):
    parent = [i for i in range(len(edges) + 1)]
    rank = [i for i in range(len(edges) + 1)]

    def find(i):
        if parent[i] == i:
            return i
        else:
            return find(parent[i])

    def union(x, y):
        px, py = find(x), find(y)

        if px == py:
            return False

        if rank[px] > rank[py]:
            parent[px] = parent[py]
        else:
            parent[px] = py
            rank[py] += 1
        return True

    for x, y in edges:
        if not union(x, y):
            return [x, y]


# 90
def countComponents(n, edges):
    parent = [i for i in range(n)]
    rank = [i for i in range(n)]

    def find(i):
        if parent[i] == i:
            return i
        else:
            return find(parent[i])

    def union(x, y):
        px, py = find(x), find(y)

        if px == py:
            return 0

        if rank[px] > rank[py]:
            parent[px] = parent[py]
        else:
            parent[px] = py
            rank[py] += 1

        return 1

    res = n

    for x, y in edges:
        res -= union(x, y)

    return res


# 91
def validTree(n, edges):
    visited = set()
    adj = defaultdict(list)

    for src, dst in edges:
        adj[src].append(dst)
        adj[src].append(src)

    def dfs(node, prev):
        if node in visited:
            return False

        visited.add(node)

        for n in adj[node]:
            if n == prev:
                continue
            if not dfs(n, node):
                return False
        return True

    return dfs(0, -1) and len(visited) == n


# 92
def ladderLength(beginWord, endWord, wordList):
    graph = defaultdict(list)
    wordList.append(beginWord)
    q = deque([beginWord])
    res = 1
    visited = set()

    for w in wordList:
        for i in range(len(w)):
            pattern = w[:i] + "*" + w[i + 1 :]
            graph[pattern].append(w)

    while q:
        for _ in range(len(q)):
            w = q.popleft()

            if w == endWord:
                return res

            for i in range(len(w)):
                pattern = w[:i] + "*" + w[i + 1 :]

                for word in graph[pattern]:
                    if word not in visited:
                        visited.add(word)
                        q.append(word)
        res += 1
    return 0


# 93
def climbStairs(n):
    one, two = 1, 1

    for _ in range(n - 1):
        tmp = one + two
        two = one
        one = tmp

    return one


# 94
def minCostClimbingStairs(cost):
    for i in range(len(cost) - 3, -1, -1):
        cost[i] += min(cost[i + 1], cost[i + 2])

    return min(cost[0], cost[1])


# 95
def rob(nums):
    oneBefore, twoBefore = 0, 0
    for n in nums:
        tmp = max(twoBefore + n, oneBefore)
        twoBefore = oneBefore
        oneBefore = tmp

    return oneBefore


# 96
def rob(nums):
    if len(nums) == 1:
        return nums[0]

    def robHelper(nums):
        oneAway, twoAway = 0, 0
        for n in nums:
            tmp = max(twoAway + n, oneAway)
            twoAway = oneAway
            oneAway = tmp

        return oneAway

    withoutFirst = robHelper(nums[1:])
    withFirst = robHelper(nums[:-1])
    return max(withoutFirst, withFirst)


# 97
def longestPalindrome(s):
    res = ""
    resLen = 0

    def isPali(l, r):
        nonlocal res
        nonlocal resLen

        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (l - r + 1) > resLen:
                res = s[l : r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1

    for i in range(len(s)):
        l, r = i, i
        isPali(l, r)

        l, r = i, i + 1
        isPali(l, r)

    return res


# 98
def countSubstrings(s):
    res = 0

    def isPali(l, r):
        nonlocal res
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1

    for i in range(len(s)):
        l, r = i, i
        isPali(l, r)

        l, r = i, i + 1
        isPali(l, r)

    return res


# 99
def numDecodings(s):
    cache = {len(s): 1}

    def dfs(i):
        if i in cache:
            return cache[i]

        if s[i] == "0":
            return 0

        res = dfs(i + 1)
        if i + 1 < len(s) and 10 <= int(s[i : i + 2]) <= 26:
            res += dfs(i + 2)

        cache[i] = res

        return res

    return dfs(0)


# 100
def coinChange(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])

    return dp[amount] if dp[amount] != float("inf") else -1


