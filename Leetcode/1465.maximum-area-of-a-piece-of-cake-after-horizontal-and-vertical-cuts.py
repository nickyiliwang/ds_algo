#
# @lc app=leetcode id=1465 lang=python3
#
# [1465] Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
#
# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/description/
#
# algorithms
# Medium (41.05%)
# Likes:    2615
# Dislikes: 350
# Total Accepted:    167.7K
# Total Submissions: 408.6K
# Testcase Example:  '5\n4\n[1,2,4]\n[1,3]'
#
# You are given a rectangular cake of size h x w and two arrays of integers
# horizontalCuts and verticalCuts where:
# 
# 
# horizontalCuts[i] is the distance from the top of the rectangular cake to the
# i^th horizontal cut and similarly, and
# verticalCuts[j] is the distance from the left of the rectangular cake to the
# j^th vertical cut.
# 
# 
# Return the maximum area of a piece of cake after you cut at each horizontal
# and vertical position provided in the arrays horizontalCuts and verticalCuts.
# Since the answer can be a large number, return this modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
# Output: 4 
# Explanation: The figure above represents the given rectangular cake. Red
# lines are the horizontal and vertical cuts. After you cut the cake, the green
# piece of cake has the maximum area.
# 
# 
# Example 2:
# 
# 
# Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
# Output: 6
# Explanation: The figure above represents the given rectangular cake. Red
# lines are the horizontal and vertical cuts. After you cut the cake, the green
# and yellow pieces of cake have the maximum area.
# 
# 
# Example 3:
# 
# 
# Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# 2 <= h, w <= 10^9
# 1 <= horizontalCuts.length <= min(h - 1, 10^5)
# 1 <= verticalCuts.length <= min(w - 1, 10^5)
# 1 <= horizontalCuts[i] < h
# 1 <= verticalCuts[i] < w
# All the elements in horizontalCuts are distinct.
# All the elements in verticalCuts are distinct.
# 
# 
#

# @lc code=start
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
# @lc code=end

