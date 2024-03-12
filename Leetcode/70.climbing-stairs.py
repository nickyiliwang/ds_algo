#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (52.83%)
# Likes:    21408
# Dislikes: 779
# Total Accepted:    3.1M
# Total Submissions: 5.9M
# Testcase Example:  '2'
#
# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
#
#
# Example 1:
#
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
#
# Example 2:
#
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
#
# Constraints:
#
#
# 1 <= n <= 45
#
#
#

# Dynamic Programming solution


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        oneBefore = 1
        twoBefore = 1
        total = 0

        for _ in range(2, n + 1):
            total = oneBefore + twoBefore
            twoBefore = oneBefore
            oneBefore = total

        return total


# @lc code=end

print(Solution().climbStairs(5))


# Naive recursive:
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        if n == 2:
            return 2

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# Recursive with memoization
class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(n, memo):
            if n in memo:
                return memo[n]

            if n == 1:
                return 1

            if n == 2:
                return 2

            memo[n] = climb(n - 1, memo) + climb(n - 2, memo)

            return memo[n]

        return climb(n, {})
