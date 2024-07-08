#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
# https://leetcode.com/problems/koko-eating-bananas/description/
#
# Koko loves to eat bananas. There are n piles of bananas, the i^th pile has
# piles[i] bananas. The guards have gone and will come back in h hours.
#
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she
# chooses some pile of bananas and eats k bananas from that pile. If the pile
# has less than k bananas, she eats all of them instead and will not eat any
# more bananas during this hour.
#
# Koko likes to eat slowly but still wants to finish eating all the bananas
# before the guards return.
#
# Return the minimum integer k such that she can eat all the bananas within h
# hours.
#
#
# Example 1:
#
#
# Input: piles = [3,6,7,11], h = 8
# Output: 4
#
#
# Example 2:
#
#
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
#
#
# Example 3:
#
#
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
#
#
#
# Constraints:
#
#
# 1 <= piles.length <= 10^4
# piles.length <= h <= 10^9
# 1 <= piles[i] <= 10^9
#
from typing import *
from collections import *
from math import *

# Time:
# Space:

# Key: 
# celi to round up because we are not gonna not eat the banana if we start
#       7 / 4 = 1.75
# update the result each time the right pointer is shifting:
#       meaning eating less banana and increasing time to consume
# break out if totalTime > than h


# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

# @lc code=end

print(Solution().minEatingSpeed([30, 11, 23, 4, 20], 5))
