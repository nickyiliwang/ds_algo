#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#
# https://leetcode.com/problems/gas-station/description/
#
# There are n gas stations along a circular route, where the amount of gas at
# the i^th station is gas[i].
#
# You have a car with an unlimited gas tank and it costs cost[i] of gas to
# travel from the i^th station to its next (i + 1)^th station. You begin the
# journey with an empty tank at one of the gas stations.
#
# Given two integer arrays gas and cost, return the starting gas station's
# index if you can travel around the circuit once in the clockwise direction,
# otherwise return -1. If there exists a solution, it is guaranteed to be
# unique
#
#
# Example 1:
#
#
# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 +
# 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to
# station 3.
# Therefore, return 3 as the starting index.
#
#
# Example 2:
#
#
# Input: gas = [2,3,4], cost = [3,4,3]
# Output: -1
# Explanation:
# You can't start at station 0 or 1, as there is not enough gas to travel to
# the next station.
# Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 =
# 4
# Travel to station 0. Your tank = 4 - 3 + 2 = 3
# Travel to station 1. Your tank = 3 - 3 + 3 = 3
# You cannot travel back to station 2, as it requires 4 unit of gas but you
# only have 3.
# Therefore, you can't travel around the circuit once no matter where you
# start.
#
#
#
# Constraints:
#
#
# n == gas.length == cost.length
# 1 <= n <= 10^5
# 0 <= gas[i], cost[i] <= 10^4
#
#
#
from re import A
from typing import List

# Key:
# sum of gas has to be more than cost
# total < 0 : only when total dips below 0 we move the index forward
# reset the total for next iteration


# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                res = i + 1
                total = 0

        return res


# @lc code=end

print(
    Solution().canCompleteCircuit(
        [1, 2, 3, 4, 5],
        [3, 4, 5, 1, 2],
    )
)


# 33/40 cases passed (N/A)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []

        for i in range(len(gas)):
            diff.append(gas[i] - cost[i])

        if len(diff) == 1 and diff[0] >= 0:
            return 0

        for i, n in enumerate(diff):
            if n > 0:
                starting = 0
                for travel in diff[i:]:
                    starting += travel
                    if starting < 0:
                        break

                for travel in diff[:i]:
                    starting += travel
                    if starting < 0:
                        break

                if starting >= 0:
                    return i

        return -1
