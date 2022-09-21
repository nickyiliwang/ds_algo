# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.


# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104


# Two pointer
# time: O(n), space: O(1)
def maxProfit(prices):
    if not prices:
        return 0
    res = 0
    left, right = 0, 1

    while right < len(prices):
        # check if profitable
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            res = max(res, profit)
        else:
            # because we want to buy low, if right prices is lower than left
            # we want the left to go to right
            left = right
        right += 1

    print(res)
    return res


prices = [2, 1, 2, 1, 0, 1, 2]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

maxProfit(prices)


# # brute force
# def maxProfit(prices):
#     if not prices:
#         return 0
#     res = 0
#     for i in range(len(prices)):
#         for j in range(i, len(prices)):
#             # sell - buy = profit
#             profit = prices[j] - prices[i]
#             print(profit)
#             res = max(res, profit)
#     print(res)
#     return res


# prices = [7, 1, 5, 3, 6, 4]
# # Output: 5
# # Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# # Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# maxProfit(prices)
