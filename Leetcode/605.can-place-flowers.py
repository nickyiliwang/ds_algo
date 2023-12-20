#
# @lc app=leetcode id=605 lang=python
#
# [605] Can Place Flowers
#
# https://leetcode.com/problems/can-place-flowers/description/
#
# algorithms
# Easy (30.20%)
# Likes:    6107
# Dislikes: 1080
# Total Accepted:    626.6K
# Total Submissions: 2.1M
# Testcase Example:  '[1,0,0,0,1]\n1'
#
# You have a long flowerbed in which some of the plots are planted, and some
# are not. However, flowers cannot be planted in adjacent plots.
#
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty
# and 1 means not empty, and an integer n, return true if n new flowers can be
# planted in the flowerbed without violating the no-adjacent-flowers rule and
# false otherwise.
#
#
# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
#
#
# Constraints:
#
#
# 1 <= flowerbed.length <= 2 * 10^4
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length
#
#
#


# @lc code=start
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        # this is O(n) memory because new list
        bed = [0] + flowerbed + [0]
        # Skip first and last
        for i in range(1, len(bed) - 1):
            if (bed[i - 1] == 0) and (bed[i] == 0) and (bed[i + 1] == 0):
                bed[i] = 1
                n -= 1

        return n <= 0


# @lc code=end


Solution.canPlaceFlowers("", [1, 0, 0, 0, 1, 0, 0], 2)


# My pointer solution
# this is O(n) memory because new list
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        bed = [0] + flowerbed + [0]

        pointer = 1
        plant = 0

        while pointer <= len(bed) - 2:
            if (
                (bed[pointer - 1] == 0)
                and (bed[pointer] == 0)
                and (bed[pointer + 1] == 0)
            ):
                bed[pointer] = 1
                plant += 1
            pointer += 1

        return plant >= n
