def maxProfit(prices):
    if not prices:
        return 0
    res = 0
    left, right = 0, 1

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            res = max(res, profit)
        else:
            left = right
        right += 1

    return res


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
            # buy low sell high: if the prices[left] > prices[right]
            # means we found a new low, therefore need to switch to buying that day
            left = right
        right += 1

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
