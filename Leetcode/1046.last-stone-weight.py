#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#
# https://leetcode.com/problems/last-stone-weight/description/
#
# algorithms
# Easy (65.20%)
# Likes:    5837
# Dislikes: 103
# Total Accepted:    571.1K
# Total Submissions: 876K
# Testcase Example:  '[2,7,4,1,8,1]'
#
# You are given an array of integers stones where stones[i] is the weight of
# the i^th stone.
#
# We are playing a game with the stones. On each turn, we choose the heaviest
# two stones and smash them together. Suppose the heaviest two stones have
# weights x and y with x <= y. The result of this smash is:
#
#
# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has
# new weight y - x.
#
#
# At the end of the game, there is at most one stone left.
#
# Return the weight of the last remaining stone. If there are no stones left,
# return 0.
#
#
# Example 1:
#
#
# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the
# value of the last stone.
#
#
# Example 2:
#
#
# Input: stones = [1]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000
#
#
#
from typing import List


import heapq


# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stones = list(map(lambda n: -abs(n), stones))
        # turning negative here so we can have a max heap
        # [1,2,3] => [-3, -2, -1]  <= stone[0] will always be largest
        stones = [-abs(n) for n in stones]

        heapq.heapify(stones)

        while True:
            if len(stones) == 1:
                return abs(stones[0])

            elif len(stones) == 0:
                return 0
            else:
                x, y = heapq.heappop(stones), heapq.heappop(stones)
                x = x - y
                heapq.heappush(stones, x)


# @lc code=end

solution = Solution()

print(solution.lastStoneWeight([2, 7, 4, 1, 8, 1]))
