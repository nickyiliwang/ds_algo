# bottom up DP solution


class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one

# Explanation
# Going from the bottom base case, because going up, every decision depends on the previous two base.


print(
    Solution.climbStairs(1, 5)
)


# class Solution:
#     def climbStairs(self, n: int) -> int:

#         # dfs approach
#         def helper(n, index, memo={}):

#             # base case
#             if index > n:
#                 return 0

#             if index == n:
#                 memo[index] = 1
#                 return 1

#             if index in memo:
#                 return memo[index]
#             # recursion case
#             memo[index] = (helper(n, index+1, memo) + helper(n, index+2, memo))

#             return memo[index]
#         return helper(n, 0)
