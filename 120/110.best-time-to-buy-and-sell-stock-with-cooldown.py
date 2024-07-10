#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# You are given an array prices where prices[i] is the price of a given stock
# on the i^th day.
#
# Find the maximum profit you can achieve. You may complete as many
# transactions as you like (i.e., buy one and sell one share of the stock
# multiple times) with the following restrictions:
#
#
# After you sell your stock, you cannot buy stock on the next day (i.e.,
# cooldown one day).
#
#
# Note: You may not engage in multiple transactions simultaneously (i.e., you
# must sell the stock before you buy again).
#
#
# Example 1:
#
#
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
#
#
# Example 2:
#
#
# Input: prices = [1]
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000
#
#
#
from typing import List

# Key
# selling +2 because you can't sell on the same day


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                selling = dfs(i + 2, not buying) + prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(selling, cooldown)

            return dp[(i, buying)]

        return dfs(0, True)


# @lc code=end

print(Solution().maxProfit([1, 2, 3, 0, 2]))
