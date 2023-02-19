from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])

        return min(cost[i], cost[i + 1])

# This function takes in a list of integers called cost, representing the cost of each step on a staircase. The goal is to find the minimum cost to reach the top of the staircase, where you can climb either one or two steps at a time.

# To solve this problem, the function appends a 0 to the end of the cost list to represent the cost of reaching the top of the staircase. Then, it uses a loop to iterate over the cost list backwards, starting from the second-to-last element and ending at the first element. For each element i, the function calculates the minimum cost to reach that step by adding the current cost cost[i] to the minimum of the cost of reaching the next step cost[i+1] or the step after that cost[i+2]. This is because you can only climb one or two steps at a time, so the cost of reaching i depends on the minimum cost of reaching the two steps ahead.

# After iterating over the entire cost list, the function returns the minimum of the cost of reaching the first step cost[0] or the second step cost[1]. This is because you can start by climbing either one or two steps at the beginning.

# Therefore, the function finds the minimum cost to reach the top of the staircase using dynamic programming approach in O(n) time complexity.


print(Solution.minCostClimbingStairs(1, [10, 15, 20]))
