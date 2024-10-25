from typing import List


## unique paths
def uniquePaths(self, m: int, n: int) -> int:
    row = [1] * n

    for i in range(m - 1):
        newRow = [1] * n
        for j in range(n - 2, -1, -1):
            newRow[j] = newRow[j + 1] + row[j]
        row = newRow
    return row[0]


## longest common subsequence
def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

    return dp[0][0]


## bet time to buy and sell stock with cooldown
def maxProfit(self, prices: List[int]) -> int:
    dp = {}

    def dfs(i, buying):
        if i >= len(prices):
            return 0
        if (i, buying) in dp:
            return dp[(i, buying)]

        cooldown = dfs(i + 1, buying)
        if buying:
            buy = dfs(i + 1, not buying) - prices[i]
            dp[(i, buying)] = max(buy, cooldown)
        else:
            sell = dfs(i + 2, not buying) + prices[i]
            dp[(i, buying)] = max(sell, cooldown)
        return dp[(i, buying)]

    return dfs(0, True)


## coin change II
def change(self, amount: int, coins: List[int]) -> int:
    cache = {}

    def dfs(i, a):
        if a == amount:
            return 1
        if a > amount:
            return 0
        if (i, a) in cache:
            return cache[(i, a)]

        cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
        return cache[(i, a)]

    return dfs(0, 0)


def changeDP(self, amount: int, coins: List[int]) -> int:
    dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
    dp[0] = [1] * (len(coins) + 1)
    for a in range(1, amount + 1):
        for i in range(len(coins) - 1, -1, -1):
            dp[a][i] = dp[a][i + 1]
            if a - coins[i] >= 0:
                dp[a][i] += dp[a - coins[i]][i]
    return dp[amount][0]


def changeDP2(self, amount: int, coins: List[int]) -> int:
    dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
    dp[0] = 1
    for i in range(len(coins) - 1, -1, -1):
        nextDP = [0] * (amount + 1)
        nextDP[0] = 1

        for a in range(1, amount + 1):
            nextDP[a] = dp[a]
            if a - coins[i] >= 0:
                nextDP[a] += nextDP[a - coins[i]]
        dp = nextDP
    return dp[amount]


## target sum
def findTargetSumWays(self, nums: List[int], target: int) -> int:
    dp = {}

    def backtrack(i, total):
        if i == len(nums):
            return 1 if total == target else 0
        if (i, total) in dp:
            return dp[(i, total)]

        dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(
            i + 1, total - nums[i]
        )
        return dp[(i, total)]

    return backtrack(0, 0)


## interleaving string
def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False

    dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
    dp[len(s1)][len(s2)] = True

    for i in range(len(s1), -1, -1):
        for j in range(len(s2), -1, -1):
            if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                dp[i][j] = True
            if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                dp[i][j] = True
    return dp[0][0]


## longest increasing path in a matrix
def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    rows, cols = len(matrix), len(matrix[0])
    dp = {}

    def dfs(r, c, prevVal):
        if r < 0 or r == rows or c < 0 or c == cols or matrix[r][c] <= prevVal:
            return 0
        if (r, c) in dp:
            return dp[(r, c)]

        res = 1
        res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
        res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
        res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
        res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
        dp[(r, c)] = res
        return res

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, -1)

    return max(dp.values())


## distinct subsequences
def numDistinct(self, s: str, t: str) -> int:
    cache = {}

    for i in range(len(s) + 1):
        cache[(i, len(t))] = 1
    for j in range(len(t)):
        cache[(len(s), j)] = 0

    for i in range(len(s) - 1, -1, -1):
        for j in range(len(t) - 1, -1, -1):
            if s[i] == t[j]:
                cache[(i, j)] = cache[(i + 1, j)]
            else:
                cache[(i, j)] = cache[(i + 1, j)]
    return cache[(0, 0)]


## edit distance
def minDistance(self, word1: str, word2: str) -> int:
    dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

    for j in range(len(word2) + 1):
        dp[len(word1)][j] = len(word2) - j
    for i in range(len(word1) + 1):
        dp[i][len(word2)] = len(word1) - i

    for i in range(len(word1) - 1, -1, -1):
        for j in range(len(word2) - 1, -1, -1):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i + 1][j + 1]
            else:
                dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
    return dp[0][0]


## burst balloons
def maxCoins(self, nums: List[int]) -> int:
    cache = {}
    nums = [1] + nums + [1]

    for offset in range(2, len(nums)):
        for left in range(len(nums) - offset):
            right = left + offset
            for pivot in range(left + 1, right):
                coins = nums[left] * nums[pivot] * nums[right]
                coins += cache.get((left, pivot), 0) + cache.get((pivot, right), 0)
                cache[(left, right)] = max(coins, cache.get((left, right), 0))
    return cache.get((0, len(nums) - 1), 0)


## regular expression matching
def isMatchBottomUpDP(self, s: str, p: str) -> bool:
    cache = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
    cache[len(s)][len(p)] = True

    for i in range(len(s), -1, -1):
        for j in range(len(p) - 1, -1, -1):
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if (j + 1) < len(p) and p[j + 1] == "*":
                cache[i][j] = cache[i][j + 2]
                if match:
                    cache[i][j] = cache[i + 1][j] or cache[i][j]
            elif match:
                cache[i][j] = cache[i + 1][j + 1]
    return cache[0][0]


def isMatchTopDown(self, s: str, p: str) -> bool:
    cache = {}

    def dfs(i, j):
        if (i, j) in cache:
            return cache[(i, j)]
        if i >= len(s) and j >= len(p):
            return True
        if j >= len(p):
            return False
        match = i < len(s) and (s[i] == p[j] or p[j] == ".")
        if (j + 1) < len(p) and p[j + 1] == "*":
            cache[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
            return cache[(i, j)]
        cache[(i, j)] = False
        return False

    return dfs(0, 0)
