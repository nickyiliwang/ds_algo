#
# @lc app=leetcode id=441 lang=python
#
# [441] Arranging Coins
#
# https://leetcode.com/problems/arranging-coins/description/
#
# algorithms
# Easy (46.43%)
# Likes:    3726
# Dislikes: 1296
# Total Accepted:    408.5K
# Total Submissions: 879.5K
# Testcase Example:  '5'
#
# You have n coins and you want to build a staircase with these coins. The
# staircase consists of k rows where the i^th row has exactly i coins. The last
# row of the staircase may be incomplete.
#
# Given the integer n, return the number of complete rows of the staircase you
# will build.
#
#
# Example 1:
#
#
# Input: n = 5
# Output: 2
# Explanation: Because the 3^rd row is incomplete, we return 2.
#
#
# Example 2:
#
#
# Input: n = 8
# Output: 3
# Explanation: Because the 4^th row is incomplete, we return 3.
#
#
#
# Constraints:
#
#
# 1 <= n <= 2^31 - 1
#
#
#


# @lc code=start
# Binary Search + Gauss' formula
class Solution(object):
    def arrangeCoins(self, n):
        left, right = 1, n
        res = 0

        while left <= right:
            mid = (left + right) // 2
            need = (mid / 2) * (1 + mid)
            if need > n:
                right = mid - 1
            else:
                left = mid + 1
                res = mid
        return res


# @lc code=end

print(Solution.arrangeCoins("", 5))


# Gauss' formula: (i / 2) * (1 + i)
class Solution(object):
    def arrangeCoins(self, n):
        i = 1

        while (i / 2) * (1 + i) <= n:
            i += 1

        return i - 1


# Simple solution, O(n)
class Solution(object):
    def arrangeCoins(self, n):
        result = n
        row = 1

        while row <= result:
            result = result - row
            row += 1

        return row - 1


# Memory Limit Exceeded
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = n
        for i in range(n):
            if total > (i + 1):
                total = total - (i + 1)
            elif total == (i + 1):
                return i + 1
            else:
                return i


# KEKbonacci sequence
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
