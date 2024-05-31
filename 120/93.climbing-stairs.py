#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
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

# Key:
# [two, one, 2, 3, 4 ]
# one will keep track of the total
# range(n - 1) because we only need to loop n - 1 times
# think of it like range(2, n + ) if you like
# total starts at 1 because constrains: 1 <= n <= 45


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for _ in range(n - 1):
            tmp = one + two
            two = one
            one = tmp

        return one


# @lc code=end

print(Solution().climbStairs(5))

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
